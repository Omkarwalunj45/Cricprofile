import streamlit as st
import pandas as pd

player_data = pd.read_csv("Dataset/WT20I_Bat.csv")
player_info = pd.read_csv("Dataset/squads.csv")
st.set_page_config(page_title='WT20I Performance Analysis Portal', layout='wide')
st.title('WT20I Performance Analysis Portal')
