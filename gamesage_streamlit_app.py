import streamlit as st
import pandas as pd

# ========== LOAD IPL 2025 DATA ==========
@st.cache_data
def load_squad_data():
    return pd.read_excel("IPL_2025_Squads_Player_Team_Role_Only.xlsx")

squad_df = load_squad_data()

# ========== HERO SECTION ==========
st.markdown("""
    <div style='text-align: center; padding: 2rem 1rem;'>
        <h1 style='font-size: 3em; color: #FF6B00;'>Where Sports Meets Strategic Intelligence</h1>
        <p style='font-size: 1.25em;'>From pitch to podium — GameSage empowers franchises with data-driven strategy, prediction, and fan connection.</p>
    </div>
""", unsafe_allow_html=True)

# ========== FRANCHISE SELECTOR ==========
st.markdown("---")
st.subheader("🏟️ Select Your Franchise")

franchise = st.selectbox("Choose from IPL 2025 teams:", sorted(squad_df["Team"].unique()))

if franchise:
    st.markdown("---")
    st.header(f"📊 {franchise} Owner Dashboard")

    # ===== A. Squad Overview =====
    st.subheader("🧾 Current Squad")
    team_squad = squad_df[squad_df["Team"] == franchise][["Player Name", "Role"]].reset_index(drop=True)
    st.dataframe(team_squad, use_container_width=True)

    # ===== B. Predicted XI (Placeholder for now) =====
    st.subheader("🧠 Predicted XI for Next Match")
    st.markdown("> _Powered soon by GameSage’s AI — based on form, match-ups, and more._")
    predicted_xi = team_squad.sample(11, random_state=42)  # deterministic for demo
    st.table(predicted_xi)

    # ===== C. Fan Engagement Zone =====
    st.subheader("🎉 Fan Engagement Zone")
    st.markdown("""
    - 🗳️ Fan Poll: Who should captain the next match?
    - 🎯 Predict the MVP
    - 💬 Share your playing XI (feature coming soon)
    """)

# ========== FOOTER ==========
st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <p style='font-size: 0.9em;'>Built by GameSage • Powered by AI • Made for Champions</p>
    </div>
""", unsafe_allow_html=True)
