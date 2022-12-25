from datetime import datetime
import psycopg2
import pandas as pd

#Проверка наличиа аналитики на день
def check_days_analytics(id_day):
    conn = psycopg2.connect(dbname='project',
                        user='airflow',
                        password='airflow',
                        host='postgres')

    # conn = psycopg2.connect(dbname='project',
    #                         user='airflow',
    #                         password='airflow',
    #                         host='localhost',
    #                         port=5000)

    cursor = conn.cursor()
    query = "SELECT count(*) FROM days_analytics WHERE id_day = %s;"
    cursor.execute(query,[id_day])
    results = cursor.fetchone()
    conn.commit()  
    cursor.close()
    conn.close()
    if results[0] == 0:
        return False
    else:
        return True


#Создание аналитики на день
def create_days_analytics(id_day):
    conn = psycopg2.connect(dbname='project',
                        user='airflow',
                        password='airflow',
                        host='postgres')

    # conn = psycopg2.connect(dbname='project',
    #                         user='airflow',
    #                         password='airflow',
    #                         host='localhost',
    #                         port=5000)

    cursor = conn.cursor()

    query = "SELECT * FROM tickets WHERE id_day = %s;"
    cursor.execute(query,[id_day])
    column_names = [desc[0] for desc in cursor.description]
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=column_names)
    print(df)

    symbol = results[0][0]
    print('symbol',symbol)
    sum_volume = int(df.volume.sum())
    print('sum_volume', sum_volume)
    day_open = float(df.loc[df['timestamp'] == df.timestamp.min()].open) 
    print('day_open',df.timestamp.min(),' ',day_open)
    day_close = float(df.loc[df['timestamp'] == df.timestamp.max()].close) 
    print('day_open',df.timestamp.max(),' ',day_close)
    relative_op = round(float((day_close/day_open-1)*100.0),2)
    print('relative_op',relative_op)
    max_volume_interval = datetime.utcfromtimestamp(int(df.loc[df['volume'] == df.volume.max()].timestamp.values[0])/1e9)
    print('max_volume_interval', max_volume_interval)
    max_price_interval = datetime.utcfromtimestamp(int(df.loc[df['high'] == df.high.max()].sort_values(by='timestamp').timestamp.values[0])/1e9)
    print('max_price_interval',max_price_interval)
    min_price_interval = datetime.utcfromtimestamp(int(df.loc[df['low'] == df.high.min()].sort_values(by='timestamp').timestamp.values[0])/1e9)
    print('min_price_interval',min_price_interval)

    insert_query = """INSERT INTO days_analytics (id_day, symbol, sum_volume, day_open, day_close, relative_op, max_volume_interval, max_price_interval, min_price_interval) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (id_day) DO UPDATE
    SET sum_volume=%s, day_open=%s, day_close=%s, relative_op=%s, max_volume_interval=%s, max_price_interval=%s, min_price_interval=%s;"""
    cursor.execute(insert_query,[id_day,symbol,sum_volume,day_open,day_close,relative_op,max_volume_interval,max_price_interval,min_price_interval,
                                               sum_volume,day_open,day_close,relative_op,max_volume_interval,max_price_interval,min_price_interval])
    conn.commit()  
    cursor.close()
    conn.close()

# check_days_analytics(id_day="IBM_2022-12-12")
# create_days_analytics(id_day="IBM_2022-12-12")