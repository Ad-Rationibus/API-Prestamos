# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:55:39 2026

@author: gdv19
"""
import streamlit as st

def footer():
    st.markdown(
        """
        <hr>
        <div style="text-align:center; color:gray; font-size:0.9em; padding-top:10px;">
            © 2026 –Ad Rationibus - Sitio de consulta de préstamos ofrecidos por Entidades Financieras autorizadas por el BCRA.<br>
            Datos provistos por la API 'Régimen de Transparencia' del Banco Central de la República Argentina.<br>
            Este sitio no representa al BCRA ni a ninguna entidad financiera.
        </div>
        """,
        unsafe_allow_html=True
    )

