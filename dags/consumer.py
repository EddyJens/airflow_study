"""
Learning airflow trigger usage
"""
from datetime import datetime
from airflow import DAG, Dataset
from airflow.operators.python import PythonOperator
import pandas as pd

mydataset = Dataset("/opt/airflow/data/Churn_new.csv")

dag = DAG(
    'consumer', 
    description='Nossa consumer DAG',
    schedule=[mydataset],
    start_date=datetime(2023, 12, 11),
    default_view='graph',
    catchup=False)

def my_file():
    dataset = pd.read_csv("/opt/airflow/data/Churn_new.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/Churn_new2.csv", sep=";")

t1 = PythonOperator(task_id='t1', python_callable=my_file, dag=dag, outlets=[mydataset])

t1
