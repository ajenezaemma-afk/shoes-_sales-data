# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 10:14:20 2025

@author: Admin
"""

import pickle
import pandas as pd
import numpy as np
import streamlit as st
import os


# Load the trained model
loaded_model = pickle.load(open('shoes_sales_data.sav', 'rb'))

def shoes_price_prediction(brand, color, size):
                            
    # Create DataFrame from input
    new_shoes = pd.DataFrame([{
        'brand': 26,
        'color': 2,
        'size': 10,
        
    }])
    
    # Predict price
    predicted_price = loaded_model.predict(new_shoes)
    
    # Return the prediction
    return predicted_price[0]
# Main Streamlit app
def main():
    st.title("shoes Price Prediction")

    # Input fields for all features
    brand = st.text_input('brand (e.g., 26)')
    color = st.text_input('color (e.g., 2)')
    size = st.text_input('size (inches) (e.g., 10)')
    
    if st.button('Predict shoes Price'):
        try:
        # Convert inputs to numeric types
         brand = int(brand)
         color = int(color)
         size = float(size)
         

        # Call the prediction function (just fix indentation)
         shoes = shoes_price_prediction(
            brand, color, size)
         st.success(f'The predicted price for the shoes is: RWF {shoes:.2f}')
        except ValueError:
            
         st.error("Please enter valid numeric values for all inputs.")
if __name__ == '__main__':

    main()         
