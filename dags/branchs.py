"""
Learning airflow trigger usage
"""
from datetime import datetime
import random
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

dag = DAG(
    'branch', 
    description='Nossa branch DAG',
    schedule_interval=None,
    start_date=datetime(2023, 11, 26),
    default_view='graph',
    catchup=False)

def gera_aleatorio():
    """
    Generate random integer
    """
    return random.randint(1, 100)

gera_nro_aleatorio_task = PythonOperator(
    task_id="gera_nro_aleatorio_task",
    python_callable=gera_aleatorio,
    dag=dag
)

def avalia_nro_aleatorio(**context):
    """
    Retrieve task data and decide if it is odd or not
    """
    number = context['task_instance'].xcom_pull(task_ids="gera_nro_aleatorio_task")
    if number % 2 == 0:
        return 'par_task'
    else:
        return 'impar_task'

branch_task = BranchPythonOperator(
    task_id="branch_task",
    python_callable=avalia_nro_aleatorio,
    provide_context=True,
    dag=dag
)

par_task = task1 = BashOperator(task_id="par_task", bash_command='echo "Número Par"', dag=dag)
impar_task = task1 = BashOperator(task_id="impar_task", bash_command='echo "Número Ímpar"', dag=dag)

gera_nro_aleatorio_task >> branch_task
branch_task >> par_task
branch_task >> impar_task
