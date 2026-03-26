import streamlit as st

def render_live_scores(events):

    if not events:
        st.info("No live ATP matches")
        return

    for e in events:
        st.markdown(f"""
        <div class="card">
            <b>{e['p1']}</b> vs <b>{e['p2']}</b><br>
            <span class="subtext">{e['status']}</span>
        </div>
        """, unsafe_allow_html=True)
