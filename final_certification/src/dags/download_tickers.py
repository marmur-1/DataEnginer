import json
import requests


def download_tickers(symbol, apikey, path_file="tickets.json", outputsize="compact"):
    func = "TIME_SERIES_INTRADAY"
    interval = "1min"
    adjusted = "true"

    url = 'https://www.alphavantage.co/query/?function='+func+'&symbol='+symbol + \
        '&interval='+interval+'&adjusted='+adjusted + \
        '&outputsize='+outputsize+'&apikey='+apikey
    print(url)
    r = requests.get(url)
    data = r.json()

    with open(path_file, "w", encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False)

