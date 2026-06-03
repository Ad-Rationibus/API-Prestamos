# -*- coding: utf-8 -*-
"""
Funciones compartidas para todas las páginas del sitio.
Incluye:
- Descarga automática diaria
- Carga de CSV
- Prettify de columnas
- Filtros dinámicos
"""

import re
import requests
import pandas as pd
from datetime import datetime, date
import streamlit as st


# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

ENDPOINTS = ['Prendarios', 'Hipotecarios', 'Personales']

# Lista maestra de campos para filtros (orden fijo)
MASTER_FIELDS = [
    'Relacion Monto Tasacion',
    'Destino Fondos',
    'Monto Minimo Otorgable',
    'Moneda',
    'Monto Maximo Otorgable',
    'Plazo Maximo Otorgable',
    'Ingreso Minimo Mensual',
    'Antiguedad Laboral Minima Meses',
    'Edad Maxima Solicitada',
    'Relacion Cuota Ingreso',
    'Beneficiario',
    'Cargo Maximo Cancelacion Anticipada',
    'Tasa Efectiva Anual Maxima',
    'Tipo Tasa',
    'Costo Financiero Efectivo Total Maximo',
    'Cuota Inicial',
    'Codigo Entidad',
    'Descripcion Entidad',
    'Fecha Informacion',
    'Nombre Completo',
    'Nombre Corto',
    'Territorio Validez',
    'Mas Informacion'
]


# ============================================================
# UTILIDADES
# ============================================================

def prettify(nombre: str) -> str:
    """Convierte nombres_de_columnas en formato legible."""
    nombre = nombre.replace("_", " ").replace("-", " ")
    nombre = re.sub(r"(?<!^)(?=[A-Z])", " ", nombre)
    return nombre.title()


# ============================================================
# DESCARGA Y CARGA DE DATOS
# ============================================================

def descargar_datos() -> None:
    """Descarga los datos desde la API del BCRA y los guarda como CSV."""
    for endpoint in ENDPOINTS:
        url = f'https://api.bcra.gob.ar/transparencia/v1.0/Prestamos/{endpoint}'
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['results'])
            df.to_csv(f'{endpoint}.csv', sep=';', decimal=',',
                      encoding='mbcs', index=False)
        else:
            st.error(f"Error {response.status_code} al descargar {endpoint}")

    st.session_state["ultima_descarga"] = datetime.now()


def necesita_descargar() -> bool:
    """Determina si es necesario descargar datos nuevamente."""
    if "ultima_descarga" not in st.session_state:
        return True
    return st.session_state["ultima_descarga"].date() < date.today()


def cargar_dataframes() -> dict:
    """Carga los CSV descargados y filtra por fecha."""
    dfs = {}

    for endpoint in ENDPOINTS:
        df = pd.read_csv(
            f"{endpoint}.csv",
            sep=';',
            decimal=',',
            encoding='mbcs'
        ).reset_index(drop=True)

        df['fechaInformacion'] = pd.to_datetime(df['fechaInformacion'],
                                                errors='coerce')

        limite = pd.Timestamp.today() - pd.Timedelta(days=365)
        df = df[df['fechaInformacion'] >= limite]

        dfs[endpoint] = df

    return dfs


# ============================================================
# FILTRADO
# ============================================================

def aplicar_filtros(df, filtros):
    """Aplica los filtros acumulados a un DataFrame."""
    mascara = pd.Series(True, index=df.index)
    for f in filtros.values():
        mascara &= f
    return df[mascara]


