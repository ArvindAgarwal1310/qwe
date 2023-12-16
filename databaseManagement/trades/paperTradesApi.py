from .paperTrades import *

from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import json

paperTrades_api = APIRouter(prefix='/trades', tags=['trades'])
paper_trades = PaperTrade(r"databaseManagement\trades\tradeDatabase.db")


@paperTrades_api.post('/insert')
def insert_trades_api(userid='XYZ123',
                      trade_id='01091',
                      order_id='10911',
                      tradingsymbol='NIFTYFUT',
                      exchange='NFO',
                      average_price=18019.5,
                      quantity=50,
                      transaction_type='BUY',
                      timestamp=datetime.now().strftime('%d/%m/%Y %H:%M')):
    global paper_trades

    ret = paper_trades.insert_trade(userid=userid, tradeid=trade_id, order_id=order_id, exchange=exchange, tradingsymbol=tradingsymbol,
                                    average_price=average_price, quantity=quantity, transaction_type=transaction_type,
                                    timestamp=timestamp)
    return ret


@paperTrades_api.get('/get')
def get_trades_api():
    global paper_trades

    df = paper_trades.getTrade()
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@paperTrades_api.get('/get_by_orderid')
def get_trade_by_orderid_api(orderid):
    global paper_trades

    df = paper_trades.GetTradeByOrderID(order_id=orderid)
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@paperTrades_api.get('/get_by_datetime')
def get_trade_by_datetime(startdate, enddate):
    global paper_trades

    df = paper_trades.GetTradeByDate(startdate=startdate, enddate=enddate)
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@paperTrades_api.delete('/delete_by_orderid')
def delete_trade_by_orderid_api(orderid):
    global paper_trades

    ret = paper_trades.deleteTradeByOrderID(order_id=orderid)
    return ret


@paperTrades_api.delete('/delete_by_datetime')
def delete_trade_by_datetime(startdate, enddate):
    global paper_trades

    ret = paper_trades.deleteTradeByDate(startdate=startdate, enddate=enddate)
    return ret
