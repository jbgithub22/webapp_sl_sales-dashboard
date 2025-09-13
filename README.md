# Streamlit ML Dashboard for Customer Sales Prediction

This project is a Streamlit-based machine learning dashboard for customer churn prediction, featuring Exploratory Data Analysis (EDA), Feature Engineering (FE), and XGBoost model predictions. The dashboard integrates with Azure Synapse Analytics for data storage and querying, enabling scalable data processing and analytics.

## Project Overview

This is a dashboard app project with the following planned features:

1. SQL: Create a SQLite DB Engine to convert and upload a CSV dataset to enable SQL queries.
2. Python: Streamlit Dashboard App with EDA, Feature Engineering & Model prediction sections/pages.
3. Cloud: App hosting on Streamlit Community Cloud and transfer of SQL Database to Azure Cloud
4. Big Data Engineering Cloud Infrastructure: Connecting the Streamlit App to the Azure Database via Azure Synapse, enabling larger future datasets, with option to use Spark/Databricks.

## Repository Structure

```
ml_dashboard/
├── app.py                    # Main Streamlit app with sidebar navigation
├── pages/
│   ├── 01_eda.py            # EDA page with visualizations
│   ├── 02_feature_eng.py    # Feature engineering page
│   └── 03_modeling.py       # XGBoost modeling and prediction page
├── utils/
│   ├── data.py              # Data loading, preprocessing, and Azure Synapse connection
│   └── modeling.py          # XGBoost training and prediction functions
├── data/
│   └── churn_dummy.csv      # Dummy dataset for testing
├── pyproject.toml           # Python dependencies
├── poetry.lock              # Poetry dependencies version lock file
└── README.md                # This file
```

## Prerequisites
### Local VENV
- Python 3.12.5, 
- Poetry >= 2.0, <= 3.0, for dependency management
- See pyproject.toml for full dependency list
### Azure Cloud
- Azure Subscription
- Azure Resource Group
