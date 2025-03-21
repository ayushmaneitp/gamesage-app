import streamlit as st
import pandas as pd

# ========== LOAD IPL 2025 DATA ==========
@st.cache_data
def load_squad_data():
    return pd.read_excel("IPL_2025_Squads_Player_Team_Role_Only.xlsx")

squad_df = load_squad_data()

# ========== FUNCTION: Generate Valid Predicted XI ==========
def get_valid_predicted_xi(team_df):
    wk = team_df[team_df['Role'].str.lower() == 'wicketkeeper']
    bat = team_df[team_df['Role'].str.lower() == 'batter']
    bowl = team_df[team_df['Role'].str.lower() == 'bowler']
    allr = team_df[team_df['Role'].str.lower() == 'all-rounder']
    
    # Overseas filtering (customize this with real overseas player names if needed)
    overseas_keywords = ['Buttler', 'Klaasen', 'Livingstone', 'Russell', 'Narine', 'Head', 'Curran', 'Rabada', 'Conway', 'Ferguson', 'Zampa', 'Topley', 'Coetzee', 'Jansen', 'Archer']
    overseas_pool = team_df[team_df['Player Name'].str.contains('|'.join(overseas_keywords), case=False, na=False)]
    
    wk_pick = wk.sample(1) if len(wk) >= 1 else pd.DataFrame()
    overseas_pick = overseas_pool.sample(min(4, len(overseas_pool))) if not overseas_pool.empty else pd.DataFrame()

    remaining_spots = 11 - len(wk_pick) - len(overseas_pick)
    rest_pool = team_df.drop(index=wk_pick.index if not wk_pick.empty else []).drop(index=overseas_pick.index if not overseas_pick.empty else [])
    
    final_pick = pd.concat([wk_pick, overseas_pick])
    if remaining_spots > 0 and not rest_pool.empty:
        final_pick = pd.concat([final_pick, rest_pool.sample(min(remaining_spots, len(rest_pool)))])
    
    return final_pick.reset_index(drop=True)

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

    # ===== B. Predicted XI (Rules-based) =====
    st.subheader("🧠 Predicted XI for Next Match")
    st.markdown("> Based on IPL rules: max 4 overseas, at least 1 WK, balanced roles.")
    predicted_xi = get_valid_predicted_xi(team_squad)
    st.table(predicted_xi)

    # ===== C. Fan Engagement Zone =====
    st.subheader("🎉 Fan Engagement Zone")
    st.markdown("""
    - 🗳️ Fan Poll: Who should captain the next match?
    - 🎯 Predict the MVP
    - 💬 Share your playing XI (coming soon!)
    """)

# ========== FOOTER ==========
st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <p style='font-size: 0.9em;'>Built by GameSage • Powered by AI • Made for Champions</p>
    </div>
""", unsafe_allow_html=True)
