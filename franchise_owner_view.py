import streamlit as st
import pandas as pd

st.set_page_config(page_title="GameSage – Franchise Owner Dashboard", layout="wide")

st.title("🏢 GameSage – Franchise Owner Dashboard")

st.markdown("""
This dashboard gives franchise owners a structured breakdown of GameSage's recommended playing XI, including logic behind every player selection.

🔐 *Login access will be enabled in future versions.*
""")

# Simulated structured playing XI breakdown
players = [
    {"Player": "Virat Kohli", "Role": "Top-order Batter", "Base": 40, "Impact Bonus": 13},
    {"Player": "Rajat Patidar", "Role": "Top-order Batter", "Base": 40, "Impact Bonus": 9},
    {"Player": "Rinku Singh", "Role": "Finisher", "Base": 45, "Impact Bonus": 4},
    {"Player": "Andre Russell", "Role": "All-rounder (Finisher + Death Bowler)", "Base": 55, "Impact Bonus": 2},
    {"Player": "Sunil Narine", "Role": "All-rounder (Opener + Powerplay Bowler)", "Base": 60, "Impact Bonus": -1},
    {"Player": "Liam Livingstone", "Role": "All-rounder (Middle-order + Spin Hitter)", "Base": 50, "Impact Bonus": -1},
    {"Player": "Krunal Pandya", "Role": "All-rounder (Spin Bowler)", "Base": 42, "Impact Bonus": 2},
    {"Player": "Rahmanullah Gurbaz", "Role": "Wicketkeeper (Opener)", "Base": 48, "Impact Bonus": -4},
    {"Player": "Varun Chakaravarthy", "Role": "Mystery Spinner (Middle Overs)", "Base": 44, "Impact Bonus": 2},
    {"Player": "Harshit Rana", "Role": "Pace Bowler (Death Overs)", "Base": 46, "Impact Bonus": 0},
    {"Player": "Yash Dayal", "Role": "Pace Bowler (Powerplay + Middle Overs)", "Base": 40, "Impact Bonus": 3}
]

for p in players:
    p["Predicted Points"] = p["Base"] + p["Impact Bonus"]

logic_df = pd.DataFrame(players).sort_values(by="Predicted Points", ascending=False).reset_index(drop=True)
logic_df.index += 1
logic_df.index.name = "Rank"

st.subheader("📋 GameSage Recommended Playing XI with Logic")
st.dataframe(logic_df.style.format({
    "Base": "{:.0f}",
    "Impact Bonus": "{:+.0f}",
    "Predicted Points": "{:.0f}"
}), use_container_width=True)

st.markdown("""
---
### 📌 Logic Structure:
- **Base**: Role-weighted value assigned by GameSage engine
- **Impact Bonus**: Match-specific adjustment based on pitch, weather, opposition
- **Total Predicted Points** = Base + Bonus

Coming Soon:
- Schedule-aware rotation logic
- Franchise squad performance tracking
- Opponent matchup insights
""")
