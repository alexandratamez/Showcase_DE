# tests/test_transform.py
import pandas as pd
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
PROC = BASE / "data" / "processed"

def test_transform_outputs_exist():
    assert (PROC / "orders_transformed.parquet").exists()
    assert (PROC / "customers_transformed.parquet").exists()
