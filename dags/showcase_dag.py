# dags/showcase_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pathlib import Path
import importlib

default_args = {"start_date": datetime(2025,1,1)}
dag = DAG("showcase_etl", schedule_interval=None, default_args=default_args)

def run_data_gen():
    import src.data_gen as dg
    dg.generate_customers(50)
    dg.generate_orders(200, pd.read_csv(Path(__file__).resolve().parents[2] / "data" / "raw" / "customers.csv"))

def run_ingest():
    import src.etl.ingest as ingest
    c, o = ingest.load_raw()
    ingest.write_staging(c, o)

def run_validate():
    import src.etl.validate as validate
    orders = pd.read_parquet(Path(__file__).resolve().parents[2] / "data" / "processed" / "orders_staging.parquet")
    print(validate.validate_orders(orders))

def run_transform():
    import src.etl.transform as t
    t.transform()

t1 = PythonOperator(task_id="data_gen", python_callable=run_data_gen, dag=dag)
t2 = PythonOperator(task_id="ingest", python_callable=run_ingest, dag=dag)
t3 = PythonOperator(task_id="validate", python_callable=run_validate, dag=dag)
t4 = PythonOperator(task_id="transform", python_callable=run_transform, dag=dag)

t1 >> t2 >> t3 >> t4
