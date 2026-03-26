import streamlit as st

def render_live_scores(events):

    if not events:
        st.info("No live matches")
        return

    for e in events:
        st.write(f"{e['p1']} vs {e['p2']} — {e['status']}")
