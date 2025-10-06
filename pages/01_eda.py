import streamlit as st
import pandas as pd
import plotly.express as px
from utils.db_connector import get_data

st.title("📊 Exploratory Data Analysis: Classic Models' Foundations")
st.header("Understanding the Business Pulse")

# --- Chapter 1: The Global Reach and Core Customer Base ---
st.markdown("---")
st.subheader("Chapter 1: The Global Reach and Core Customer Base 🌍")

# 1. Customer Distribution by Country (Bar Chart)
st.markdown("#### 1.1 Customer Distribution by Country (Top 10)")
country_count_query = """
SELECT 
    country, 
    COUNT(customerNumber) AS customer_count
FROM 
    customers
GROUP BY 
    country
ORDER BY 
    customer_count DESC
LIMIT 10;
"""
df_country_counts = get_data(country_count_query)

if not df_country_counts.empty:
    fig_country = px.bar(
        df_country_counts, 
        x='customer_count', 
        y='country', 
        orientation='h',
        title='Top 10 Countries by Customer Count',
        labels={'customer_count': 'Number of Customers', 'country': 'Country'}
    )
    fig_country.update_yaxes(categoryorder='total ascending')
    st.plotly_chart(fig_country, use_container_width=True)
    st.info("**Insight:** The USA is the dominant market, suggesting a need for focused international expansion or deeper penetration in key European markets.")
else:
    st.warning("Could not load Customer Country data.")

# 2. Customer Credit Limit Distribution (Histogram)
st.markdown("#### 1.2 Customer Credit Limit Distribution")
credit_limit_query = "SELECT creditLimit FROM customers;"
df_credit_limits = get_data(credit_limit_query)

if not df_credit_limits.empty:
    fig_credit = px.histogram(
        df_credit_limits,
        x='creditLimit',
        nbins=20,
        title='Distribution of Customer Credit Limits',
        labels={'creditLimit': 'Credit Limit ($)', 'count': 'Number of Customers'}
    )
    st.plotly_chart(fig_credit, use_container_width=True)
    st.info("**Insight:** The distribution is skewed, indicating many customers with lower limits but a significant tail of high-value customers who drive large revenue.")
else:
    st.warning("Could not load Customer Credit Limit data.")


# --- Chapter 2: The Inventory & Sales Performance Engines ---
st.markdown("---")
st.subheader("Chapter 2: The Inventory & Sales Performance Engines ⚙️")

# 3. Product Line Sales Volume (Pie Chart for Proportion)
st.markdown("#### 2.1 Product Line Sales Volume & Proportion")
product_sales_query = """
SELECT
    pl.productLine,
    SUM(od.quantityOrdered) AS TotalQuantitySold
FROM
    productlines pl
JOIN
    products p ON pl.productLine = p.productLine
JOIN
    orderdetails od ON p.productCode = od.productCode
GROUP BY
    pl.productLine
ORDER BY
    TotalQuantitySold DESC;
"""
df_product_sales = get_data(product_sales_query)

if not df_product_sales.empty:
    fig_sales_volume = px.pie(
        df_product_sales,
        values='TotalQuantitySold',
        names='productLine',
        title='Proportion of Total Quantity Sold by Product Line'
    )
    st.plotly_chart(fig_sales_volume, use_container_width=True)
    st.info("**Insight:** 'Classic Cars' dominate sales volume. Marketing efforts should either double down on this winner or strategically boost lagging lines like 'Motorcycles' and 'Trucks and Buses'.")
else:
    st.warning("Could not load Product Sales Volume data.")


# 4. Profitability by Product Line (Bar Chart)
st.markdown("#### 2.2 Profitability by Product Line (Gross Profit)")
profit_query = """
SELECT
    pl.productLine,
    SUM((od.priceEach - p.buyPrice) * od.quantityOrdered) AS GrossProfit
FROM
    productlines pl
JOIN
    products p ON pl.productLine = p.productLine
JOIN
    orderdetails od ON p.productCode = od.productCode
GROUP BY
    pl.productLine
ORDER BY
    GrossProfit DESC;
"""
df_profit = get_data(profit_query)

if not df_profit.empty:
    fig_profit = px.bar(
        df_profit,
        x='productLine',
        y='GrossProfit',
        title='Gross Profit by Product Line',
        labels={'productLine': 'Product Line', 'GrossProfit': 'Gross Profit ($)'}
    )
    st.plotly_chart(fig_profit, use_container_width=True)
    st.info("**Insight:** Profitability generally aligns with sales volume, confirming 'Classic Cars' as the primary revenue engine. However, we should check if lower-selling lines have better margins, indicating untapped profit potential.")
else:
    st.warning("Could not load Product Profitability data.")