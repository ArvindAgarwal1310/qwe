
from .paperOrders import PaperOrders
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import json

orders_api = APIRouter(prefix="/orders", tags=["orders"])
paper_order = PaperOrders(r"databaseManagement\orders\OrderDatabase.db")


@orders_api.post('/insert')
def insert_orders_api(userid='XYZ123',
                      order_id='10223',
                      trading_symbol='NIFTYFUT',
                      qty=50,
                      exchange='NFO',
                      trans_type='BUY',
                      timestamp=datetime.now().strftime('%d/%m/%Y %H:%M'),
                      product='FUT',
                      order_type='MKT',
                      price=18010.05,
                      stoploss_trigger=17910.05,
                      status='ACTIVE'):
    global paper_order

    ret = paper_order.insert_paper_orders(userid=userid, order_id=order_id, trading_symbol=trading_symbol, qty=qty, exchange=exchange, trans_type=trans_type,
                                          timestamp=timestamp, product=product, order_type=order_type, price=price, stoploss_trigger=stoploss_trigger, status=status)

    return ret


@orders_api.get('/get')
def get_orders_api():
    global paper_order

    df = paper_order.get_paper_orders()
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@orders_api.get('/get_by_orderid')
def get_by_orderid_orders_api(order_id: str):
    global paper_order

    df = paper_order.get_orderHistory_orders(order_id=order_id)
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@orders_api.get('/get_by_datetime')
def get_by_datetime_orders_api(sdate: str, edate: str, status: str):
    global paper_order

    df = paper_order.get_list_orders(sdate=sdate, edate=edate, status=status)
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@orders_api.put('/update_status')
def update_status_orders_api(status: str, order_id: str):
    global paper_order

    ret = paper_order.update_order_status_orders(
        status=status, order_id=order_id)
    return ret


@orders_api.put('/update_stoploss_price')
def update_stoploss_price_orders_api(stoploss_trigger_price, order_id):
    global paper_order

    ret = paper_order.update_SLtrigger_price_orders(
        stoploss_trigger=stoploss_trigger_price, order_id=order_id)
    return ret


@orders_api.put('/update_complete_order')
def update_complete_orders_api(order_id, price):
    global paper_order

    ret = paper_order.update_complete_orders(order_id=order_id, price=price)
    return ret


@orders_api.delete('/delete_by_orderid')
def delete_by_orderid_orders_api(order_id: str):
    global paper_order

    ret = paper_order.delete_orderHistory_orders(order_id=order_id)
    return ret


@orders_api.delete('/delete_by_datetime')
def delete_by_datetime_orders_api(sdate: str, edate: str, status: str):
    global paper_order

    ret = paper_order.delete_list_orders(
        sdate=sdate, edate=edate, status=status)
    return ret
