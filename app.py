st.markdown("""
<style>
body {
    background-color: #080603;
}

.block-container {
    padding-top: 2rem;
}

.card {
    background: #171009;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #3a2010;
    margin-bottom: 12px;
}

.match-title {
    font-size: 20px;
    font-weight: 600;
    color: #f8efe8;
}

.subtext {
    font-size: 12px;
    color: #a07050;
}

.value {
    color: #c8f000;
    font-weight: bold;
}

.fade {
    color: #ff4444;
}
</style>
""", unsafe_allow_html=True)
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
