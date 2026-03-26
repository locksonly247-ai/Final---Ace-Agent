import requests
import streamlit as st

API_KEY = "096702a1936e38b0594bac42b59e6214"

@st.cache_data(ttl=60)
def get_odds():
    try:
        url = f"https://api.the-odds-api.com/v4/sports/tennis_atp/odds/?apiKey={API_KEY}&regions=us&markets=h2h"
        r = requests.get(url)
        return r.json()
    except:
        return []
