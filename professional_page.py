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

# left column of page
with left:
  #linkedin pic in a container
  pic_container = st.container(border=True)
  with pic_container:
    st.image("./data/linkedin_photo.png")
  # hyperlink to linkedin profile, github, ..etc. not in same container as pic
  st.write("[LinkedIn Profile](https://www.linkedin.com/in/chinelo-agbim-15b50a7a/)")
  st.write("[GitHub](https://github.com/neloagbim)")
  st.write("[Request copy of my resume](https://drive.google.com/file/d/1h5XbDWqymzrqaqO9qni8VXJtIH9j0xjB/view?usp=drive_link)") 
# right column of the page
with right:
  st.title("Chinelo Agbim's Portfolio")
  st.header("About me")
  st.write( '''Hey there! My name is Chinelo, but my friends call me Nelo. I'm an analyst with a passion for 
  helping people and using data as a tool to do so. I received my B.S. in Civil Engineering, M.S. in Energy Resources, and a Master's in Public Policy. During my studies at UIUC and
  UT Austin, I did a lot of research on ways to ensure the energy transition is more equitable. More recently,
  I've worked for some lovely Clean Energy Tech companies in data analytics and management roles where I played a critical role in helping them do what they do best: 
  accelerate the clean energy transition. I've also done analytics consulting where I've improved data accessibility and decision making for clients
  through the power of visualization and data modeling.
  Check out some of my publications and side projects below:
  ''')
  
  # add container and header for projects
  st.subheader("Portfolio Projects")
  with st.container():
    # split container into 4 columns for each project
    col1,col2,col3,col4 = st.columns([0.25,0.25,0.25,0.25])
    # col1 - USDA project
    with col1:
      st.write("[USDA Open Dataset Summary](https://github.com/neloagbim/usda-data-summary/blob/main/README.md)")
      st.image("./data/usda.png", caption= "Skills: python, json manipulation, google sheet api")
    with col2:
      st.write("[EIA 860 Postgresql Upload](https://github.com/neloagbim/eia-860-data-summary)")
      st.image("./data/eia.png", caption = "Skills: python, webscrape, sqlalchemy, postgresql")
  # add another container below it for Research
  st.subheader("Research and Publications")
  with st.container():
    # split container into 4 columns for each project
    col5,col6,col7,col8 = st.columns([0.25,0.25,0.25,0.25])
    # col5 - energy policy publication
    with col5:
      st.write("[1st Author Publication - Energy Policy 2020](https://www.sciencedirect.com/science/article/abs/pii/S0301421520303529)")
      st.image("./data/electricity.png", caption="Skills: logistic regression, chi-squared, research, energy policy, writing")
    with col6:
      st.write("[Co-author - White Paper - UT Austin Energy Institute 2017](https://energy.utexas.edu/sites/default/files/UTAustin_FCe_UtilityBusModels_2017.pdf)")
      st.image("./data/electricity.png",caption = "Skills: distrubted energy, energy policy, utilities, writing")
    with col7:
      st.write("[Community Solar Brief - Greenlining Institute 2017](https://drive.google.com/file/d/1bdT-kpOx0ZLYFFv4I8cDYT1KasaAuhB0/view?usp=drive_link)")
      st.image("./data/electricity.png",caption = "Skills: distrubted energy, energy policy, energy equity, communication")

