import streamlit as st
from models.prediction import win_probability
from utils.helpers import american_to_prob, calc_edge

def render_match_cards(matches, odds_data):

    for m in matches:
        p1, p2 = m["players"]

        model_p = win_probability("#20", "#30")
        vegas_p = 0.5
        edge = calc_edge(model_p, vegas_p)

        st.markdown(f"""
        <div class="card">
            <div class="match-title">{p1} vs {p2}</div>
            <div class="subtext">⏰ {m['time']}</div>
            <br>

            <div>Model Probability: <b>{model_p}</b></div>
            <div>Edge: <b>{edge}%</b></div>

            <br>
            <div class="{ 'value' if edge > 5 else 'fade' if edge < -5 else '' }">
                {"🔥 VALUE BET" if edge > 5 else "❌ FADE" if edge < -5 else "No edge"}
            </div>
        </div>
        """, unsafe_allow_html=True)
