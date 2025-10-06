import streamlit as st
import pandas as pd
from utils.db_connector import get_data

st.title("🛒 ML Prediction: Next Product Recommendation")
st.header("Boosting Cross-Selling and Customer Engagement")

st.markdown("""
This simulated recommendation system suggests the next most likely product line a customer will purchase, 
based on their historical buying patterns and product popularity.
""")

st.markdown("---")

# --- Data Loading and Preprocessing for Simulation ---
# 1. Get all customers
df_customers = get_data("SELECT customerNumber, customerName FROM customers ORDER BY customerName;")
customer_options = {row['customerNumber']: f"{row['customerName']} (ID: {row['customerNumber']})" 
                    for index, row in df_customers.iterrows()}

# 2. Get customer's most frequent product line (for simulation input)
# This query calculates the most purchased product line for each customer
most_purchased_query = """
WITH CustomerProductSales AS (
    SELECT
        c.customerNumber,
        pl.productLine,
        SUM(od.quantityOrdered) AS TotalQuantity
    FROM
        customers c
    JOIN orders o ON c.customerNumber = o.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    JOIN products p ON od.productCode = p.productCode
    JOIN productlines pl ON p.productLine = pl.productLine
    GROUP BY
        c.customerNumber, pl.productLine
),
RankedSales AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY customerNumber ORDER BY TotalQuantity DESC) as rn
    FROM CustomerProductSales
)
SELECT 
    customerNumber, 
    productLine
FROM 
    RankedSales
WHERE 
    rn = 1;
"""
df_most_purchased = get_data(most_purchased_query)

# --- Recommendation Logic Setup ---
# Define a simple hardcoded recommendation map based on assumed affinity
RECOMMENDATION_MAP = {
    'Classic Cars': ['Vintage Cars', 'Motorcycles', 'Planes'],
    'Planes': ['Ships', 'Trains', 'Classic Cars'],
    'Motorcycles': ['Vintage Cars', 'Classic Cars', 'Trucks and Buses'],
    'Ships': ['Planes', 'Classic Cars', 'Trains'],
    'Trains': ['Trucks and Buses', 'Planes', 'Vintage Cars'],
    'Trucks and Buses': ['Planes', 'Trains', 'Ships'],
    'Vintage Cars': ['Classic Cars', 'Motorcycles', 'Ships']
}

# --- Recommendation Interface ---
st.subheader("Generate Recommendations")

customer_id_selected = st.selectbox(
    "Select a Customer to Generate Recommendations:",
    options=list(customer_options.keys()),
    format_func=lambda x: customer_options[x]
)

if customer_id_selected:
    customer_name = df_customers[df_customers['customerNumber'] == customer_id_selected].iloc[0]['customerName']
    
    # 1. Get the customer's top product line
    top_line_df = df_most_purchased[df_most_purchased['customerNumber'] == customer_id_selected]
    
    if top_line_df.empty:
        st.warning(f"Customer {customer_name} (ID: {customer_id_selected}) has no historical orders to base a recommendation on.")
    else:
        most_purchased_line = top_line_df.iloc[0]['productLine']
        
        # 2. Look up the recommendations
        recommendations = RECOMMENDATION_MAP.get(most_purchased_line, ['Planes', 'Ships', 'Motorcycles']) # Default list
        
        st.markdown("---")
        st.subheader(f"Recommendations for: {customer_name}")
        
        st.metric(
            label="Customer's Most Purchased Line", 
            value=most_purchased_line
        )

        st.markdown("#### Top 3 Recommended Product Lines:")
        
        rec_data = {
            'Rank': [1, 2, 3],
            'Product Line': recommendations,
            'Confidence Score (Simulated)': [0.85, 0.70, 0.55] # Simulated confidence
        }
        df_rec = pd.DataFrame(rec_data).set_index('Rank')
        
        st.table(df_rec)
        
        st.success(
            f"**Action:** Target {customer_name} with email and promotional materials for **{recommendations[0]}**, "
            f"as our model indicates a high purchase affinity."
        )

st.markdown("---")
st.caption(
    "Disclaimer: This recommendation is based on a simple content-based rule (most purchased line). "
    "A production system would use collaborative filtering and matrix factorization for higher accuracy."
)