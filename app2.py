import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="wide")
import base64

def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
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
            background: rgba(0, 0, 0, 0.75);
            z-index: -1;
        }}

        /* Make containers slightly transparent */
        .block-container {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 15px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# CALL THIS
set_bg("car_collage_image.png") 



st.title("🚗 Car Price Predictor (Debug Mode)")

# ------------------ LOAD DATA ------------------
try:
    data = pd.read_csv("Cleaned_car_data.csv")
    st.success("✅ Data Loaded")
    #st.write("Columns:", data.columns)
except Exception as e:
    st.error(f"❌ Data Load Error: {e}")
    st.stop()

# ------------------ LOAD MODEL ------------------
try:
    model = pickle.load(open("LinearRegressionModel.pkl", "rb"))
    st.success("✅ Model Loaded")
except Exception as e:
    st.error(f"❌ Model Load Error: {e}")
    st.stop()

# ------------------ UI HEADER ------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>🚗 Car Price Predictor</h1>
    <p style='text-align: center;'>Enter car details to estimate resale price</p>
    """,
    unsafe_allow_html=True
)

# ------------------ SIDEBAR ------------------
st.sidebar.header("About")
st.sidebar.info(
    "This app predicts car prices using a trained ML model.\n\n"
    "Built with Streamlit."
)

# ------------------ FORM ------------------
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Company", sorted(data['company'].unique()))
    name = st.selectbox("Car Model", sorted(data['name'].unique()))
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

        st.success(f"Estimated Price: ₹ {int(prediction):,}")

        # Optional insight
        st.info(f"Car Age: {2025 - year} years")

    except Exception as e:
        st.error("Prediction failed. Check model compatibility.")
        st.exception(e)

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("Built by Ansh Yadav")
 
#streamlit run app2.py

#python -m pip install streamlit 