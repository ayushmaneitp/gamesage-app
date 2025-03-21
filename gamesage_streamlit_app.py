df = pd.read_excel("IPL_2025_Squads_Player_Team_Role_Only.xlsx")
import streamlit as st

# ========== LANDING BANNER ==========
st.markdown("""
    <div style='text-align: center; padding: 2rem 1rem;'>
        <h1 style='font-size: 3em; color: #FF6B00;'>Where Sports Meets Strategic Intelligence</h1>
        <p style='font-size: 1.25em;'>From pitch to podium — GameSage empowers franchises with data-driven strategy, prediction, and fan connection.</p>
    </div>
""", unsafe_allow_html=True)

# ========== FRANCHISE SELECTOR ==========
st.markdown("---")
st.subheader("🏟️ Select Your Franchise")

franchise = st.selectbox(
    "Choose from your league:",
    [
        "🏏 Kolkata Knight Riders (IPL)",
        "🏏 Royal Challengers Bengaluru (IPL)",
        "⚽ Mumbai City FC (ISL)",
        "🏐 Jaipur Pink Panthers (PKL)"
    ]
)

if franchise:
    st.markdown("---")
    st.header(f"📊 {franchise} Dashboard")

    # ========== A. Squad Overview ==========
    st.subheader("🧾 Current Squad")
    st.markdown("""
    - **Shreyas Iyer** (Batter) — Fit
    - **Andre Russell** (All-rounder) — In Form 🔥
    - **Sunil Narine** (All-rounder) — Fit
    - **Mitchell Starc** (Bowler) — Fit
    """)

    # ========== B. Upcoming Fixtures ==========
    st.subheader("📅 Upcoming Matches")
    st.table({
        "Opponent": ["RCB", "MI", "GT"],
        "Date": ["Mar 22", "Mar 25", "Mar 29"],
        "Venue": ["Eden Gardens", "Wankhede", "Narendra Modi Stadium"]
    })

    # ========== C. Predicted Playing XI ==========
    st.subheader("🧠 Predicted XI (Next Match vs RCB)")
    st.markdown("""
    - **Shreyas Iyer** — Avg: 56 pts — Selected for consistency
    - **Russell** — Avg: 72 pts — Selected for finishing firepower
    - **Narine** — Avg: 60 pts — Effective vs RCB middle order
    - **Starc** — Avg: 48 pts — Match-up vs Kohli
    """)

    st.markdown("> _**Selection Logic:** Based on recent form, historical performance vs opponent, and match conditions._")

    # ========== D. Key Team Stats ==========
    st.subheader("📈 Season Stats Snapshot")
    st.markdown("""
    - **Win Rate:** 66%
    - **Top Performer:** Andre Russell
    - **Avg Fantasy Score (Team):** 812 pts/match
    - **Most Impactful Player:** Sunil Narine (Avg 3 wickets/match)
    """)

    # ========== E. Fan Engagement Tools ==========
    st.subheader("🎉 Fan Engagement Zone")
    st.markdown("""
    - 🗳️ **Fan Poll:** Who should be captain next match?
    - 🎯 Predict the top scorer vs RCB
    - 📊 Fantasy League Integration (Coming soon)
    """)

# ========== FOOTER ==========
st.markdown("""
<div style='text-align: center; padding: 1rem;'>
    <p style='font-size: 0.9em;'>Built by GameSage • Powered by AI • Made for Champions</p>
</div>
""", unsafe_allow_html=True)
