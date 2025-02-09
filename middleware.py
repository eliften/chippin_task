from feature_eng.methods import time_series, customer_anlys, branch_analys
from preprocessing.methods import open_files_and_merge, find_missing_values, remove_future_dates
import logging

def start_logging(log_file="app.log"):
    logging.basicConfig(
        filename=log_file, 
        level=logging.DEBUG, 
        format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("Logging started.")
start_logging("app.log")

def get_data():
    folder_path = "assets/cambaz_sample/"
    datas = open_files_and_merge(folder_path)
    data = find_missing_values(datas)
    df = remove_future_dates(data, "transaction_date")
    time_series_df = time_series(df)
    customer_anlys_df = customer_anlys(df)
    branch_analys_df = branch_analys(df)
    return time_series_df, customer_anlys_df, branch_analys_df
