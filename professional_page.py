# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:15:48 2024

@author: NeloAgbim
"""

import pandas as pd
import streamlit as st

#set page to wide configuration -- this way it takes up the whole page
st.set_page_config(layout="wide")

# create 2 columns on the page
left,right = st.columns([0.25,0.75], gap="medium")

with left:
  #linkedin pic in a container
  pic_container = st.container(border=True)
  with pic_container:
    st.image("./data/linkedin_photo.png")
  # hyperlink to linkedin profile
  st.write("[LinkedIn Profile](https://www.linkedin.com/in/chinelo-agbim-15b50a7a/)")
  st.write("Put link to resume here")
with right:
  st.title("Chinelo Agbim's Porfolio")
  st.header("About me")
  st.write( '''I'm an analyst with a passion for helping people through data.
  I am particularly interested in Clean Energy and creating a more equitable world.''')
  st.subheader("Portfolio Projects")
  st.container("Put drop down for portfolio projects.")
  st.subheader("Research and Publications")
  st.container("Put research and Publications")

