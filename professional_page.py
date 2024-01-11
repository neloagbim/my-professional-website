# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:15:48 2024

@author: NeloAgbim
"""

import pandas as pd
import streamlit as st

col1,col2 = st.columns([0.3,0.7])
with col1:
  st.text("put your picture here.")
with col2:
  st.title("Chinelo Agbim's Porfolio")
  st.header("About me")
  st.write("I'm an analyst with a passion for helping people through data.","", "I am particularly interested in Clean Energy and creating a more equitable world.")
