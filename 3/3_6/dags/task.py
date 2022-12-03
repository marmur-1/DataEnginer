# Задача 3_6 
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd

# использование технологии Variables
from airflow.models import Variable
# путь к файлу /opt/airflow/dags/cities.csv
path_file = Variable.get("path_to_csv",default_var="/opt/airflow/dags/cities.csv")
path_new_file = Variable.get("path_to_new_csv",default_var="/opt/airflow/dags/cities_new.csv")
path_to_set = Variable.get("path_to_set",default_var="/opt/airflow/dags/result")

def task_a(**kwargs):
    # чтение файла
    file = pd.read_csv(path_file)
    # кол-во строк в файле 
    LEN = len(file)
    # вывод в xcom
    kwargs['ti'].xcom_push(key='length_csv', value=LEN)

def task_b(**kwargs):
    # ввод из xcom
    LEN = kwargs['ti'].xcom_pull(task_ids='task_a', key='length_csv')
    # чтение файла
    file = pd.read_csv(path_file)
    # добавление столбца Num от 128 до 1
    file.insert(len(file.columns), "Num", range(1,LEN+1)[::-1], False)
    # сохраниние в файл
    file.to_csv(path_new_file)

with DAG(
    dag_id="task_3_6",
    start_date=datetime(2022,12,3),
    schedule="0 0 * * *"
) as dag:
    python_task = PythonOperator(
        task_id="task_a", 
        python_callable = task_a,
        provide_context=True
    )

    python_task_second = PythonOperator(
        task_id="task_b", 
        python_callable = task_b,
        provide_context=True
    )

    bush_task = BashOperator(
        task_id="task_c",
        bash_command="mv "+path_new_file+" "+path_to_set
    )

    bush_task_second = BashOperator(
        task_id="task_d",
        bash_command="echo Success"
    )

    python_task >> python_task_second >> bush_task >> bush_task_second