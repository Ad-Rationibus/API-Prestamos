# -*- coding: utf-8 -*-
"""
Página principal del sitio – Presentación profesional
"""

import streamlit as st
from components.footer import footer

st.set_page_config(page_title="Consultas BCRA – Inicio", layout="wide")

# CSS personalizado para cambiar el ancho de la sidebar
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            width: 160px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.image("logo.png", width=160)

# ============================================================
# PRESENTACIÓN
# ============================================================

st.title("Consultas de Préstamos")
st.markdown(
    """
Bienvenido!

Este portal permite explorar, filtrar y descargar información actualizada sobre **préstamos Prendarios, Hipotecarios y Personales**, con datos provistos directamente por la API 'Régimen de Transparencia' del BCRA.

La información aquí expuesta se actualiza automáticamente todos los días y corresponde exclusivamente a préstamos ofrecidos por Entidades Financieras autorizadas por el Banco Central de la República Argentina.
"""
)

st.markdown("---")

# ============================================================
# SECCIONES VISUALES
# ============================================================

st.subheader("Tipos de préstamos disponibles")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🚗 Préstamos Prendarios")
    st.markdown(
        """
Créditos con garantía prendaria sobre automotores y otros bienes muebles registrables.
"""
    )
    st.page_link("pages/1_Prestamos_Prendarios.py", label="Ir a Prendarios")

with col2:
    st.markdown("### 🏠 Préstamos Hipotecarios")
    st.markdown(
        """
Créditos con garantía hipotecaria destinados a la compra, construcción o refacción de viviendas.

"""
    )
    st.page_link("pages/2_Prestamos_Hipotecarios.py", label="Ir a Hipotecarios")

with col3:
    st.markdown("### 💳 Préstamos Personales")
    st.markdown(
        """
Créditos sin garantía real, orientados al consumo general.
"""
    )
    st.page_link("pages/3_Prestamos_Personales.py", label="Ir a Personales")

st.markdown("---")

# ============================================================
# INFORMACIÓN ADICIONAL
# ============================================================

st.subheader("Sobre este sitio")

st.markdown(
    """
- Los datos provienen de la API **'Régimen de Transparencia'** publicada por el **BCRA**.
- La información se filtra para mostrar únicamente los últimos **12 meses**.
- Podés aplicar filtros por entidad, tasas, montos, plazos y más.
- Se exponen únicamente los campos más significativos (nombre de la entidad financiera, moneda, tasa, plazo, etc)
- Cada sección permite **descargar los datos filtrados** a un archivo en formato CSV que contiene todos los campos disponibles.
"""
)

st.markdown("---")

st.page_link("pages/4_Aviso_Legal.py", label="Ver Aviso Legal")

footer()
