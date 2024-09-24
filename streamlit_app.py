import streamlit as st

st.title('Cricketer Profile Dashboard (Women)')
st.header("ICC Women's T20WC 2024")
import pandas as pd


# Load the player data from the Excel sheet
player_data = pd.read_excel('player_data.xlsx')

# Create the Streamlit app
st.set_page_config(page_title='Player Profile')

# Add a sidebar for the player search
st.sidebar.title('Player Search')
search_term = st.sidebar.text_input('Enter player name:')

# Filter the player data based on the search term
filtered_players = player_data[player_data['Name'].str.contains(search_term, case=False)]

# Display the player profile
if not filtered_players.empty:
    for _, player in filtered_players.iterrows():
        st.title(player['Name'])
        st.subheader(f"{player['Age']} years old")
        st.text(f"Batting style: {player['Batting Style']}")
        st.text(f"Bowling style: {player['Bowling Style']}")
        st.text(f"Playing role: {player['Playing Role']}")
        st.subheader('Career Performance')
        st.dataframe(player_data[['Runs', 'Balls', 'Strike Rate']])
else:
    st.write('No player found.')
