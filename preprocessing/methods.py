import os
import logging
import pandas as pd
from datetime import datetime

def open_files_and_merge(folder_path):
    if not os.path.exists(folder_path):
        logging.error(f"Error: The folder '{folder_path}' was not found!")
        raise FileNotFoundError(f"Error: The folder '{folder_path}' was not found!")
    
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    if not csv_files:
        logging.warning("Warning: No CSV files found in the folder!")
        raise ValueError("Warning: No CSV files found in the folder!")

    logging.info(f"CSV files found: {csv_files}")

    cust_best_sample = pd.read_csv(os.path.join(folder_path, 'cust_best_sample.csv'), encoding="utf-8", low_memory=False)
    cust_sample = pd.read_csv(os.path.join(folder_path, 'cust_sample.csv'), encoding="utf-8", low_memory=False)

    if cust_best_sample.empty or cust_sample.empty:
        logging.warning("One or both files ('cust_best_sample', 'cust_sample') are empty.")
    else:
        logging.info("Merging 'cust_best_sample' and 'cust_sample' on 'unique_customer_id'.")
        merged_cust = pd.merge(cust_best_sample, cust_sample, on='unique_customer_id', how='inner')
        logging.info("Merge completed: 'cust_best_sample' and 'cust_sample'.")
    
    trx_sample = pd.read_csv(os.path.join(folder_path, 'trx_sample.csv'), encoding="utf-8", low_memory=False)

    if trx_sample.empty:
        logging.warning("'trx_sample' file is empty.")
    else:
        logging.info("Merging 'merged_cust' with 'trx_sample' on 'cb_customer_id'.")
        final_merged = pd.merge(merged_cust, trx_sample, left_on='cb_customer_id', right_on='cb_customer_id', how='inner')
        logging.info("Merge completed: 'merged_cust' and 'trx_sample'.")
    
    return final_merged

def remove_future_dates(df, date_column):
    today = datetime.today().strftime('%Y-%m-%d')
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    initial_count = len(df)
    df = df[df[date_column] <= pd.to_datetime(today)]
    removed_count = initial_count - len(df)
    logging.info(f"Future dates removed from column '{date_column}'. Rows removed: {removed_count}.")
    return df

def find_missing_values(df):
    df = df.replace('UNKNOWN', pd.NA)
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    
    if missing_values.empty:
        logging.info("No missing values found in the dataset.")
    else:
        logging.warning("Missing values found in the following columns:")
        logging.warning(f"{missing_values}")
        df = df.dropna(axis=1, how='any')
        logging.info("Columns with missing values have been dropped.")
    return df

