# -*- coding: utf-8 -*-
"""
Página de Préstamos Hipotecarios
"""

import streamlit as st
import pandas as pd
from utils import (
    descargar_datos,
    necesita_descargar,
    cargar_dataframes,
    prettify,
    MASTER_FIELDS,
    aplicar_filtros
)
from components.footer import footer

# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(page_title="Préstamos Hipotecarios", layout="wide")

ENDPOINT = "Hipotecarios"

# Columnas a mostrar en la tabla
COLUMN_ORDER = [
    'Descripcion Entidad',
    'Nombre Completo',
    'Beneficiario',
    'Destino Fondos',
    'Moneda',
    'Tipo Tasa',
    'Costo Financiero Efectivo Total Maximo',
    'Plazo Maximo Otorgable'
]


# ============================================================
# DESCARGA AUTOMÁTICA
# ============================================================

if necesita_descargar():
    descargar_datos()

dfs = cargar_dataframes()
df = dfs[ENDPOINT].copy()

# Renombrar columnas
df.rename(columns={"denominacion": "Moneda"}, inplace=True)
df.columns = [prettify(col) for col in df.columns]


# ============================================================
# SIDEBAR DE FILTROS (ÚNICO)
# ============================================================

st.sidebar.markdown("## Filtros – Hipotecarios")

filtros = {}

st.sidebar.markdown("### Filtros básicos")

campos_a_usar = COLUMN_ORDER if COLUMN_ORDER else list(df.columns)

for campo in campos_a_usar:
    if campo not in df.columns:
        continue

    serie = df[campo]

    # Categóricos
    if serie.dtype == "str":
        valores = sorted(serie.dropna().unique(), key=lambda x: str(x))
        opciones = ["Todas"] + valores

        seleccion = st.sidebar.multiselect(
            campo,
            opciones,
            default=["Todas"],
            key=f"{campo}_multiselect_hipotecarios"
        )

        filtros[campo] = (
            pd.Series(True, index=df.index)
            if "Todas" in seleccion
            else serie.isin(seleccion)
        )

    # Texto
    elif not pd.api.types.is_numeric_dtype(serie) and not pd.api.types.is_datetime64_any_dtype(serie):
        texto = st.sidebar.text_input(
            campo,
            key=f"{campo}_text_hipotecarios"
        )
        filtros[campo] = (
            serie.astype(str).str.contains(texto, case=False, na=False)
            if texto
            else pd.Series(True, index=df.index)
        )

st.sidebar.markdown("---")
st.sidebar.markdown("### Filtros avanzados")

for campo in campos_a_usar:
    if campo not in df.columns:
        continue

    serie = df[campo]

    # Numéricos
    if pd.api.types.is_numeric_dtype(serie):
        serie_num = pd.to_numeric(serie, errors='coerce')
        valido = serie_num.dropna()

        if len(valido) == 0:
            filtros[campo] = pd.Series(True, index=df.index)
        else:
            minimo, maximo = float(valido.min()), float(valido.max())

            rango = st.sidebar.slider(
                campo,
                min_value=minimo,
                max_value=maximo,
                value=(minimo, maximo),
                key=f"{campo}_slider_hipotecarios"
            )

            filtros[campo] = (
                pd.Series(True, index=df.index)
                if rango == (minimo, maximo)
                else serie_num.between(rango[0], rango[1])
            )

    # Fechas
    elif pd.api.types.is_datetime64_any_dtype(serie):
        min_fecha, max_fecha = serie.min().date(), serie.max().date()

        fecha_sel = st.sidebar.date_input(
            campo,
            value=(min_fecha, max_fecha),
            min_value=min_fecha,
            max_value=max_fecha,
            key=f"{campo}_date_hipotecarios"
        )

        filtros[campo] = (
            pd.Series(True, index=df.index)
            if fecha_sel == (min_fecha, max_fecha)
            else serie.between(
                pd.to_datetime(fecha_sel[0]),
                pd.to_datetime(fecha_sel[1])
            )
        )


# ============================================================
# TABLA + DESCARGA
# ============================================================

st.title("Préstamos Hipotecarios – BCRA")
st.markdown("Consulta, filtrado y descarga de datos oficiales del BCRA.")

df_filtrado = aplicar_filtros(df, filtros)

col_a, col_b = st.columns([7, 1])

with col_a:
    st.info(f"Registros mostrados: {len(df_filtrado)} de {len(df)}")


with col_b:
    csv_completo = df_filtrado.to_csv(
        sep=';',
        decimal=',',
        encoding='utf-8',
        index=False
    )
    st.download_button(
        label="📥 Descargar CSV",
        data=csv_completo,
        file_name="Hipotecarios_filtrado.csv",
        mime="text/csv"
    )

st.data_editor(
    df_filtrado,
    width='content',
    column_order=COLUMN_ORDER,
    hide_index=True
)
footer()

