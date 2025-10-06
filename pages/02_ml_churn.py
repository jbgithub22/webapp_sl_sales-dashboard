import streamlit as st
import pandas as pd
import numpy as np
from utils.db_connector import get_data

st.title("⚙️ ML Prediction: Customer Churn Risk")
st.header("Identifying and Retaining High-Value Customers")

st.markdown("""
This model aims to predict the likelihood of a customer churning (i.e., not placing an order 
within the next 12 months). This allows the sales team to launch targeted retention campaigns.
""")

st.markdown("---")

# --- Dummy Model/Data Setup ---
# In a real application, you would load a trained model here:
# model = joblib.load('models/churn_model.pkl')

# Get the list of customers for the selection box
df_customers = get_data("SELECT customerNumber, customerName, creditLimit FROM customers ORDER BY customerName;")
customer_options = {row['customerNumber']: f"{row['customerName']} (ID: {row['customerNumber']})" 
                    for index, row in df_customers.iterrows()}


# --- Prediction Interface ---
st.subheader("Simulate Churn Risk Prediction")

customer_id_selected = st.selectbox(
    "Select a Customer to Analyze:",
    options=list(customer_options.keys()),
    format_func=lambda x: customer_options[x]
)

if customer_id_selected:
    # Fetch the actual credit limit for the selected customer
    customer_info = df_customers[df_customers['customerNumber'] == customer_id_selected].iloc[0]
    credit_limit = customer_info['creditLimit']
    
    # --- DUMMY CHURN LOGIC (Simulating Model Output) ---
    # Low credit limit = higher assumed churn risk (less commitment)
    # High credit limit = lower assumed churn risk (high commitment, easier to retain)
    
    if credit_limit < 50000:
        # High Risk 
        churn_risk_score = np.random.uniform(0.65, 0.95)
        risk_level = "HIGH"
        color = "red"
        action = "Immediate contact by Sales Manager with a personalized discount offer."
    elif credit_limit >= 50000 and credit_limit < 100000:
        # Medium Risk
        churn_risk_score = np.random.uniform(0.35, 0.65)
        risk_level = "MEDIUM"
        color = "orange"
        action = "Send a targeted email campaign showcasing new Classic Car models."
    else:
        # Low Risk
        churn_risk_score = np.random.uniform(0.05, 0.35)
        risk_level = "LOW"
        color = "green"
        action = "Monitor passively and include in standard loyalty communications."
        
    
    st.markdown("---")
    st.subheader(f"Analysis for: {customer_info['customerName']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Current Credit Limit", value=f"${credit_limit:,.2f}")
    
    with col2:
        st.metric(
            label="Predicted Churn Risk Score (0-1)", 
            value=f"{churn_risk_score:.2f}",
            delta=risk_level,
            delta_color=color
        )
        
    st.markdown("#### Recommended Retention Strategy")
    st.markdown(f"**Risk Level:** :point_right: <span style='color:{color}; font-weight:bold;'>{risk_level}</span>", unsafe_allow_html=True)
    st.success(f"**Action:** {action}")
    
    st.markdown("---")
    st.caption(
        f"Disclaimer: This prediction is based on a dummy model using only Credit Limit as a feature. "
        "A true ML model would incorporate Recency, Frequency, Monetary value (RFM), product line loyalty, and other factors."
    )