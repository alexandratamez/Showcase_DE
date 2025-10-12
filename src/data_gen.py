from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_customers(n=100):
    data = []
    for _ in range(n):
        data.append({
            "customer_id": fake.uuid4() if random.random() > 0.05 else None,  # some missing IDs
            "name": fake.name() if random.random() > 0.05 else fake.name().upper(),  # inconsistent casing
            "email": fake.email() if random.random() > 0.1 else "",  # some missing emails
            "city": random.choice([fake.city(), fake.city().upper(), None]),  # inconsistent casing + nulls
            "signup_date": fake.date_between(start_date="-2y", end_date="today").strftime("%Y/%m/%d")
        })
    return pd.DataFrame(data)

def generate_orders(n=350, customer_ids=None):
    data = []
    for _ in range(n):
        data.append({
            "order_id": fake.uuid4(),
            "customer_id": random.choice(customer_ids) if customer_ids and random.random() > 0.1 else None,  # missing foreign keys
            "product": random.choice(["Empanadas", "Cake", "Cookies", "EMPANADAS", None]),
            "quantity": random.choice([1, 2, 3, None]),
            "price": random.choice([50, 75, 100, None]),
            "order_date": fake.date_time_this_year().strftime("%d-%m-%Y %H:%M:%S")
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    customers = generate_customers()
    orders = generate_orders(customer_ids=customers["customer_id"].dropna().tolist())

    customers.to_csv("../data/raw/customers_raw.csv", index=False)
    orders.to_csv("../data/raw/orders_raw.csv", index=False)

    print("✅ Raw data generated: customers_raw.csv and orders_raw.csv")
