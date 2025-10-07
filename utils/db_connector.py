import pandas as pd
from sqlalchemy import create_engine, text
import streamlit as st

DATABASE_FILE = "classicmodels.sqlite"

@st.cache_resource
def get_engine():
    """Initializes and returns the SQLAlchemy engine, cached for efficiency."""
    # SQLite URL format: sqlite:///path/to/database.db
    engine = create_engine(f"sqlite:///data/{DATABASE_FILE}")
    return engine

def get_data(sql_query: str) -> pd.DataFrame:
    """Executes an SQL query and returns the result as a pandas DataFrame."""
    engine = get_engine()
    
    # We use a connection object for executing the query.
    # The 'with' statement ensures the connection is closed and returned to the pool.
    with engine.connect() as connection:
        try:
            # The text() construct is used to execute literal SQL strings
            result = connection.execute(text(sql_query))
            
            # Fetch all results and column names
            columns = result.keys()
            data = result.fetchall()
            
            # Convert to DataFrame
            df = pd.DataFrame(data, columns=columns)
            return df
        except Exception as e:
            st.error(f"Database Query Error: {e}")
            return pd.DataFrame()

# The engine can be disposed manually if needed, but Streamlit handles resource cleanup.
# def dispose_engine():
#     get_engine().dispose()