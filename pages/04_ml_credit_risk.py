import streamlit as st
import pandas as pd
import numpy as np
from utils.db_connector import get_data

st.title("💰 ML Prediction: Credit Risk Assessment")
st.header("Quantifying Financial Exposure for Credit Decisions")

st.markdown("""
This tool simulates a model used by the Finance department to assess the risk of offering credit 
to a new customer or increasing the limit for an existing one. It helps maintain a healthy accounts receivable balance.
""")

st.markdown("---")

# --- Data for Simulation Setup ---
# Get all unique countries from the customers table
df_countries = get_data("SELECT DISTINCT country FROM customers ORDER BY country;")
country_list = df_countries['country'].tolist()

# Define hardcoded risk factors for simulation (in a real app, this would be model output)
RISK_FACTORS = {
    'USA': 0.05,
    'France': 0.10,
    'Spain': 0.10,
    'UK': 0.15,
    'Italy': 0.20,
    'Germany': 0.25,
    # Assign a higher base risk to small/new markets
    'Japan': 0.40, 
    'Australia': 0.30
}

# --- Prediction Interface: User Input Form ---
st.subheader("Simulate New Credit Request")

with st.form("credit_risk_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        customer_country = st.selectbox(
            "Customer Country (Proxy for Economic Stability):",
            options=country_list,
            index=country_list.index('USA') if 'USA' in country_list else 0
        )
        
        annual_revenue = st.number_input(
            "Customer Annual Revenue ($):",
            min_value=10000,
            value=150000,
            step=10000,
            help="Higher revenue suggests greater financial capacity."
        )

    with col2:
        requested_credit_limit = st.number_input(
            "Requested Credit Limit ($):",
            min_value=1000,
            value=75000,
            step=5000,
            help="The amount of credit the customer is requesting."
        )
        
        payment_history = st.selectbox(
            "Historical Payment Record:",
            options=['Excellent (Always on time)', 'Good (Rare late payment)', 'Poor (Frequent delays)'],
            index=0
        )
        
    submitted = st.form_submit_button("Assess Risk")

# --- Risk Assessment Logic ---
if submitted:
    
    # 1. Base Risk (from country)
    base_risk = RISK_FACTORS.get(customer_country, 0.50) # Default high risk for unknown country
    
    # 2. Limit and Revenue Adjustment
    # High limit relative to revenue increases risk
    limit_to_revenue_ratio = requested_credit_limit / annual_revenue
    limit_risk_factor = min(0.4, limit_to_revenue_ratio * 0.5) # Cap at 40% influence

    # 3. Payment History Adjustment
    if payment_history == 'Excellent (Always on time)':
        history_adjustment = -0.10
    elif payment_history == 'Poor (Frequent delays)':
        history_adjustment = 0.20
    else:
        history_adjustment = 0.00
        
    # 4. Final Predicted Risk Score (Simulated)
    raw_risk_score = base_risk + limit_risk_factor + history_adjustment
    # Bound the score between 0.05 and 0.95 and add noise for realism
    final_risk_score = np.clip(raw_risk_score, 0.05, 0.95) + np.random.uniform(-0.05, 0.05)
    final_risk_score = np.clip(final_risk_score, 0.0, 1.0)
    
    # --- Output and Recommendation ---
    st.markdown("---")
    st.subheader("Credit Risk Decision")
    
    if final_risk_score < 0.30:
        decision = "LOW Risk"
        advice = "Recommended. Approve the requested limit, or slightly higher."
        color = "green"
    elif final_risk_score < 0.60:
        decision = "MODERATE Risk"
        advice = f"Proceed with caution. Approve a reduced limit of **${requested_credit_limit * 0.75:,.2f}** and monitor payments closely."
        color = "orange"
    else:
        decision = "HIGH Risk"
        advice = "Not Recommended. Reject the request or approve only a minimal limit with strict pre-payment terms."
        color = "red"
        
    
    st.metric(
        label="Predicted Default Risk Score (0=Low, 1=High)",
        value=f"{final_risk_score:.2f}",
        delta=decision,
        delta_color=color
    )
    
    st.markdown("#### Finance Department Recommendation")
    st.markdown(f"**Risk Profile:** :point_right: <span style='color:{color}; font-weight:bold;'>{decision}</span>", unsafe_allow_html=True)
    st.success(f"**Suggested Action:** {advice}")

st.markdown("---")
st.caption(
    "Disclaimer: This risk assessment is based on a simulated model using simplified proxies. "
    "A production system would use features like accounts payable turnover, historical delinquencies, and third-party credit scores."
)