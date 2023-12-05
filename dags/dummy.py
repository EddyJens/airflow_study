"""
Learning airflow trigger usage
"""
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

dag = DAG(
    'dummy', 
    description='Nossa dummy DAG',
    schedule_interval=None,
    start_date=datetime(2023, 11, 26),
    catchup=False, default_view="graph")

task1 = BashOperator(task_id="tsk1", bash_command="sleep 2", dag=dag)
task2 = BashOperator(task_id="tsk2", bash_command="sleep 2", dag=dag)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 2", dag=dag)
task4 = BashOperator(task_id="tsk4", bash_command="sleep 2", dag=dag)
task5 = BashOperator(task_id="tsk5", bash_command="sleep 2", dag=dag)
taskEmpty = EmptyOperator(task_id="taskdummy", dag=dag)

[task1, task2, task3] >> taskEmpty >> [task4, task5]
