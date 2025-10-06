# Streamlit ML Dashboard for Customer Sales Prediction

This project is a Streamlit-based machine learning dashboard for customer sales prediction, featuring Exploratory Data Analysis (EDA), Feature Engineering (FE), and XGBoost model predictions. The dashboard integrates with Azure Synapse Analytics for data storage and querying, enabling scalable data processing and analytics.

## Project Overview

This is a dashboard app project with the following planned features:

1. SQL: Create a SQLite DB Engine to convert and upload a CSV dataset to enable SQL queries.
2. Python: Streamlit Dashboard App with EDA, Feature Engineering & Model prediction sections/pages.
3. Cloud: App hosting on Streamlit Community Cloud and transfer of SQL Database to Azure Cloud
4. Big Data Engineering Cloud Infrastructure: Connecting the Streamlit App to the Azure Database via Azure Synapse, enabling larger future datasets, with option to use Spark/Databricks.
5. Containerization: Containerize with Docker

## Repository Structure

```
ml_dashboard/
├── app.py                        # Main Streamlit app with sidebar navigation
├── classicmodels.sqlite          # MySQL Classic Models Business Dataset
├── pages/
│   ├── 01_eda.py                 # EDA page with visualizations
│   ├── 02_ml_churn.py            # ML page for calculating churn of customers
│   ├── 03_ml_product_reco.py     # ML page for product recommendations based on past purchase history
│   └── 04_ml_credit_risk.py      # ML page for risk prediction based on customer credit rating
├── utils/
│   └── db_connector.py           # Module to connect with SQLEngine
├── data/
│   └── sales_data.csv            # Dummy dataset for testing
│   └── customers.csv             # Dummy dataset for testing
│   └── orders.csv                # Dummy dataset for testing
│   └── orderdetails.csv          # Dummy dataset for testing
│   └── classicmodels.sqlite      # Copy of MySQL Classic Models Business Dataset for notebook testing
├── notebooks/
│   └── draft.ipynb               # Draft notebook version of the entire app
│   └── sql_test.ipynb            # Setup and testing of SQL Engine for SQL usage
├── pyproject.toml                # Python dependencies
├── poetry.lock                   # Poetry dependencies version lock file
└── README.md                     # This file
``` 

## Prerequisites
### Local VENV
- Python 3.12.5, 
- Poetry >= 2.0, <= 3.0, for dependency management
- See pyproject.toml for full dependency list
### Azure Cloud
- Azure Subscription
- Azure Resource Group

## Running the app locally
If running with poetry run with command
```python
poetry run streamlit run app.py
```