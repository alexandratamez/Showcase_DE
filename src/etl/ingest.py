# src/etl/ingest.py
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
RAW = BASE / "data" / "raw"
PROC = BASE / "data" / "processed"
PROC.mkdir(parents=True, exist_ok=True)

def load_raw():
    customers = pd.read_csv(RAW / "customers_raw.csv", parse_dates=["signup_date"])
    orders = pd.read_csv(RAW / "orders_raw.csv", parse_dates=["order_date"])
    return customers, orders

def write_staging(customers, orders):
    customers.to_parquet(PROC / "customers_staging.parquet", index=False)
    orders.to_parquet(PROC / "orders_staging.parquet", index=False)

if __name__ == "__main__":
    c, o = load_raw()
    write_staging(c, o)
    print("Wrote staging parquet files to data/processed/")
