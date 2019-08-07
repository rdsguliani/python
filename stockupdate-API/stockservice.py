import requests

apikey = 'PSLV87KDUJWTR1P3';

class StockService():

    def __init__(self):
        pass

    def getDaily(self, symbol):

        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={}&apikey={}'.format(symbol, apikey);
        resp = requests.get(url)
        obj =  resp.json()
        metaData = obj['Meta Data']
        print('Meta Data: {}'.format(metaData));
        return metaData;
