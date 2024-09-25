import streamlit as st
import pandas as pd
st.set_page_config(page_title='WT20I Performance Analysis Portal', layout='wide')
st.title('WT20I Performance Analysis Portal')

pdf = pd.read_csv("Dataset/WT20I_Bat.csv")
idf = pd.read_csv("Dataset/squads.csv")
