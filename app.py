import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load('random_forest_fraud.pkl')  # Make sure to place your model in the same directory

# Streamlit app UI
st.title("Credit Card Fraud Detection")

# Input fields for user to enter transaction details with unique keys
merchant = st.number_input("Merchant", min_value=1, value=1, step=1, key="merchant")
category = st.number_input("Category", min_value=1, value=1, step=1, key="category")  # Adjust this based on the actual feature range
amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0, step=1.0, key="amount")
age = st.slider("Age", min_value=18, max_value=100, value=30, step=1, key="age")

# Gender (converted to numeric: Male=1, Female=0)
gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
gender = 1 if gender == "Male" else 0

city = st.number_input("City", min_value=1, value=1, step=1, key="city")  # Adjust based on how 'city' is encoded
state = st.number_input("State", min_value=1, value=1, step=1, key="state")  # Adjust based on how 'state' is encoded
latitude = st.number_input("Merchant Latitude", min_value=-90.0, max_value=90.0, value=37.7749, key="latitude")
longitude = st.number_input("Merchant Longitude", min_value=-180.0, max_value=180.0, value=-122.4194, key="longitude")
city_population = st.number_input("City Population", min_value=1000, max_value=10000000, value=500000, step=1000, key="city_population")

# Example job input (numeric encoding of jobs)
job = st.number_input("Job", min_value=1, value=1, step=1, key="job")  # This should be adjusted based on how 'job' is encoded in the model

merch_lat = st.number_input("Merchant Latitude", min_value=-90.0, max_value=90.0, value=37.7749, key="merch_lat")
merch_long = st.number_input("Merchant Longitude", min_value=-180.0, max_value=180.0, value=-122.4194, key="merch_long")

# Prepare input for prediction (ensure the order of features is correct)
user_input = np.array([[merchant, category, amount, gender, city, state, latitude, longitude, city_population, job, merch_lat, merch_long, age]])

# Predict button
if st.button("Predict Fraud"):
    # Make prediction
    prediction = model.predict(user_input)
    
    # Show prediction result
    if prediction[0] == 1:
        st.error("⚠️ Fraud Detected!")
    else:
        st.success("✅ Transaction is Not Fraud")
