import streamlit as st
import pandas as pd

# ========== LOAD IPL 2025 DATA ==========
@st.cache_data
def load_squad_data():
    return pd.read_excel("IPL_2025_Squads_Player_Team_Role_Only.xlsx")

squad_df = load_squad_data()

# ========== FUNCTION: Generate Valid Predicted XI ==========
def get_valid_predicted_xi(team_df):
    must_haves = {
        "Mumbai Indians": ["Rohit Sharma", "Suryakumar Yadav", "Hardik Pandya", "Ishan Kishan", "Jasprit Bumrah"],
        "Chennai Super Kings": ["Ruturaj Gaikwad", "MS Dhoni", "Ravindra Jadeja", "Rachin Ravindra"],
        "Royal Challengers Bengaluru": ["Virat Kohli", "Faf du Plessis", "Glenn Maxwell", "Mohammed Siraj"],
        "Kolkata Knight Riders": ["Shreyas Iyer", "Andre Russell", "Sunil Narine", "Rinku Singh"],
        "Rajasthan Royals": ["Sanju Samson", "Yashasvi Jaiswal", "Jofra Archer"],
        "Delhi Capitals": ["Rishabh Pant", "Kuldeep Yadav", "Axar Patel", "Mitchell Starc"],
        "Punjab Kings": ["Shikhar Dhawan", "Sam Curran", "Liam Livingstone", "Arshdeep Singh"],
        "Gujarat Titans": ["Shubman Gill", "Rashid Khan", "Mohammed Shami", "Jos Buttler"],
        "Lucknow Super Giants": ["KL Rahul", "Marcus Stoinis", "Nicholas Pooran", "Ravi Bishnoi"],
        "Sunrisers Hyderabad": ["Pat Cummins", "Heinrich Klaasen", "Travis Head", "Abhishek Sharma"]
    }

    # Use the full team DataFrame which includes the "Team" column
    franchise = team_df['Team'].iloc[0]
    must_pick_names = must_haves.get(franchise, [])
    must_pick = team_df[team_df["Player Name"].isin(must_pick_names)]
    
    # Overseas logic
    overseas_keywords = ['Buttler', 'Klaasen', 'Livingstone', 'Russell', 'Narine', 'Head', 'Curran', 
                         'Rabada', 'Conway', 'Ferguson', 'Zampa', 'Topley', 'Coetzee', 'Jansen', 'Archer']
    overseas_pool = team_df[team_df['Player Name'].str.contains('|'.join(overseas_keywords), case=False, na=False)]
    
    # Remove already selected from overseas pool
    overseas_selected = must_pick[must_pick['Player Name'].isin(overseas_pool['Player Name'])]
    overseas_remaining = overseas_pool.drop(index=overseas_selected.index, errors='ignore')
    
    overseas_needed = max(0, 4 - len(overseas_selected))
    overseas_pick = overseas_remaining.sample(min(overseas_needed, len(overseas_remaining)), random_state=1)
    
    # Assemble the final XI
    selected = pd.concat([must_pick, overseas_pick])
    remaining_pool = team_df.drop(index=selected.index, errors='ignore')
    
    if len(selected) < 11:
        fill_count = 11 - len(selected)
        filler = remaining_pool.sample(min(fill_count, len(remaining_pool)), random_state=1)
        selected = pd.concat([selected, filler])
    
    final_xi = selected.drop_duplicates(subset='Player Name').head(11).reset_index(drop=True)
    final_xi.index = final_xi.index + 1  # Set index starting at 1
    return final_xi

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
    team_squad_full = squad_df[squad_df["Team"] == franchise].reset_index(drop=True)
    # Adjust index to start at 1
    team_squad_display = team_squad_full[["Player Name", "Role"]].copy()
    team_squad_display.index = team_squad_display.index + 1
    st.dataframe(team_squad_display, use_container_width=True)
    
    # ===== B. Predicted XI (Rules + Stars) =====
    st.subheader("🧠 Predicted XI for Next Match")
    st.markdown("> Prioritizes key players, respects IPL rules (max 4 overseas, 1+ WK, balanced team).")
    predicted_xi = get_valid_predicted_xi(team_squad_full)
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
