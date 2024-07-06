from airflow import DAG, Dataset
from airflow.decorators import task

from datetime import datetime

my_file = Dataset('/temp/my_file.text')

with DAG(
    dag_id='consumer',
    schedule = [my_file],
    start_date=datetime(2021, 1, 1),
    catchup=False
):
    @task
    def read_dataset():
        my_file = Dataset('/temp/my_file.text')
        with open(my_file.uri, "r") as f:
            print(f.read)
        
    read_dataset(
)