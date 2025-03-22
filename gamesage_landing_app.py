import streamlit as st
import pandas as pd

st.set_page_config(page_title="GameSage Portal", layout="centered")

st.title("🏏 Welcome to GameSage")
st.subheader("Your AI-powered sports intelligence hub")

st.markdown("---")

# Role selection
role = st.radio("Who are you?", ["Fan", "Franchise Owner"], horizontal=True)

st.markdown("---")

if role == "Fan":
    st.header("🎯 Fan Dashboard Preview")
    st.markdown("""
    - View GameSage-predicted Fantasy XI for each match
    - Get player-wise predicted points and captain/VC picks
    - Compare your team with crowd averages
    - Account for pitch, weather, and match-day playing XI
    - Swap players and simulate outcomes

    🔐 *Login access will be required in future versions.*
    """)
    if st.button("Go to Fan Dashboard"):
        st.switch_page("fan_view.py")

elif role == "Franchise Owner":
    st.header("🏢 Franchise Owner Dashboard Preview")
    st.markdown("""
    - Select your franchise to view full IPL 2025 squad
    - See GameSage's recommended Playing XI
    - Understand player selection logic with structured insights
    - Track match-by-match readiness and team building

    🔐 *Access-controlled login coming soon.*
    """)
    if st.button("Go to Franchise Dashboard"):
        st.switch_page("franchise_owner_view.py")

st.markdown("---")
st.caption("GameSage is designed for both fantasy fans and franchise professionals. AI insights. Real impact.")
