import streamlit as st
from PIL import Image

# ========== HERO SECTION ==========
st.markdown("""
    <div style='text-align: center; padding: 2rem 1rem;'>
        <h1 style='font-size: 3em; color: #FF6B00;'>Win IPL Matches with AI-Backed Precision</h1>
        <p style='font-size: 1.25em;'>GameSage delivers real-time player insights, fan engagement tools, and match-winning predictions — built by IIT Roorkee talent.</p>
        <a href='mailto:contact@gamesage.ai'>
            <button style='margin-top: 1rem; font-size: 1.1em; padding: 0.75em 1.5em; background-color: #FF6B00; color: white; border: none; border-radius: 10px;'>
                Schedule a Demo
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# ========== MATCH SELECTOR ==========
st.subheader("🔍 Select an IPL Match")
match = st.selectbox("Choose a match to view predictions:", [
    "KKR vs RCB - Match 1",
    "RR vs GT - Match 2",
    "SRH vs MI - Match 3",
])

st.markdown("---")

# ========== PREDICTED XI & MATCH-UP SNAPSHOT ==========
st.subheader("📋 Predicted Playing XIs")
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🟣 Kolkata Knight Riders")
    kkr_players = [
        ("Shreyas Iyer", "Batter", 56),
        ("Andre Russell", "All-rounder", 72),
        ("Sunil Narine", "All-rounder", 60),
        ("Mitchell Starc", "Bowler", 48)
    ]
    for player, role, points in kkr_players:
        st.write(f"**{player}** ({role}) — 🔮 {points} pts")

with col2:
    st.markdown("#### 🔴 Royal Challengers Bengaluru")
    rcb_players = [
        ("Virat Kohli", "Batter", 66),
        ("Faf du Plessis", "Batter", 58),
        ("Glenn Maxwell", "All-rounder", 70),
        ("Mohammed Siraj", "Bowler", 52)
    ]
    for player, role, points in rcb_players:
        st.write(f"**{player}** ({role}) — 🔮 {points} pts")

st.markdown("---")

# ========== KEY MATCH-UPS ==========
st.subheader("⚔️ Key Player Match-ups")
st.markdown("""
- **Virat Kohli vs Mitchell Starc**  
  _Projected SR: 132.4 | Avg Dismissal: 2.3 innings_

- **Russell vs Siraj**  
  _Projected SR: 186.0 | Dot Ball %: 42%_

- **Maxwell vs Narine**  
  _Projected SR: 122.1 | Wickets Probability: 38%_
""")

st.markdown("---")

# ========== FOOTER ==========
st.markdown("""
<div style='text-align: center; padding: 1rem;'>
    <p style='font-size: 0.9em;'>Built by GameSage • Powered by AI • Made for Champions</p>
</div>
""", unsafe_allow_html=True)
