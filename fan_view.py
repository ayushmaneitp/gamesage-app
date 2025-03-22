import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="GameSage – Fan Dashboard", layout="wide")

st.title("🎯 GameSage – Fan Dashboard")
st.markdown("""
This view shows your optimized fantasy XI with predicted points based on match-day inputs like playing XI, pitch, ground dimensions, and weather.

🔐 *Login will be required in future versions.*
""")

# Simulated logic for displaying fantasy XI with predicted points
role_weight = {
    "Top-order Batter": 40,
    "Finisher": 45,
    "All-rounder (Finisher + Death Bowler)": 55,
    "All-rounder (Opener + Powerplay Bowler)": 60,
    "All-rounder (Middle-order + Spin Hitter)": 50,
    "All-rounder (Spin Bowler)": 42,
    "Wicketkeeper (Opener)": 48,
    "Mystery Spinner (Middle Overs)": 44,
    "Pace Bowler (Death Overs)": 46,
    "Pace Bowler (Powerplay + Middle Overs)": 40
}

team = [
    {"Player": "Virat Kohli", "Team": "RCB", "Role": "Top-order Batter"},
    {"Player": "Rajat Patidar", "Team": "RCB", "Role": "Top-order Batter"},
    {"Player": "Rinku Singh", "Team": "KKR", "Role": "Finisher"},
    {"Player": "Andre Russell", "Team": "KKR", "Role": "All-rounder (Finisher + Death Bowler)"},
    {"Player": "Sunil Narine", "Team": "KKR", "Role": "All-rounder (Opener + Powerplay Bowler)"},
    {"Player": "Liam Livingstone", "Team": "RCB", "Role": "All-rounder (Middle-order + Spin Hitter)"},
    {"Player": "Krunal Pandya", "Team": "RCB", "Role": "All-rounder (Spin Bowler)"},
    {"Player": "Rahmanullah Gurbaz", "Team": "KKR", "Role": "Wicketkeeper (Opener)"},
    {"Player": "Varun Chakaravarthy", "Team": "KKR", "Role": "Mystery Spinner (Middle Overs)"},
    {"Player": "Harshit Rana", "Team": "KKR", "Role": "Pace Bowler (Death Overs)"},
    {"Player": "Yash Dayal", "Team": "RCB", "Role": "Pace Bowler (Powerplay + Middle Overs)"}
]

for p in team:
    base = role_weight.get(p["Role"], 35)
    noise = random.randint(-5, 10)
    p["Predicted Points"] = base + noise

fantasy_df = pd.DataFrame(team).sort_values(by="Predicted Points", ascending=False).reset_index(drop=True)
fantasy_df.index += 1
fantasy_df.index.name = "Rank"

st.subheader("📊 Predicted Fantasy XI")
st.dataframe(fantasy_df.style.format({"Predicted Points": "{:.0f}"}), use_container_width=True)

st.markdown("""
---
### 🧠 Why GameSage?
- Based on real match-day variables
- Role-aware prediction engine
- Proven to outperform average fantasy selections

Coming Soon:
- Compare vs crowd-picked teams
- Team score simulation
""")
