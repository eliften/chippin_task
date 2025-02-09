import pandas as pd
from datetime import datetime
import logging

def time_series(df):
    logging.info("Starting time series transformation...")
    try:
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        logging.info("Transaction date converted to datetime.")

        df['year'] = df['transaction_date'].dt.year
        df['month'] = df['transaction_date'].dt.month
        df['day_of_week'] = df['transaction_date'].dt.dayofweek
        df['week_of_year'] = df['transaction_date'].dt.isocalendar().week
        df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
        df['quarter'] = df['transaction_date'].dt.quarter
        logging.info("Time-based features added.")

        df = df.drop("year", axis=1)
        logging.info("Year column dropped.")

        return df
    except Exception as e:
        logging.error(f"Error in time series transformation: {e}")
        raise

def customer_anlys(df):
    logging.info("Starting customer analysis...")
    try:
        customer_features = df.groupby('cb_customer_id').agg(
            total_transactions=('transaction_date', 'count'),
            total_spent=('amount_after_discount', 'sum'),
            avg_spent=('amount_after_discount', 'mean'),
            first_transaction=('transaction_date', 'min'),
            last_transaction=('transaction_date', 'max'),
        ).reset_index()
        logging.info("Customer aggregation completed.")

        today = datetime.today()

        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        customer_features['life_time'] = (customer_features['last_transaction'] - customer_features['first_transaction']).dt.days
        customer_features['recency'] = (today - customer_features['last_transaction']).dt.days
        logging.info("Customer features (lifetime and recency) calculated.")

        return customer_features
    except Exception as e:
        logging.error(f"Error in customer analysis: {e}")
        raise

def branch_analys(df):
    logging.info("Starting branch analysis...")
    try:
        branch_features = df.groupby('cb_branch_id').agg(
            branch_total_sales=('amount_after_discount', 'sum'),
            branch_avg_sales=('amount_after_discount', 'mean'),
            branch_total_discount=('amount_discount', 'sum'),
            branch_transaction_count=('transaction_date', 'count'),
        ).reset_index()
        logging.info("Branch aggregation completed.")

        return branch_features
    except Exception as e:
        logging.error(f"Error in branch analysis: {e}")
        raise