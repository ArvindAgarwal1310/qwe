from .paperHolding import *

from fastapi import APIRouter
from pydantic import BaseModel
import json

paperHolding_api = APIRouter(prefix='/holding', tags=['holding'])
paper_holding = PaperHolding(r'databaseManagement\holding\holdingDatabase.db')


@paperHolding_api.post('/insert')
def insert_position(userid='XYZ123',
                    tradingsymbol='NIFTYFUT',
                    exchange='NFO',
                    product='FUT',
                    quantity=50,
                    average_price=18019.5,
                    last_price=18100.5):
    global paper_holding

    ret = paper_holding.insert_holding_paper(userid=userid, tradingsymbol=tradingsymbol, exchange=exchange,
                                             product=product, quantity=quantity, average_price=average_price, last_price=last_price)
    return ret


@paperHolding_api.get('/get')
def get_position():
    global paper_holding

    df = paper_holding.get_holding_paper()
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@paperHolding_api.get('/get_by_tradingsymbol')
def get_position_by_tradingsymbol(tradingsymbol):
    global paper_holding

    df = paper_holding.get_holding_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@paperHolding_api.put('/update')
def update_position(quantity, average_price, last_price, tradingsymbol):
    global paper_holding

    ret = paper_holding.update_holding_paper(
        quantity=quantity, average_price=average_price, last_price=last_price, tradingsymbol=tradingsymbol)
    return ret


@paperHolding_api.put('/update_quantity')
def update_position(tradingsymbol, quantity, t1_quantity=0, realised_quantity=0, used_quantity=0, collateral_quantity=0):
    global paper_holding

    ret = paper_holding.update_quantity_holding_paper(tradingsymbol=tradingsymbol, quantity=quantity, t1_quantity=t1_quantity,
                                                      realised_quantity=realised_quantity, used_quantity=used_quantity, collateral_quantity=collateral_quantity)
    return ret


@paperHolding_api.delete('/delete_by_tradingsymbol')
def delete_position_by_tradingsymbol(tradingsymbol):
    global paper_holding

    ret = paper_holding.delete_holding_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)
    return ret
