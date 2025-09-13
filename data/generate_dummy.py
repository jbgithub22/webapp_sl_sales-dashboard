import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_dummy_data(n_rows=2000, seed=42):
    # Set seed for reproducibility
    np.random.seed(seed)
    random.seed(seed)

    # Define feature ranges and categories
    customer_ids = range(1, n_rows + 1)
    ages = np.random.randint(18, 81, size=n_rows)
    incomes = np.random.normal(60_000, 20_000, size=n_rows).round(2)
    regions = random.choices(['North', 'South', 'East', 'West'], k=n_rows)
    product_categories = random.choices(['Electronics', 'Clothing', 'Books'], k=n_rows)
    start_date = datetime(2024, 1, 1)
    purchase_dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(n_rows)]
    quantities = np.random.randint(1, 11, size=n_rows)
    unit_prices = np.random.uniform(10, 500, size=n_rows).round(2)

    # Introduce ~20% missing values in income
    missing_mask = np.random.choice([True, False], size=n_rows, p=[0.2, 0.8])
    incomes = np.where(missing_mask, np.nan, incomes)

    # Calculate total_sales with noise
    discount_factor = np.random.uniform(0.8, 1.0, size=n_rows)  # Random discount 0-20%
    total_sales = (quantities * unit_prices * discount_factor + np.random.normal(0, 50, n_rows)).round(2)

    # Create DataFrame
    data = {
        'customer_id': customer_ids,
        'age': ages,
        'income': incomes,
        'region': regions,
        'product_category': product_categories,
        'purchase_date': purchase_dates,
        'quantity': quantities,
        'unit_price': unit_prices,
        'total_sales': total_sales
    }
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv('data/dataset.csv', index=False)
    return df

if __name__ == "__main__":
    df = generate_dummy_data()
    print(f"Dataset generated with {len(df)} rows. Saved to 'data/dataset.csv'.")
    print(df.head())