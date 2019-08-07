#pip install flask flask-jsonpify flask-sqlalchemy flask-restful
import stockservice;

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

ss = stockservice.StockService();

class Stocks(Resource):
    def get(self, symbol):
        data = ss.getDaily(symbol);
        print('data', data)
        return {'data': data};


# def getInput():
#     symbol = raw_input('enter Symbol you want to search ?');
#
#
#
# getInput();

api.add_resource(Stocks, '/stock/<symbol>')

if __name__ == '__main__':
     app.run(port='5002')
