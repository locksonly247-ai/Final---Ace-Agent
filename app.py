import streamlit as st
from data.sofascore import get_live_matches
from data.odds_api import get_odds
from data.static_data import MATCHES
from components.live_scores import render_live_scores
from components.match_cards import render_match_cards

st.set_page_config(layout="wide")

st.title("🎾 ACE AGENT PRO")
st.caption("Live ATP Betting Intelligence")

tab = st.radio("", ["Dashboard"])

if tab == "Dashboard":

    st.subheader("🔴 Live Matches")
    live = get_live_matches()
    render_live_scores(live)

    st.divider()

    st.subheader("📊 Betting Opportunities")

    odds_data = get_odds()
    render_match_cards(MATCHES, odds_data)
