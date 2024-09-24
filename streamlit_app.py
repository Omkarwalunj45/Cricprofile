import streamlit as st
import pandas as pd

# Create the Streamlit app
st.set_page_config(page_title='Player Profile')
# Load the player data from the Excel sheet
player_data = pd.read_csv("Dataset/WT20I_Bat.csv")
player_info = pd.read_csv("Dataset/squads.csv")

# Add a sidebar for the player search
st.sidebar.title('Player Search')
search_term = st.sidebar.text_input('Enter player name:')

# Filter the player data based on the search term
filtered_players = player_data[player_data['batsman'].str.contains(search_term, case=False)]

# Display the player profile
if not filtered_players.empty:
    for _, player in filtered_players.iterrows():
        st.title(player['batsman'])
        # st.subheader(f"{player['Age']} years old")
        # st.text(player_info['batting_hand'])
        # st.text(f"Bowling style: {player['Bowling Style']}")
        # st.text(f"Playing role: {player['Playing Role']}")
        # st.subheader('Career Performance')
        st.dataframe(player_data[['runs', 'ball', 'SR']])
else:
    st.write('No player found.')
