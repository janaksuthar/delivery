# prompt: with dump file rf_classifier_model.pkl make app.py useful for streamlit and download as app.py

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
loaded_model = joblib.load('rf_classifier_model.pkl')

# Create the Streamlit app
st.title("Manufacturing Defect Prediction")

# Input features
production_volume = st.number_input("Production Volume", min_value=0)
production_cost = st.number_input("Production Cost", min_value=0)
supplier_quality = st.number_input("Supplier Quality", min_value=0)
delivery_delay = st.number_input("Delivery Delay", min_value=0)
defect_rate = st.number_input("Defect Rate", min_value=0.0)
quality_score = st.number_input("Quality Score", min_value=0.0)
maintenance_hours = st.number_input("Maintenance Hours", min_value=0.0)
downtime_percentage = st.number_input("Downtime Percentage", min_value=0.0)
inventory_turnover = st.number_input("Inventory Turnover", min_value=0)
stockout_rate = st.number_input("Stockout Rate", min_value=0)
worker_productivity = st.number_input("Worker Productivity", min_value=0.0)
safety_incidents = st.number_input("Safety Incidents", min_value=0.0)
energy_consumption = st.number_input("Energy Consumption", min_value=0)
energy_efficiency = st.number_input("Energy Efficiency", min_value=0)
additive_process_time = st.number_input("Additive Process Time", min_value=0)
additive_material_cost = st.number_input("Additive Material Cost", min_value=0)


# Create a DataFrame for prediction
new_data = pd.DataFrame({
    'ProductionVolume': [production_volume],
    'ProductionCost': [production_cost],
    'SupplierQuality': [supplier_quality],
    'DeliveryDelay': [delivery_delay],
    'DefectRate': [defect_rate],
    'QualityScore': [quality_score],
    'MaintenanceHours': [maintenance_hours],
    'DowntimePercentage': [downtime_percentage],
    'InventoryTurnover': [inventory_turnover],
    'StockoutRate': [stockout_rate],
    'WorkerProductivity': [worker_productivity],
    'SafetyIncidents': [safety_incidents],
    'EnergyConsumption': [energy_consumption],
    'EnergyEfficiency': [energy_efficiency],
    'AdditiveProcessTime': [additive_process_time],
    'AdditiveMaterialCost': [additive_material_cost]
})

# Make predictions
if st.button("Predict Defect Status"):
    prediction = loaded_model.predict(new_data)
    st.write(f"Predicted Defect Status: {prediction[0]}")