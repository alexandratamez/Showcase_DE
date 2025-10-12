# tests/test_validate.py
import pandas as pd
from pathlib import Path
from src.etl import validate

BASE = Path(__file__).resolve().parents[1]
PROC = BASE / "data" / "processed"

def test_orders_validation():
    orders = pd.read_parquet(PROC / "orders_staging.parquet")
    errs = validate.validate_orders(orders)
    # assert there are no fatal errors besides expected (this is demo; adjust)
    assert "missing column: order_id" not in errs
