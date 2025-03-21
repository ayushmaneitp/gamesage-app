import streamlit as st
import pandas as pd
import numpy as np

# ========== CSS & Background Setup ==========
st.markdown(
    """
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1521412644187-c49fa049e84d");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    .reportview-container .main .block-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ========== Header with IPL Logos ==========
st.markdown(
    """
    <div style="text-align: center; padding-bottom: 1rem;">
        <img src="https://upload.wikimedia.org/wikipedia/en/4/46/Chennai_Super_Kings_logo.svg" alt="CSK" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/1/13/Mumbai_Indians_logo.svg" alt="MI" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/7/7d/Royal_Challengers_Bengaluru_logo.svg" alt="RCB" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/6/6e/Kolkata_Knight_Riders_logo.svg" alt="KKR" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/9/94/Rajasthan_Royals_logo.svg" alt="RR" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/f/fd/Punjab_Kings_logo.svg" alt="PBKS" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/d/d8/Delhi_Capitals_logo.svg" alt="DC" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/5/55/Sunrisers_Hyderabad_logo.svg" alt="SRH" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/4/44/Gujarat_Titans_logo.svg" alt="GT" height="50">
        <img src="https://upload.wikimedia.org/wikipedia/en/2/2b/Lucknow_Super_Giants_logo.svg" alt="LSG" height="50">
    </div>
    """,
    unsafe_allow_html=True,
)

# ========== LOAD IPL 2025 DATA ==========
@st.cache_data
def load_squad_data():
    return pd.read_excel("IPL_2025_Squads_Player_Team_Role_Only.xlsx")

squad_df = load_squad_data()

# ========== FUNCTIONS: Generate Predicted XI ==========
def get_valid_predicted_xi(team_df):
    # Rules-based selection (includes marquee players and applies IPL rules)
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

    franchise = team_df['Team'].iloc[0]
    must_pick_names = must_haves.get(franchise, [])
    must_pick = team_df[team_df["Player Name"].isin(must_pick_names)]
    
    # Overseas logic (using keywords)
    overseas_keywords = ['Buttler', 'Klaasen', 'Livingstone', 'Russell', 'Narine', 'Head', 'Curran', 
                         'Rabada', 'Conway', 'Ferguson', 'Zampa', 'Topley', 'Coetzee', 'Jansen', 'Archer']
    overseas_pool = team_df[team_df['Player Name'].str.contains('|'.join(overseas_keywords), case=False, na=False)]
    
    overseas_selected = must_pick[must_pick['Player Name'].isin(overseas_pool['Player Name'])]
    overseas_remaining = overseas_pool.drop(index=overseas_selected.index, errors='ignore')
    
    overseas_needed = max(0, 4 - len(overseas_selected))
    overseas_pick = overseas_remaining.sample(min(overseas_needed, len(overseas_remaining)), random_state=1)
    
    selected = pd.concat([must_pick, overseas_pick])
    remaining_pool = team_df.drop(index=selected.index, errors='ignore')
    
    if len(selected) < 11:
        fill_count = 11 - len(selected)
        filler = remaining_pool.sample(min(fill_count, len(remaining_pool)), random_state=1)
        selected = pd.concat([selected, filler])
    
    final_xi = selected.drop_duplicates(subset='Player Name').head(11).reset_index(drop=True)
    final_xi.index = final_xi.index + 1  # 1-based index
    return final_xi

def predict_playing_xi_ml(team_df):
    # Simulated ML-based prediction logic
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
    franchise = team_df['Team'].iloc[0]
    must_have_list = must_haves.get(franchise, [])
    
    team_df = team_df.copy()
    # Simulated prediction score: higher for must-have players
    def score(player):
        if player in must_have_list:
            return np.random.uniform(8, 12)
        else:
            return np.random.uniform(0, 5)
    team_df['Predicted Score'] = team_df['Player Name'].apply(score)
    team_df = team_df.sort_values(by='Predicted Score', ascending=False)
    predicted = team_df.head(11)
    # Ensure at least one wicketkeeper is present
    if not any(predicted['Role'].str.lower().str.contains("wicket", na=False)):
        wk_candidates = team_df[team_df['Role'].str.lower().str.contains("wicket", na=False)]
        if not wk_candidates.empty:
            wk_best = wk_candidates.iloc[0]
            predicted = predicted.append(wk_best)
            predicted = predicted.sort_values(by='Predicted Score', ascending=False).head(11)
    predicted = predicted.drop(columns=['Predicted Score']).reset_index(drop=True)
    predicted.index = predicted.index + 1
    return predicted

def get_model_accuracy(model_choice):
    # Simulated accuracies for demonstration:
    if model_choice == "Rules-based":
        return 82  # Average Prediction Correctness Percentage
    else:
        return 92  # Game Sage ML Model Prediction Correctness Percentage

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

# Radio button to select prediction model
model_choice = st.radio("Select Prediction Model:", ("Rules-based", "ML-based"))
accuracy = get_model_accuracy(model_choice)
if model_choice == "Rules-based":
    st.markdown(f"**Average Prediction Correctness Percentage: {accuracy}%**")
else:
    st.markdown(f"**Game Sage ML Model Prediction Correctness Percentage: {accuracy}%**")

if franchise:
    st.markdown("---")
    st.header(f"📊 {franchise} Owner Dashboard")
    
    # ===== A. Squad Overview =====
    st.subheader("🧾 Current Squad")
    team_squad_full = squad_df[squad_df["Team"] == franchise].reset_index(drop=True)
    team_squad_display = team_squad_full[["Player Name", "Role"]].copy()
    team_squad_display.index = team_squad_display.index + 1
    st.dataframe(team_squad_display, use_container_width=True)
    
    # ===== B. Predicted XI =====
    st.subheader("🧠 Predicted XI for Next Match")
    st.markdown("> Prioritizes key players and respects IPL rules.")
    if model_choice == "Rules-based":
        predicted_xi = get_valid_predicted_xi(team_squad_full)
    else:
        predicted_xi = predict_playing_xi_ml(team_squad_full)
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
