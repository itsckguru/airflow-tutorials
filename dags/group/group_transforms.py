from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

def transforms_task():
    with TaskGroup("transforms", tooltip="transform task") as group:
        transform_a = BashOperator(
            task_id='download_a',
            bash_command='sleep 10'
        )

        transform_b = BashOperator(
            task_id='download_b',
            bash_command='sleep 10'
        )

        transform_c = BashOperator(
            task_id='download_c',
            bash_command='sleep 10'
        )

        return group
