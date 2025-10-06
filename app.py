import streamlit as st
import pandas as pd
from utils.db_connector import get_data

# --- Page Configuration ---
st.set_page_config(
    page_title="Classic Models Dashboard",
    page_icon="🚗",
    layout="wide"
)

# --- Header and Introduction ---
st.title("🚗 Revving Up Classic Models: A Data-Driven Pit Stop")

st.markdown("""
Welcome to the strategic dashboard for Classic Models, a retailer specializing in exquisite scale models. 
This dashboard is designed to transform raw data from the `classicmodels.sqlite` database into actionable insights, 
guiding our business strategy from simple exploration to advanced machine learning predictions.
""")

st.markdown("---")

# --- The Story: Context Setting ---
st.header("The Strategy Journey: From Insight to Action")

st.markdown(
    """
    Our journey is broken down into two main phases, accessible via the sidebar on the left:

    ### 📊 Phase 1: Exploratory Data Analysis (EDA)
    We begin by understanding our foundation: 
    * **Global Reach:** Where are our customers, and what is their purchasing power?
    * **Inventory Health:** What products are selling, and are we managing stock efficiently?
    * **Financial Pulse:** How do our employees and payment dynamics affect our bottom line?

    ### 🧠 Phase 2: Machine Learning Solutions
    We then tackle critical business challenges with predictive modeling:
    * **Customer Churn:** Identifying at-risk customers for targeted retention.
    * **Product Recommendations:** Suggesting the next best item for customers to boost sales.
    * **Credit Risk:** Quantifying the risk associated with extending credit to maintain financial health.
    """
)

st.markdown("---")

# --- Quick Database Health Check (Optional but helpful) ---
st.header("Database Status Check")

# Query to get basic info (e.g., total customers)
try:
    df_customers_count = get_data("SELECT COUNT(customerNumber) AS total_customers FROM customers;")
    if not df_customers_count.empty:
        st.success(f"Database connection successful! We are tracking **{df_customers_count.iloc[0]['total_customers']}** customers.")
    else:
        st.warning("Database connected, but no customer data found.")
except Exception as e:
    st.error(f"Failed to query database. Ensure 'classicmodels.sqlite' is in the root directory. Error: {e}")

st.markdown(
    """
    **💡 Get Started:** Select **'📊 Exploratory Data Analysis'** from the sidebar to begin your data deep dive!
    """
)