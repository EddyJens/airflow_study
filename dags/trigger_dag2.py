"""
Learning airflow trigger usage
"""
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    'trigger2_dag', 
    description='Nossa trigger2 DAG',
    schedule_interval=None,
    start_date=datetime(2023, 11, 26),
    catchup=False)

task1 = BashOperator(task_id="tsk1", bash_command="exit 1", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(
    task_id="tsk3",
    bash_command="sleep 5",
    dag=dag,
    trigger_rule='one_failed'
)

[task1, task2] >> task3
