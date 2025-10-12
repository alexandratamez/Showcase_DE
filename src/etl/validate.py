# src/etl/validate.py
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
PROC = BASE / "data" / "processed"

def check_nulls(df, col_thresholds=None):
    """Return dict of column -> pct_null"""
    res = {}
    for c in df.columns:
        res[c] = df[c].isnull().mean()
    return res

def validate_orders(df):
    errors = []
    # required columns
    required = ["order_id","customer_id","order_date","amount","status"]
    for r in required:
        if r not in df.columns:
            errors.append(f"missing column: {r}")
    # negative or missing amounts
    if "amount" in df.columns:
        if (df["amount"].dropna() < 0).any():
            errors.append("negative amounts present")
        pct_null = df["amount"].isnull().mean()
        if pct_null > 0.05:
            errors.append(f"too many null amounts ({pct_null:.2%})")
    # duplicate order ids
    if df["order_id"].duplicated().any():
        errors.append("duplicate order_id found")
    return errors

if __name__ == "__main__":
    orders = pd.read_parquet(PROC / "orders_staging.parquet")
    print("Null summary:", check_nulls(orders))
    print("Validation errors:", validate_orders(orders))
