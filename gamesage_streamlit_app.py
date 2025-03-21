import streamlit as st
import pandas as pd
import plotly.express as px

# Set red and black theme using custom CSS
st.markdown("""
    <style>
    body {
        background-color: #0d0d0d;
        color: white;
    }
    .stApp {
        background-color: #0d0d0d;
    }
    h1, h2, h3 {
        color: #e50914;
    }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("GameSage ⚡ | IPL Fantasy AI Engine")
st.markdown("## Predict. Compare. Dominate.")
st.markdown("GameSage uses AI to predict fantasy points and compare them to actual results from IPL 2023–24.")

# GitHub raw URL of your CSV
csv_url = "https://raw.githubusercontent.com/itsyoko/gamesage-app/refs/heads/main/GameSage_Prediction_vs_Actual_Comparison%20(1).csv"

# Load comparison data from GitHub
@st.cache_data
def load_data():
    return pd.read_csv(csv_url)

df = load_data()

# Match Selector
match_ids = sorted(df["Match ID"].unique())
selected_match = st.selectbox("Select a Match ID", match_ids)
match_df = df[df["Match ID"] == selected_match]

# Display table
st.subheader("📊 Predicted vs Actual Fantasy Points")
st.dataframe(match_df[['Player', 'Total Fantasy Points', 'Predicted Fantasy Points', 'Absolute Error', 'Prediction Quality']], use_container_width=True)

# Plotting comparison
fig = px.bar(
    match_df.sort_values("Total Fantasy Points", ascending=False),
    x="Player",
    y=["Total Fantasy Points", "Predicted Fantasy Points"],
    barmode="group",
    title="Prediction vs Actual for Each Player",
    labels={"value": "Fantasy Points", "variable": "Type"},
    color_discrete_map={
        "Total Fantasy Points": "#e50914",
        "Predicted Fantasy Points": "#ffffff"
    }
)
st.plotly_chart(fig, use_container_width=True)

# Fantasy Leaderboard
st.subheader("🏆 Fantasy Points Leaderboard")
leaderboard_df = match_df.sort_values("Total Fantasy Points", ascending=False).reset_index(drop=True)
st.table(leaderboard_df[['Player', 'Total Fantasy Points']].head(10))

# Captain/Vice-Captain Suggestion
st.subheader("🧠 Suggested Captain & Vice-Captain")
captain = leaderboard_df.iloc[0]['Player'] if not leaderboard_df.empty else "N/A"
vice_captain = leaderboard_df.iloc[1]['Player'] if len(leaderboard_df) > 1 else "N/A"
st.markdown(f"**Captain:** 🔴 {captain}")
st.markdown(f"**Vice-Captain:** ⚪ {vice_captain}")

# Predicted XI (based on top 11 fantasy scorers)
st.subheader("🧾 Predicted XI")
predicted_xi = leaderboard_df[['Player', 'Total Fantasy Points']].head(11)
st.dataframe(predicted_xi.rename(columns={'Player': 'Name', 'Total Fantasy Points': 'Predicted Fantasy Points'}), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by GameSage")
