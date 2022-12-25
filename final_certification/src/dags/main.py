#первый тестовый DAGs
from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
import sys
import os.path
sys.path.insert(0,"/opt/airflow/dags/init")
from download_tickers import download_tickers
from write_ticker_to_db import write_ticker_to_db

apikey = Variable.get("apikey",default_var="BV2KKAXL81BMBVWB")
# место сохранения необработаных данных
path_raw_data = Variable.get("path_raw_data_file",default_var="/opt/airflow/dags/")
# список символов валют
symbols = Variable.get("symbols",default_var="IBM, GOOGL, META, AAPL, AMZN, TSLA, MMM, F, EA, ORCL")


# Если файла с сырыми данными не существует то считается что скрипт запускается впервые
# и скачиваются расширенные данные
def download_tickers_task(**kwargs):
    symbol = kwargs['symbol']
    outputsize = "compact"
    if not os.path.exists(path_raw_data+symbol+".json"):
        outputsize = "full"
    download_tickers(symbol,apikey,path_raw_data+symbol+".json",outputsize)

def write_ticker_to_db_task(**kwargs):
    symbol = kwargs['symbol']
    write_ticker_to_db(path_raw_data+symbol+".json")


#Создание задач по символу
minute = 0
for symbol in symbols.replace(" ","").split(","):
    #так как у API есть ограничение 5 запросов в минуту то каждое последующая закачка происходит через менуту от предыдущей
    #каждый 1 час
    dag_id = "trade_"+symbol
    with DAG(
        dag_id="trade_"+symbol,
        start_date=datetime.now()-timedelta(hours=1),
        schedule=str(minute)+" */1 * * *",
        catchup=False
    ) as globals()[dag_id]:
        download_tickers_task_id = "download_tickers_task_"+symbol
        write_ticker_to_db_task_id = "write_ticker_to_db_task_"+symbol


        globals()[download_tickers_task_id] = PythonOperator(
            task_id="download_tickers", 
            op_kwargs={'symbol': symbol},
            python_callable = download_tickers_task,
            provide_context=True
        )
        globals()[write_ticker_to_db_task_id] = PythonOperator(
            task_id="write_ticker_to_db", 
            op_kwargs={'symbol': symbol},
            python_callable = write_ticker_to_db_task,
            provide_context=True
        )
        globals()[download_tickers_task_id] >> globals()[write_ticker_to_db_task_id]
    minute += 1
