# 🚀 Showcase Data Engineering & Analytics Pipeline

## 🎯 Project Purpose
This project demonstrates a **production-grade ETL and analytics pipeline** built for e-commerce data.  
It highlights how raw datasets can be **ingested, validated, transformed, and visualized** using Python and modern data engineering best practices.  

Designed as a portfolio-ready project, it showcases both **data engineering** and **data analytics** expertise through a reproducible, automated workflow.

---

## 🏗️ Architecture Overview

- **Raw:** Synthetic CSV files simulating customer and order data  
- **Staging / Processed:** Cleaned and standardized Parquet files  
- **Transform:** Business logic, derived metrics, and aggregations  
- **Dashboard:** Interactive Streamlit dashboard with KPIs, top products, and time-based trends  

---

## 🧰 Tech Stack

- **Python** – core scripting and ETL orchestration  
- **Pandas** – data cleaning, transformation, and aggregation  
- **Parquet** – efficient intermediate data storage  
- **Streamlit** – dashboard visualization  
- **Airflow** (optional) – DAG-based pipeline automation  
- **GitHub Actions** – CI/CD and reproducibility  
- **Docker** (optional) – containerized environment for development and deployment  

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/showcase-data-engineering.git
cd showcase-data-engineering

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate synthetic data
python src/data_gen.py

# 4. Run the ETL pipeline
python src/etl/ingest.py
python src/etl/validate.py
python src/etl/transform.py

# 5. Launch the dashboard
streamlit run src/app/dashboard.py
```

## Key Highlights

- Idempotent pipeline: Re-running the workflow won’t create duplicates (deduplication logic included).
- Data validation: Detects missing values, invalid formats, and inconsistencies before processing.
- Meaningful transformations: Includes derived metrics such as total sales, average order value, and daily aggregates.
- Orchestration with Airflow: Demonstrates task sequencing and pipeline automation.
- Reproducibility: CI workflows and Docker ensure consistency across environments.
- Automation-ready: Modular scripts designed for integration with cloud schedulers or CI/CD pipelines.

## Dashboard Features

- KPI metrics: Total Sales, Average Order Value, and Unique Customers
- Top products & cities: Ranked by revenue
- Sales over time: Interactive time series charts
- Data quality previews: Optional display of validation results

<div align="center"> <img src="images/dashboard demo.png" alt="Streamlit Dashboard Demo" width="700"> </div>

## Project Structure

project/
│
├── data/
│   ├── raw/                # Stores raw datasets
│   └── processed/          # Contains cleaned and transformed data
│
├── src/
│   ├── etl/
│   │   ├── ingest.py       # Ingests data from raw sources
│   │   ├── validate.py     # Validates data quality and detects issues
│   │   └── transform.py    # Applies cleaning and transformation logic
│   │
│   └── app/
│       └── dashboard.py    # Streamlit dashboard application
│
└── dags/
    └── showcase_dag.py     # Airflow DAG automating the ETL workflow

## File Explanations
- data/raw/
Stores raw, unprocessed datasets used as input for the ETL pipeline.

- data/processed/
Contains validated and transformed data, ready for analysis and visualization.

- src/etl/ingest.py
Handles data ingestion from CSVs or external sources into the raw data directory.

- src/etl/validate.py
Performs quality checks — identifies nulls, duplicates, and incorrect formats — and logs issues for review.

- src/etl/transform.py
Executes the main transformation logic, cleaning and enriching data for analytical use.

- dags/showcase_dag.py
Defines an Airflow DAG that automates the full ETL process, from ingestion to transformation.

- src/app/dashboard.py
Creates the Streamlit dashboard visualizing processed data.


## CI / Automation

GitHub Actions ensures consistent, automated validation of the project on every push or pull request:
- Runs ETL scripts end-to-end
- Installs dependencies from requirements.txt
- Executes validation and transformation tests
- Performs linting and code quality checks

## Notes

The pipeline can easily be extended to handle real-world client data or cloud data sources.
The project follows production-like standards to serve as a strong portfolio example for data engineering and analytics.
Additional documentation, screenshots, or validation reports can be added under /docs for stakeholders or recruiters.

## 👩‍💻 Author
Alexandra Tamez
Data Engineer | Data Analyst | Machine Learning Integrator
[LinkedIn](https://www.linkedin.com/in/alexandratamez/) • [GitHub](https://github.com/alexandratamez)

