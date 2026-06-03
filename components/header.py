# -*- coding: utf-8 -*-
"""
Created on Wed May  6 23:24:33 2026

@author: gdv19
"""
import streamlit as st
import base64

def header():
    with open("logo.png", "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <div style="display:flex; align-items:center; gap:10px; margin-bottom:5px;">
            <img src="data:image/png;base64,{encoded}" width="35">
            <span style="font-size:1.2em; font-weight:600; font-family:serif;">
                Ad Rationibus
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
