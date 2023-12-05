"""
Learning airflow trigger usage
"""
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable

dag = DAG(
    'variaveis', 
    description='Nossa variaveis DAG',
    schedule_interval=None,
    start_date=datetime(2023, 11, 26),
    catchup=False)

def print_variable(**context):
    """
    print the var value in airflow logs
    """
    minha_var = Variable.get('minhavar')
    print(f'o valor da variável é: {minha_var}')

task1 = PythonOperator(task_id="tsk1", python_callable=print_variable, dag=dag)

task1
