# app.py
import streamlit as st
from components.match_cards import render_match_cards
from components.live_scores import render_live_scores
from data.static_data import MATCHES, LIVE_EVENTS

# Custom CSS
st.markdown("""
<style>
body { background-color: #080603; color: #f8efe8; font-family: 'Arial', sans-serif; }
.block-container { padding-top: 2rem; max-width: 900px; margin: auto; }
.card { background: #171009; padding: 16px; border-radius: 12px; border: 1px solid #3a2010; margin-bottom: 12px; }
.match-title { font-size: 20px; font-weight: 600; color: #f8efe8; }
.subtext { font-size: 12px; color: #a07050; }
.fade { color: #ff4444; }
</style>
""", unsafe_allow_html=True)

# App Header
st.image("assets/logo.png", width=120)  # optional logo
st.title("🎾 Ace Agent - Tennis Betting Tool")

# Upcoming Matches
st.header("Upcoming Matches")
render_match_cards(MATCHES)

# Live Matches
st.header("Live Matches")
render_live_scores(LIVE_EVENTS)

