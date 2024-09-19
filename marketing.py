import streamlit as st
import pandas as pd
import pickle
from sklearn.impute import SimpleImputer
from sklearn.utils.validation import check_is_fitted
from sklearn.ensemble import RandomForestClassifier

# Load the trained model
model = pickle.load(open('rf_model.pkl', 'rb'))

# Define the features
features = ['Age', 'Annual Income', 'Spending Score', 'Previous Purchases',
            'Campaign Engagement', 'Days Since Last Purchase', 'Gender',
            'Marital Status', 'Children', 'Social Media Interaction',
            'Email Click Rate', 'Online Browsing Time', 'Loyalty Points',
            'Product Reviews', 'Customer Tenure']

# Create the Streamlit app
st.title('Customer Response Prediction')

# Input fields for user to enter feature values
age = st.number_input('Age', min_value=18, max_value=100)
annual_income = st.number_input('Annual Income')
spending_score = st.number_input('Spending Score', min_value=1, max_value=100)
previous_purchases = st.number_input('Previous Purchases')
campaign_engagement = st.number_input('Campaign Engagement')
days_since_last_purchase = st.number_input('Days Since Last Purchase')
gender = st.selectbox('Gender', ['Male', 'Female'])
marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
children = st.number_input('Children')
social_media_interaction = st.number_input('Social Media Interaction')
email_click_rate = st.number_input('Email Click Rate')
online_browsing_time = st.number_input('Online Browsing Time')
loyalty_points = st.number_input('Loyalty Points')
product_reviews = st.number_input('Product Reviews')
customer_tenure = st.number_input('Customer Tenure')

# Create a button to predict
if st.button('Predict'):
    # Create a DataFrame with the user input
    input_data = pd.DataFrame([[age, annual_income, spending_score, previous_purchases,
                               campaign_engagement, days_since_last_purchase, gender,
                               marital_status, children, social_media_interaction,
                               email_click_rate, online_browsing_time, loyalty_points,
                               product_reviews, customer_tenure]], columns=features)

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)[0]

    # Display the prediction
    if prediction == 1:
        st.success('The customer is likely to respond to the campaign.')
    else:
        st.warning('The customer is unlikely to respond to the campaign.')
