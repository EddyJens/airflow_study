"""
Learning airflow trigger usage
"""
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    'xcom', 
    description='Nossa xcom DAG',
    schedule_interval=None,
    start_date=datetime(2023, 11, 26),
    catchup=False)

def task_write(**kwarg):
    """
    writing value
    """
    kwarg['ti'].xcom_push(key='valorxcom1', value=10200)

task1 = PythonOperator(task_id="tsk1", python_callable=task_write, dag=dag)

def task_read(**kwarg):
    """
    reading value
    """
    valor = kwarg['ti'].xcom_pull(key='valorxcom1')
    print(f'valor recuperado: {valor}')

task2 = PythonOperator(task_id="tsk2", python_callable=task_read, dag=dag)

task1 >> task2
