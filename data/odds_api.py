import requests
import streamlit as st

API_KEY = "YOUR_API_KEY_HERE"

@st.cache_data(ttl=60)
def get_odds():
    try:
        url = f"https://api.the-odds-api.com/v4/sports/tennis_atp/odds/?apiKey={API_KEY}&regions=us&markets=h2h"
        r = requests.get(url)
        return r.json()
    except:
        return []
