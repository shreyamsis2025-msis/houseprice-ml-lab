import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load(r"C:\Users\Administrator\Documents\GitHub\msis\houseprice-ml-lab\model.pkl")

option =['Jayanagar', 'Koramangala', 'Indiranagar', 'HSR Layout', 'Whitefield', 'Electronic City', 'Missing']
with st.form("predict"):
    rent = st.number_input("Monthly Rent", value=15000)
    area = st.number_input("Square Feet", value=1000)
    locality = st.selectbox("Locality",option)
    BHK = st.number_input("BHK", value=2, min_value=0, max_value=10, step=1)
    bathrooms = st.number_input("bathrooms", value=2, min_value=0, max_value=10, step=1)
    parking = st.selectbox("Parking (Bike,Car)", ['Bike','Car','Bike and Car'])
    facing = st.text_input("facing (east/west/north/south)", "east")
    submitted = st.form_submit_button("Predict")


if submitted:
    X = pd.DataFrame([{
        "rent": rent,
        "area": area,
        "locality": locality if locality else "Missing",
        "BHK": BHK,
        "bathrooms": bathrooms,
        "parking": parking if parking else "Missing",
        "facing": facing if facing else "Missing"
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")

# import streamlit as st
# import joblib
# import pandas as pd

# # --- Page config ---
# st.set_page_config(
#     page_title="🏠 House Price Predictor",
#     page_icon="🏡",
#     layout="centered"
# )

# # --- Custom CSS for styling ---
# st.markdown("""
#     <style>
#         .main {
#             background-color: #f8f9fa;
#         }
#         .stButton>button {
#             background-color: #4CAF50;
#             color: white;
#             border-radius: 12px;
#             height: 50px;
#             font-size: 18px;
#             font-weight: bold;
#         }
#         .stButton>button:hover {
#             background-color: #45a049;
#         }
#         .result-box {
#             padding: 20px;
#             border-radius: 15px;
#             background: #e9f7ef;
#             text-align: center;
#             font-size: 22px;
#             font-weight: bold;
#             color: #155724;
#             border: 2px solid #c3e6cb;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # --- Title ---
# st.title("🏡 Bangalore House Price Predictor")

# st.markdown("### Enter house details below to estimate the property price.")

# # --- Load Model ---
# model = joblib.load(r"C:\Users\Administrator\Documents\GitHub\msis\houseprice-ml-lab\model.pkl")

# # --- Input Form ---
# option = ['Jayanagar', 'Koramangala', 'Indiranagar', 'HSR Layout', 'Whitefield', 'Electronic City', 'Missing']

# with st.form("predict", clear_on_submit=False):
#     col1, col2 = st.columns(2)

#     with col1:
#         rent = st.number_input("💰 Monthly Rent", value=15000, step=500)
#         area = st.number_input("📐 Square Feet", value=1000, step=50)
#         locality = st.selectbox("📍 Locality", option)

#     with col2:
#         BHK = st.number_input("🛏️ BHK", value=2, min_value=0, max_value=10, step=1)
#         bathrooms = st.number_input("🚿 Bathrooms", value=2, min_value=0, max_value=10, step=1)
#         parking = st.selectbox("🚗 Parking", ['Bike','Car','Bike and Car'])
#         facing = st.selectbox("🧭 Facing", ["East", "West", "North", "South", "Missing"])

#     submitted = st.form_submit_button("🔮 Predict Price")

# # --- Prediction ---
# if submitted:
#     X = pd.DataFrame([{
#         "rent": rent,
#         "area": area,
#         "locality": locality if locality else "Missing",
#         "BHK": BHK,
#         "bathrooms": bathrooms,
#         "parking": parking if parking else "Missing",
#         "facing": facing if facing else "Missing"
#     }])

#     pred = model.predict(X)[0]

#     st.markdown(
#         f"<div class='result-box'>🏠 Predicted Price: ₹ {pred:,.2f}</div>",
#         unsafe_allow_html=True
#     )
