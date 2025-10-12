from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[2]  # project root
RAW = BASE / "data/raw"
PROC = BASE / "data/processed"
PROC.mkdir(exist_ok=True)


def transform():
    df_customers = pd.read_csv(RAW / "customers_raw.csv")
    df_orders = pd.read_csv(RAW/ "orders_raw.csv")

    #Customers 
    df_customers = df_customers.dropna(subset=["customer_id", "email"])
    df_customers["name"] = df_customers["name"].str.title().str.strip()

    #Clean cities
    df_customers["city"] = (
    df_customers["city"]
    .fillna("Unknown")  # optional placeholder if city missing
    .str.title()        # makes "NEW YORK" → "New York"
    .str.strip()        # removes leading/trailing spaces
)

    #Orders 
    #drop orders with missing crucial info
    df_orders = df_orders.dropna(subset=["customer_id", "product"])

    #fil missing info 
    df_orders["quantity"].fillna(1, inplace=True)  # assume quantity 1 if missing
    df_orders["price"].fillna(0, inplace=True)     # assume price 0 if missing


    # Standardize text
    df_orders["product"] = df_orders["product"].str.lower().str.strip()

    # Add missing columns expected by validation/dashboard
    df_orders["amount"] = df_orders["quantity"] * df_orders["price"]
    df_orders["status"] = "completed"  # default value

    #Remove duplicates
    df_orders = df_orders.drop_duplicates(subset=["order_id"])

    # Save cleaned data
    PROC.mkdir(exist_ok=True)
    df_customers.to_parquet(PROC / "customers_staging.parquet", index=False)
    df_orders.to_parquet(PROC / "orders_staging.parquet", index=False)

if __name__ == "__main__":
    transform()
    print("✅ Transform complete: orders and customers ready for dashboard")

