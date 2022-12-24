import json
import requests


def download_tickers(symbol, apikey, path_file="tickets.json", outputsize="compact", interval="1min"):
    func = "TIME_SERIES_INTRADAY"
    # symbol = "IBM"
    # interval ="1min"  #1min, 5min, 15min,30min, 60min
    adjusted = "true"
    # outputsize = "full" #compact, full
    # apikey = "BV2KKAXL81BMBVWB"

    url = 'https://www.alphavantage.co/query/?function='+func+'&symbol='+symbol + \
        '&interval='+interval+'&adjusted='+adjusted + \
        '&outputsize='+outputsize+'&apikey='+apikey
    print(url)
    r = requests.get(url)
    data = r.json()
    # print(data)

    with open(path_file, "w", encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False)
