import streamlit as st
import pandas as pd
import pickle
import base64

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="wide")

# ------------------ BACKGROUND ------------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Dark overlay for readability */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.80);
        z-index: -1;
    }}

    /* Main container */
    .block-container {{
        background-color: rgba(0, 0, 0, 0.65);
        padding: 2rem;
        border-radius: 15px;
        color: white;
    }}

    /* Inputs */
    .stSelectbox, .stNumberInput, .stSlider {{
        color: white;
    }}

    /* Button */
    .stButton > button {{
        background: linear-gradient(90deg, #00F5A0, #00D9F5);
        color: black;
        border-radius: 10px;
        font-weight: bold;
        padding: 10px 20px;
    }}

    </style>
    """, unsafe_allow_html=True)

# APPLY BACKGROUND
set_bg("car_collage_image.png")

# ------------------ TITLE ------------------
st.markdown("""
<h1 style='
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    background: linear-gradient(90deg, #00F5A0, #00D9F5, #7F00FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
'>
🚗 Car Price Predictor
</h1>
<p style='text-align:center; color:white; font-size:18px;'>
Enter car details to estimate resale price
</p>
""", unsafe_allow_html=True)

# ------------------ LOAD DATA ------------------
try:
    data = pd.read_csv("processed_data.csv")
except Exception as e:
    st.error(f"❌ Data Load Error: {e}")
    st.stop()

# ------------------ LOAD MODEL ------------------
try:
    model = pickle.load(open("model.pkl", "rb"))
except Exception as e:
    st.error(f"❌ Model Load Error: {e}")
    st.stop()

# ------------------ SIDEBAR ------------------
st.sidebar.header("About")
st.sidebar.info(
    "This app predicts car prices using a trained ML model.\n\nBuilt with Streamlit.\n\n By Ansh Yadav"
)

# ------------------ FORM ------------------
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Company", sorted(data['company'].unique()))

    # ✅ Dependent dropdown (important fix)
    filtered_models = data[data['company'] == company]['name'].unique()
    name = st.selectbox("Car Model", sorted(filtered_models))

    year = st.slider("Year", int(data['year'].min()), int(data['year'].max()), 2015)

with col2:
    kms_driven = st.number_input("Kilometers Driven", min_value=0, step=1000)
    fuel_type = st.selectbox("Fuel Type", data['fuel_type'].unique())

# ------------------ PREDICTION ------------------
if st.button("💰 Predict Price"):
    input_df = pd.DataFrame({
        'name': [name],
        'company': [company],
        'fuel_type': [fuel_type],
        'year': [year],
        'kms_driven': [kms_driven]
    })

    try:
        prediction = model.predict(input_df)[0]

        st.markdown(f"""
                    <div style="
                    background: linear-gradient(90deg, #00F5A0, #00D9F5);
                    padding: 20px;
                    border-radius: 15px;
                    text-align: center;
                    font-size: 26px;
                    font-weight: bold;
                    color: black;
                    box-shadow: 0 0 25px rgba(0,255,200,0.8);
                    margin-top: 20px;
                    ">
                💰 Estimated Price: ₹ {int(prediction):,}
                </div>
                """, unsafe_allow_html=True)
        st.markdown(f"""
                    <div style="
                    background: linear-gradient(90deg, #FFD700, #FFA500);
                    padding: 15px;
                    border-radius: 12px;
                    text-align: center;
                    font-size: 20px;
                    font-weight: bold;
                    color: black;
                    box-shadow: 0 0 20px rgba(255,215,0,0.8);
                    margin-top: 10px;
                    ">
                📅 Car Age: {2025 - year} years
                </div>
                """, unsafe_allow_html=True)

    except Exception as e:
        st.error("Prediction failed. Check model compatibility.")
        st.exception(e)

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("<p style='text-align:center; color:white;'>Built by Ansh Yadav 🚀</p>", unsafe_allow_html=True) 


#streamlit run app.py