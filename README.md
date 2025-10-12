# Showcase Data Engineering & Analytics Pipeline

## Project Purpose
This repository demonstrates a production-like ETL pipeline for e-commerce data. It shows how raw data can be ingested, validated, transformed, and visualized using Python and modern data engineering best practices. The project is designed to highlight both **data engineering** and **data analytics** skills in a reproducible, automated workflow.

---

## Architecture


- **Raw:** Synthetic CSV files simulating customer and order data  
- **Staging:** Cleaned and partially processed Parquet files  
- **Transform:** Final data transformations, derived metrics, aggregation  
- **Dashboard:** Interactive Streamlit dashboard displaying KPIs, top products, top cities, and sales over time  

---

## Tech Stack
- **Python** – data processing, scripting, and ETL  
- **Pandas** – data cleaning, aggregation, and transformations  
- **Parquet** – efficient intermediate storage  
- **Streamlit** – dashboard and visualization  
- **Airflow** (optional) – pipeline orchestration demonstration  
- **GitHub Actions** – CI for automated testing and reproducibility  
- **Docker** (optional) – containerized development and deployment  

---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/showcase-data-engineering.git
cd showcase-data-engineering

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate synthetic data
python src/data_gen.py

# 4. Run ETL pipeline
python src/etl/ingest.py
python src/etl/validate.py
python src/etl/transform.py

# 5. Launch dashboard
streamlit run src/app/dashboard.py

--- 

## What I Want You to Notice

- **Idempotent pipeline:** re-running the pipeline does not create duplicates (deduplication logic)
- **Data validation:** prevents bad downstream data; printed validation errors highlight missing or duplicate rows
- **Lightweight but realistic transformations:** includes derived metrics like amount and daily aggregates for analytics
- **Orchestration example:** simple DAG demonstrates task sequencing (optional Airflow integration)
- **Reproducible development:** containerized environment with Docker and automated CI using GitHub Actions
- **Automation & tests:** pipeline scripts and CI ensure consistent, reliable outputs


## Dashboard Highlights

- **KPI metrics:** Total Sales, Average Order Value, Unique Customers  
- **Top products and cities:** Bar charts with derived revenue metrics  
- **Sales over time:** Line charts with daily aggregates and interactive filters  
- **Data quality checks:** Optional preview tables showing validation results  

---

## Demo

A short video shows the pipeline running end-to-end, including data generation, pipeline execution, validation, transformation, and the interactive Streamlit dashboard.

---

## Optional Notes

- The pipeline can be extended to handle real client data  
- The workflow demonstrates production-like standards for a portfolio-ready DE/DA project  
- Screenshots of the dashboard and sample validation outputs can be added to `docs/` for non-technical stakeholders  

---

## CI / Automation

GitHub Actions runs the pipeline and tests automatically on each push or pull request. This ensures:

- **The pipeline scripts are always functional**  
- **Dependencies** are correctly installed from `requirements.txt`  
- **Data validation and transformation steps** are executed without manual intervention  
- **Linting and code quality checks** are performed
