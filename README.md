# Streamlit ML Dashboard for Customer Sales Prediction

This project is a Streamlit-based machine learning dashboard for customer sales prediction, featuring Exploratory Data Analysis (EDA), Feature Engineering (FE), and XGBoost model predictions. The dashboard integrates with Azure Synapse Analytics for data storage and querying, enabling scalable data processing and analytics.

## Project Overview

This is a dashboard app project with the following planned features:

1. SQL: Create a SQLite DB Engine to convert and upload a CSV dataset to enable SQL queries.
2. Python: Streamlit Dashboard App with EDA, Feature Engineering & Model prediction sections/pages.
3. Cloud: App hosting on Streamlit Community Cloud and transfer of SQL Database to Azure Cloud
4. Big Data Engineering Cloud Infrastructure: Connecting the Streamlit App to the Azure Database via Azure Synapse, enabling larger future datasets, with option to use Spark/Databricks.
5. Containerization: Containerize with Docker

## AI-Assisted Development Process

This Streamlit application was developed using AI-assisted coding (Gemini and GPT) under a guided, structured workflow emphasizing human oversight and prompt engineering skill.

My Contributions and Methods:

- **System Design and Context Planning** – Defined the overall app structure, project setup, dependency management (poetry), secrets management, data flow, and SQL Server connection requirements through progressive prompt scaffolding.

- **Prompt Engineering** – Structured prompts to incrementally build context and maintain coherence across sessions, ensuring the model followed a logical development path.

- **Technical Oversight** – Identified and corrected model-generated issues such as Python package version mismatches, deprecated or legacy syntax, and broken dependencies.

- **AI Workflow Management** – Directed the model to decompose complex coding tasks into smaller steps to minimize hallucination and improve consistency.

- **Conversation Strategy** – Managed AI conversation states, deciding when to continue an existing thread or restart with refined context for clarity and accuracy.

- **Integration Experience** – Leveraged prior experience in process automation systems (PAS) development to align the app’s architecture with robust data-handling and reliability practices.

This approach combines human design intent with AI acceleration, emphasizing practical prompt engineering, code validation, and iterative refinement rather than one-shot code generation.

Recommended resource: [The Quick Guide to Prompt Engineering by Ian Khan](https://www.amazon.sg/dp/1394243324)

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