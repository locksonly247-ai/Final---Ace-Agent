import streamlit as st
from models.prediction import win_probability
from utils.helpers import american_to_prob, calc_edge

def render_match_cards(matches, odds_data):

    for m in matches:
        p1, p2 = m["players"]

        st.markdown(f"### {p1} vs {p2}")

        model_p = win_probability("#20", "#30")

        vegas_p = 0.5  # fallback

        edge = calc_edge(model_p, vegas_p)

        st.write(f"Model Prob: {model_p}")
        st.write(f"Edge: {edge}%")

        if edge > 5:
            st.success("🔥 VALUE BET")
        elif edge < -5:
            st.error("❌ FADE")
