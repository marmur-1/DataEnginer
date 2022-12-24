import json
import psycopg2


def write_ticker_to_db(path_file="tickets.json"):
    with open(path_file, "r") as read_file:
        raw_data = json.load(read_file)
    conn = psycopg2.connect(dbname='project',
                            user='airflow',
                            password='airflow',
                            host='postgres')
    cursor = conn.cursor()

    data = []
    Symbol = raw_data["Meta Data"]["2. Symbol"]
    
    for Timestamp in raw_data["Time Series (1min)"]:
        Id = Symbol+" "+Timestamp
        Open = raw_data["Time Series (1min)"][Timestamp]["1. open"]
        Close = raw_data["Time Series (1min)"][Timestamp]["4. close"]
        High = raw_data["Time Series (1min)"][Timestamp]["2. high"]
        Low = raw_data["Time Series (1min)"][Timestamp]["3. low"]
        Volume = raw_data["Time Series (1min)"][Timestamp]["5. volume"]
        data.append((Id, Symbol, Timestamp, Open, Close, High, Low, Volume))
        
    print(data)
    args = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s)", i).decode('utf-8') for i in data)
    insert_query = "INSERT INTO tickets (id, symbol, timestamp, open, close, high, low, volume) VALUES " + (args) + " ON CONFLICT (id) DO NOTHING;"

    cursor.execute(insert_query)

    conn.commit()  
    cursor.close()
    conn.close()