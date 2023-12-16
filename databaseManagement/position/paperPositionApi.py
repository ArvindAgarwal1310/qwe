from .paperPosition import *

from fastapi import APIRouter
import json

paperPosition_api = APIRouter(prefix='/position', tags=['position'])
paper_position = PaperPosition(
    'databaseManagement\position\positionDatabase.db')


@paperPosition_api.post('/insert')
def insert_position(userid='XYZ123',
                    tradingsymbol='NIFTYFUT',
                    exchange='NFO',
                    product='FUT',
                    quantity=50,
                    average_price=18019.5,
                    last_price=18100.5,):
    global paper_position

    ret = paper_position.insert_position_paper(userid=userid, tradingsymbol=tradingsymbol, exchange=exchange,
                                               product=product, quantity=quantity, average_price=average_price, last_price=last_price)
    return ret

@paperPosition_api.get('/get')
def get_position():
    global paper_position

    df = paper_position.get_positions_paper()
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@paperPosition_api.get('/get_by_tradingsymbol')
def get_position_by_tradingsymbol(tradingsymbol):
    global paper_position

    df = paper_position.get_positions_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)
    try:
        ret = df.copy()
        res = ret.to_json(orient="records")
        parsed = json.loads(res)
        return parsed
    except:
        return df


@paperPosition_api.put('/update')
def update_position(quantity, average_price, last_price, tradingsymbol):
    global paper_position

    ret = paper_position.update_position_paper(
        quantity=quantity, average_price=average_price, last_price=last_price, tradingsymbol=tradingsymbol)
    return ret


@paperPosition_api.put('/updateMarginAndM2M')
def update_position_margin(tradingsymbol, margin_required, m2m):
    global paper_position

    ret = paper_position.update_position_margin(
        tradingsymbol=tradingsymbol, margin_required=margin_required, m2m=m2m)
    return ret


@paperPosition_api.delete('/delte_by_tradingsymbol')
def delete_position_by_tradingsymbol(tradingsymbol):
    global paper_position

    ret = paper_position.delete_positions_by_tradingsymbol_paper(
        tradingsymbol=tradingsymbol)
    return ret
