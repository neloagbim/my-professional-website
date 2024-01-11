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
  st.title("Chinelo Agbim's Portfolio")
  st.header("About me")
  st.write( '''Hey there! My name is Chinelo, but my friends call me Nelo. I'm an analyst with a passion for 
  helping people and using data as a tool to do so. I recieved my B.S. in Civil Engineering, M.S. in Energy Resources, and a Master's in Public Policy. During my studies at UIUC and
  UT Austin, I did a lot of research on ways to ensure the energy transition is more equitable. More recently,
  I've worked for some lovely Clean Energy Tech companies in data analytics and management roles where I played a critical role in helping them do what they do best: 
  accelerate the clean energy transition. I've also done consulting working supporting companies improve data accessebility and decision making
  through the power of visualization and data modeling.
  Check out some of my publications and side projects below:
  ''')
  
  # add container and header for projects
  st.subheader("Portfolio Projects")
  with st.container():
    st.write("Put drop down for portfolio projects.")
  # add another container below it for Research
  st.subheader("Research and Publications")
  with st.container():
    st.write("Put research and Publications")

