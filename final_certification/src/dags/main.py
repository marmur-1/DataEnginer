import sys
sys.path.insert(0, "/opt/airflow/dags/init")
import os.path
from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from write_ticker_to_db import write_ticker_to_db
from download_tickers import download_tickers
from create_days_analytics import create_days_analytics
from create_days_analytics import check_days_analytics

apikey = Variable.get("apikey", default_var="BV2KKAXL81BMBVWB")
# место сохранения необработаных данных
path_raw_data = Variable.get("path_raw_data_file", default_var="/opt/airflow/dags/")
# список символов валют
symbols = Variable.get("symbols", default_var="IBM, GOOGL, META, AAPL, AMZN, TSLA, MMM, F, EA, ORCL")


# Если файла с сырыми данными не существует то считается что скрипт запускается впервые
# и скачиваются расширенные данные
def download_tickers_task(**kwargs):
    symbol = kwargs['symbol']
    outputsize = "compact"
    if not os.path.exists(path_raw_data+symbol+".json"):
        outputsize = "full"
    download_tickers(symbol, apikey, path_raw_data+symbol+".json", outputsize)


# Перенос данных из файлов в БД игнорируя дубликаты
def write_ticker_to_db_task(**kwargs):
    symbol = kwargs['symbol']
    write_ticker_to_db(path_raw_data+symbol+".json")

# Проходит по таблице дневной аналитики.
# Последний день создаётся/обнавляется всегда
# Если нет дневной аналитики то создает
# Если нет тикетов 5 дней подрят то выходит
def create_days_analytics_task(**kwargs):
    symbol = kwargs['symbol']
    date=datetime.now()
    id_day = (str(date.date())+'_'+symbol)
    i = 0
    while create_days_analytics(id_day) == False:
        date=date-timedelta(days=1)
        id_day = (str(date.date())+'_'+symbol)
    i = 5
    while i>=0:
        date=date-timedelta(days=1)
        id_day = (str(date.date())+'_'+symbol)
        if check_days_analytics(id_day) == False:
            if create_days_analytics(id_day) == True:
                i = 5
        i -= 1

# Создание задач по символу
minute = 0
for symbol in symbols.replace(" ", "").split(","):
    # так как у API есть ограничение 5 запросов в минуту то каждое последующая закачка
    # происходит через менуту от предыдущей каждый 1 час
    dag_id = "trade_"+symbol
    with DAG(
        dag_id="trade_"+symbol,
        start_date=datetime.now()-timedelta(hours=1),
        schedule=str(minute)+" */1 * * *",
        catchup=False
    ) as globals()[dag_id]:
        download_tickers_task_id = "download_tickers_task_"+symbol
        write_ticker_to_db_task_id = "write_ticker_to_db_task_"+symbol
        create_days_analytics_task_id = "create_days_analytics_task_"+symbol

        globals()[download_tickers_task_id] = PythonOperator(
            task_id="download_tickers",
            op_kwargs={'symbol': symbol},
            python_callable=download_tickers_task,
            provide_context=True
        )
        globals()[write_ticker_to_db_task_id] = PythonOperator(
            task_id="write_ticker_to_db",
            op_kwargs={'symbol': symbol},
            python_callable=write_ticker_to_db_task,
            provide_context=True
        )
        globals()[create_days_analytics_task_id] = PythonOperator(
            task_id="create_days_analytics",
            op_kwargs={'symbol': symbol},
            python_callable=create_days_analytics_task,
            provide_context=True
        )
        globals()[download_tickers_task_id] >> globals()[write_ticker_to_db_task_id] >> globals()[create_days_analytics_task_id]
    minute += 1
