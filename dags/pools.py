"""
Learning airflow trigger usage
"""
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

dag = DAG(
    'pool', 
    description='Nossa pool DAG',
    schedule_interval=None,
    start_date=datetime(2023, 11, 26),
    default_view='graph',
    catchup=False)

task1 = BashOperator(task_id="tsk1", bash_command="sleep 4", dag=dag, pool='meupool')
task2 = BashOperator(task_id="tsk2", bash_command="sleep 4", dag=dag, pool='meupool',
                     priority_weight=5)
task3 = BashOperator(task_id="tsk3", bash_command="sleep 4", dag=dag, pool='meupool')
task4 = BashOperator(task_id="tsk4", bash_command="sleep 4", dag=dag, pool='meupool',
                     priority_weight=10)
