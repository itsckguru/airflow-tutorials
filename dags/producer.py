from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset('/temp/my_file.text')

with DAG(
    dag_id='producer',
    schedule = '@daily',
    start_date=datetime(2021, 1, 1),
    catchup=False
):
    
    @task(outlets=[my_file])
    def update_dataset():
        with open(my_file.uri, "a+") as f:
            f.write('producer update')

    update_dataset()