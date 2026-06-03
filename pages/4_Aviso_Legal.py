# -*- coding: utf-8 -*-
"""
Página de Disclaimer Legal
"""

import streamlit as st
from components.footer import footer

st.set_page_config(page_title="Aviso Legal", layout="wide")
st.sidebar.image("logo.png", width='content')

# ============================================================
# DISCLAIMER
# ============================================================

st.title("Aviso Legal")

st.markdown(
    """
Este sitio web presenta información puesta a disposición por el **Banco Central de la República Argentina (BCRA)** a través de su API **Régimen de Transparencia**.

Dicha información está constituida por datos sobre préstamos **Prendarios, Hipotecarios y Personales**, proporcionados al Banco Central de la República Argentina por las entidades financieras en cumplimiento del Régimen Informativo de Transparencia previsto por el referido organismo estatal.

La normativa correspondiente se encuentra publicada en la sección 36 del texto ordenado de 'Presentación de Informaciones al BCRA', pudiendo accederse a la misma a través del siguiente vínculo:  https://www.bcra.gob.ar/archivos/Pdfs/Texord/t-optico.pdf).

---

## Alcances y limitaciones

- Este sitio **no modifica, interpreta ni valida** los datos provistos por el BCRA.
- La información se muestra **tal como es publicada por la API oficial**, pudiendo contener errores, omisiones o actualizaciones pendientes.
- Los datos son utilizados **exclusivamente con fines informativos**.
- Este sitio **no representa al BCRA ni a ninguna entidad financiera**.
- La información expuesta en este sitio **no constituye en ningún caso** un ofrecimiento de servicios financieros, comerciales ni de asesoramiento.
- Este sitio **no efectúa recomendación, promoción o evaluación** respecto de los préstamos expuestos en el mismo así como tampoco de los servicios ofrecidos por entidad financiera alguna.

---

## Actualización de datos

- La información se actualiza automáticamente **una vez por día**.
- Los datos mostrados corresponden a los últimos **12 meses** publicados por la API.
- La disponibilidad de la información depende del funcionamiento del servicio del BCRA.

---

## Uso de la información

El usuario es responsable de:

- Verificar la vigencia y exactitud de los datos.
- Consultar directamente a las entidades financieras para obtener condiciones actualizadas.
- Utilizar la información de manera adecuada y conforme a la normativa vigente.

---

## Contacto

Si necesitás reportar un error técnico del sitio, podés comunicarte con el administrador del sistema.

"""
)
footer()

