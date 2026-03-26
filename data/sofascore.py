import requests
import streamlit as st

@st.cache_data(ttl=10)
def get_live_matches():
    try:
        url = "https://api.sofascore.com/api/v1/sport/tennis/events/live"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = r.json()

        events = []
        for e in data.get("events", []):
            if "ATP" in e.get("tournament", {}).get("name", ""):
                events.append({
                    "p1": e["homeTeam"]["name"],
                    "p2": e["awayTeam"]["name"],
                    "status": e["status"]["description"]
                })
        return events
    except:
        return []
