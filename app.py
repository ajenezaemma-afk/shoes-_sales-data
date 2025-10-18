import numpy as np
import streamlit as st
import joblib

# Load model and columns
loaded_model = joblib.load("shoes_sales_data.joblib")
model_columns = joblib.load("model_columns.joblib")
import os
import joblib

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "shoes_sales_data.joblib")
columns_path = os.path.join(BASE_DIR, "model_columns.joblib")

loaded_model = joblib.load(model_path)
model_columns = joblib.load(columns_path)
# Streamlit UI
st.title("Shoes Sales Data Prediction")

brand = st.number_input("Brand", value=26)
color = st.number_input("Color", value=4)
size = st.number_input("Size", value=6.5)

if st.button("Predict"):
    # Create a dataframe with the same columns
    import pandas as pd
    input_dict = {"brand": brand, "color": color, "size": size}
    input_df = pd.DataFrame([input_dict])
    
    # Ensure all columns match model
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    
    # Predict
    prediction = loaded_model.predict(input_df)
    st.success(f"Predicted shoe price: {prediction[0]:.2f}")

