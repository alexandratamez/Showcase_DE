import pandas as pd
import streamlit as st
from pathlib import Path
import plotly.express as px

# -----------------------------
# Paths
# -----------------------------
PROC = Path(__file__).resolve().parents[2] / "data/processed"

orders_file = PROC / "orders_staging.parquet"
customers_file = PROC / "customers_staging.parquet"  # or customers_transformed.parquet

# -----------------------------
# Check files exist
# -----------------------------
if not orders_file.exists():
    st.error(f"Orders file not found: {orders_file}")
    st.stop()

if not customers_file.exists():
    st.error(f"Customers file not found: {customers_file}")
    st.stop()

# -----------------------------
# Load data
# -----------------------------
df_orders = pd.read_parquet(orders_file)
df_customers = pd.read_parquet(customers_file)

# Ensure dates are datetime
df_orders["order_date"] = pd.to_datetime(df_orders["order_date"])

# -----------------------------
# Merge orders with customers
# -----------------------------
# Assuming 'customer_id' is the join key
df_orders = df_orders.merge(
    df_customers[["customer_id", "name", "email", "city"]],
    on="customer_id",
    how="left"
)


# Make sure order_date is datetime
df_orders["order_date"] = pd.to_datetime(df_orders["order_date"], errors="coerce")

# Create the year column for filtering
df_orders["year"] = df_orders["order_date"].dt.year

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filters")

years = sorted(df_orders["year"].unique())
selected_years = st.sidebar.multiselect(
    "Select Year(s):",
    options=years,
    default=years  # all selected by default
)

cities = sorted(df_orders["city"].dropna().unique())
selected_cities = st.sidebar.multiselect(
    "Select City:",
    options=cities,
    default=cities
)

# --- APPLY FILTERS ---
filtered_df = df_orders[df_orders["year"].isin(selected_years) & df_orders["city"].isin(selected_cities)]

# --- DASHBOARD TITLE ---
st.title("📊 Sales Dashboard")
st.markdown("A simple interactive dashboard showing orders and customer data")


# -----------------------------
# Calculate KPIs
# -----------------------------
total_orders = df_orders["order_id"].nunique()
total_revenue = df_orders["amount"].sum()
avg_order_value = df_orders["amount"].mean()
total_customers = df_orders["customer_id"].nunique()

# -----------------------------
# Display KPIs
# -----------------------------

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"${round(total_revenue):,}")
col3.metric("Avg. Order Value", f"${round(avg_order_value):,}")
col4.metric("Total Customers", total_customers)


# -----------------------------
# Aggregate daily metrics
# -----------------------------
daily = df_orders.groupby(df_orders["order_date"].dt.date).agg(
    total_orders=("order_id", "count"),
    total_amount=("amount", "sum")   # sum the 'amount' column
).reset_index()

# Rename column
daily.rename(columns={"order_date": "order_day"}, inplace=True)

# Optional: format total_amount as string (for display, not for plotting)
daily["total_amount"] = daily["total_amount"].apply(lambda x: f"${round(x):,}")

# -----------------------------
# Streamlit App
# -----------------------------

st.subheader("Daily Orders Summary")
st.dataframe(daily)

#Sales Over Time
st.subheader("🕒 Sales Over Time")

# Aggregate daily sales
sales_by_date = (
    filtered_df.groupby("order_date")["amount"]
    .sum()
    .reset_index()
    .sort_values("order_date")
)

# Create Plotly line chart
fig = px.line(
    sales_by_date,
    x="order_date",
    y="amount",
    labels={"order_date": "Month", "amount": ""},  # remove Y-axis label
    title="Sales Over Time"
)

# Format Y-axis as currency
fig.update_yaxes(tickprefix="$")

# Format hover label with $ sign
fig.update_traces(
    hovertemplate="Date: %{x}<br>Amount: $%{y:,.0f}<extra></extra>"
)

# Display chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


#Top Cities by Sales
st.subheader("🏙️ Top Cities by Sales")

# Remove 'Unknown' cities and aggregate
city_sales = (
    filtered_df[filtered_df["city"] != "Unknown"]
    .groupby("city")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# Create Plotly bar chart
fig = px.bar(
    city_sales,
    x="city",
    y="amount",
    labels={"city": "City", "amount": ""},  # remove Y-axis label
    title="Top Cities by Sales"
)

# Format Y-axis as currency
fig.update_yaxes(tickprefix="$")

# Add hover template
fig.update_traces(
    hovertemplate="City: %{x}<br>Amount: $%{y:,.0f}<extra></extra>"
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

#Top Products by Revenue
st.subheader("📦 Top Products by Revenue")
top_products = (
    filtered_df.groupby("product")["amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_products = px.bar(
    top_products,
    x="product",
    y="amount",
    labels={"product": "Product", "amount": ""},
    title="Top Products by Revenue"
)

# Y-axis as $
fig_products.update_yaxes(tickprefix="$")

# Hover with $
fig_products.update_traces(
    hovertemplate="Product: %{x}<br>Amount: $%{y:,.0f}<extra></extra>"
)


st.plotly_chart(fig_products, use_container_width=True)

#Top customers
st.subheader("Top Customers by Total Amount")

# Aggregate top 10 customers
top_customers = (
    df_orders.groupby("name")
    .agg(total_amount=("amount", "sum"))
    .sort_values("total_amount", ascending=False)
    .head(10)
)

# Format total_amount as currency string
top_customers["total_amount"] = top_customers["total_amount"].apply(lambda x: f"${x:,.0f}")

# Display in Streamlit
st.dataframe(top_customers)


st.markdown("---")
st.caption("Data Engineering Showcase | Alexandra Tamez")