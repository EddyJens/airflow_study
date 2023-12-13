"""
Learning airflow trigger usage
"""
from datetime import datetime
from airflow import DAG
from big_data_operator import BigDataOperator

dag = DAG(
    'bigdata', 
    description='Nossa bigdata DAG',
    schedule_interval=None,
    start_date=datetime(2023, 11, 26),
    default_view='graph',
    catchup=False)

big_data = BigDataOperator(
    task_id="big_data",
    path_to_csv_file="/opt/airflow/data/Churn.csv",
    path_to_save_file="/opt/airflow/data/Churn.json",
    file_type="json",
    dag=dag
)
