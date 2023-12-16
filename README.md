# PaperBrokerage

Api to store the order and trade related data.


## Installation
```
pip install paperBrokerage
```

## Usage
Api contains 5 tags:
1. Order
2. Order Group
3. Trade
4. Position
5. Price


### Order
It has 7 endpoints:

**1.Insert Data**
```
-Request: Post

-link: http://127.0.0.1:8000/orders/insert?userid=XYZ123&order_id=10223&tradingsymbol=NIFTYFUT&quantity=50&exchange=NFO&transaction_type=BUY&timestamp=08%2F11%2F2022+22%3A55t=FUT&order_type=MKT&price=18010.05&stoploss_trigger_price=17910.05&status=ACTIVE

-return: {
  "Success": "Inserted succefully!"
}

```

**2. Get All Data**
```
-Request: Get

-link: http://127.0.0.1:8000/orders/get

-return: [
  {
    "userid": "XYZ123",
    "order_id": 10223,
    "tradingsymbol": "NIFTYFUT",
    "quantity": 50,
    "exchange": "NFO",
    "transaction_type": "BUY",
    "timestamp": "06/11/2022|13:59:46",
    "product": "FUT",
    "order_type": "MKT",
    "price": 18010.05,
    "stoploss_trigger_price": 17910.05,
    "status": "ACTIVE",
    "intent": "FRESH",
    "StopLossStatus": "None",
    "remarks": null
  }
]

```

**3. Get Data Status By OrderId**
```
-Request: Get

-link: http://127.0.0.1:8000/orders/get_by_orderid?orderid=10223
-return:[
  {
    "status": "ACTIVE",
    "status_message": ""
  }
]

```

**4. Get Data by Datetime**
```
-Request: Get

-link: http://127.0.0.1:8000/orders/get_by_datetime?sdate=08%2F11%2F2022+22%3A55&edate=08%2F11%2F2022+22%3A55&status=ACTIVE

-return: [
  {
    "order_id": 10223,
    "instrument": "NIFTYFUT",
    "exchange": "NFO",
    "qty": 50,
    "transaction_type": "BUY"
  }
]

```

**5. Update Order Status**
```
-Request: Put

-link: http://127.0.0.1:8000/orders/update_status?status=COMPLETE&order_id=10223

-return: {
  "Success": "Order status updated!!"
}
```

**6. Update Stoploss Price**
```
-Request: Put

-link: http://127.0.0.1:8000/orders/update_stoploss_price?stoploss_trigger_price=17920.05&order_id=10223

-return: {
  "Success": "Sl Updated successfully"
}

```

**7. Update Order Price**
```
-Request: Put

-link: http://127.0.0.1:8000/orders/update_complete_order?order_id=10223&price=18011.05

-return: {
  "Success": "order Updated!"
}

```


### Order Group
It has 7 endpoints:

**1.Insert Data**
```
-Request: Post

-link: http://127.0.0.1:8000/orderGroups/insert?userid=XYZ123&order_id=10223&tradingsymbolOne=NIFTYFUT&tradingsymbolTwo=NIFTYFUT&tradingsymbolThree=NIFTYFUT&tradingsymbolFour=NIFTYFUT&quantityOne=50&quantityTwo=50&quantityThree=50&quantityFour=50&exchange=NFO&transaction_typeOne=BUY&transaction_typeTwo=BUY&transaction_typeThree=BUY&transaction_typeFour=BUY&timestamp=08%2F11%2F2022+22%3A55&product=FUT&order_typeOne=MKT&order_typeTwo=MKT&order_typeThree=MKT&order_typeFour=MKT&priceOne=18010.05&priceTwo=18010.05&priceThree=18010.05&priceFour=18010.05&stoploss_trigger_priceOne=17910.05&stoploss_trigger_priceTwo=17910.05&stoploss_trigger_priceThree=17910.05&stoploss_trigger_priceFour=17910.05&status=ACTIVE

-return: {
  "Success": "Inserted data successfully"
}

```

**2. Get All Data**
```
-Request: Get

-link: http://127.0.0.1:8000/orderGroups/get

-return: [
  {
    "userid": "XYZ123",
    "order_id": 10223,
    "tradingsymbolOne": "NIFTYFUT",
    "tradingsymbolTwo": "NIFTYFUT",
    "tradingsymbolThree": "NIFTYFUT",
    "tradingsymbolFour": "NIFTYFUT",
    "quantityOne": 50,
    "quantityTwo": 50,
    "quantityThree": 50,
    "quantityFour": 50,
    "exchange": "NFO",
    "transaction_typeOne": "BUY",
    "transaction_typeTwo": "BUY",
    "transaction_typeThree": "BUY",
    "transaction_typeFour": "BUY",
    "timestamp": "06/11/2022|14:50:11",
    "product": "FUT",
    "order_typeOne": "MKT",
    "order_typeTwo": "MKT",
    "order_typeThree": "MKT",
    "order_typeFour": "MKT",
    "priceOne": 18010.05,
    "priceTwo": 18010.05,
    "priceThree": 18010.05,
    "priceFour": 18010.05,
    "stoploss_trigger_priceOne": 17910.05,
    "stoploss_trigger_priceTwo": 17910.05,
    "stoploss_trigger_priceThree": 17910.05,
    "stoploss_trigger_priceFour": 17910.05,
    "status": "ACTIVE",
    "intent": "FRESH",
    "StopLossStatus": "None",
    "remarks": null
  }
]

```

**3. Get Data Status By OrderId**
```
-Request: Get

-link: http://127.0.0.1:8000/orderGroups/get_by_orderid?orderid=10223

-return:[
  {
    "status": "ACTIVE",
    "status_message": ""
  }
]

```

**4. Get Data by Datetime**
```
-Request: Get

-link: http://127.0.0.1:8000/orderGroups/get_by_datetime?sdate=08%2F11%2F2022+22%3A55&edate=08%2F11%2F2022+22%3A55&status=ACTIVE

-return: [
  {
    "userid": "XYZ123",
    "order_id": 10223,
    "tradingsymbolOne": "NIFTYFUT",
    "tradingsymbolTwo": "NIFTYFUT",
    "tradingsymbolThree": "NIFTYFUT",
    "tradingsymbolFour": "NIFTYFUT",
    "quantityOne": 50,
    "quantityTwo": 50,
    "quantityThree": 50,
    "quantityFour": 50,
    "exchange": "NFO",
    "transaction_typeOne": "BUY",
    "transaction_typeTwo": "BUY",
    "transaction_typeThree": "BUY",
    "transaction_typeFour": "BUY",
    "timestamp": "06/11/2022|14:50:11",
    "product": "FUT",
    "order_typeOne": "MKT",
    "order_typeTwo": "MKT",
    "order_typeThree": "MKT",
    "order_typeFour": "MKT",
    "priceOne": 18010.05,
    "priceTwo": 18010.05,
    "priceThree": 18010.05,
    "priceFour": 18010.05,
    "stoploss_trigger_priceOne": 17910.05,
    "stoploss_trigger_priceTwo": 17910.05,
    "stoploss_trigger_priceThree": 17910.05,
    "stoploss_trigger_priceFour": 17910.05,
    "status": "ACTIVE",
    "intent": "FRESH",
    "StopLossStatus": "None",
    "remarks": null
  }
]

```

**5. Update Order Status**
```
-Request: Put

-link: http://127.0.0.1:8000/orderGroups/update_status?status=COMPLETED&order_id=10223

-return: {
  "Success": "Order status updated!!"
}
```

**6. Update Stoploss Price**
```
-Request: Put

-link: http://127.0.0.1:8000/orderGroups/update_stoploss_price?stoploss_trigger_priceOne=17920&stoploss_trigger_priceTwo=17930&stoploss_trigger_priceThree=17940&stoploss_trigger_priceFour=17950&order_id=10223

-return: {
  "Success": "StopLoss Updated!!"
}

```

**7. Update Order Price**
```
-Request: Put

-link: http://127.0.0.1:8000/orderGroups/update_complete_order?orderid=10223&priceOne=18011&priceTwo=18012&priceThree=18013&priceFour=18014

-return: {
  "Success": "order Updated!"
}
```


### Trade
It has 4 endpoints:

**1.Insert Data**

```
-Request: Post

-link: http://127.0.0.1:8000/trades/insert?userid=XYZ123&trade_id=01091&order_id=10911&tradingsymbol=NIFTYFUT&exchange=NFO&average_price=18019.5&quantity=50&transaction_type=BUY&timestamp=08%2F11%2F2022+22%3A55

-return: {
  "Success": "Inserted Successfully"
}

```

**2. Get All Data**

```
-Request: Get

-link: http://127.0.0.1:8000/trades/get

-return: [
  {
    "userid": "XYZ123",
    "trade_id": 1,
    "order_id": 10911,
    "tradingsymbol": "NIFTYFUT",
    "exchange": "NFO",
    "average_price": 18019.5,
    "quantity": 50,
    "transaction_type": "BUY",
    "timestamp": "06/11/2022|14:53:19"
  }
]

```

**3. Get Data Status By OrderId**

```
-Request: Get

-link: http://127.0.0.1:8000/trades/get_by_orderid?orderid=10911

-return:[
  {
    "average_price": 18019.5,
    "exchange_timestamp": "06/11/2022|14:53:19",
    "tradingsymbol": "NIFTYFUT"
  }
]

```

**4. Get Data by Datetime**

```
-Request: Get

-link: http://127.0.0.1:8000/trades/get_by_datetime?startdate=06%2F11%2F2022%7C14%3A53%3A19&enddate=06%2F11%2F2022%7C14%3A53%3A19

-return: [
  {
    "userid": "XYZ123",
    "trade_id": 1,
    "order_id": 10911,
    "tradingsymbol": "NIFTYFUT",
    "exchange": "NFO",
    "average_price": 18019.5,
    "quantity": 50,
    "transaction_type": "BUY",
    "timestamp": "06/11/2022|14:53:19"
  }
]
```

### Position
It has 4 endpoints:

**1.Insert Data**
```
-Request: Post

-link: http://127.0.0.1:8000/position/insert?userid=XYZ123&tradingsymbol=NIFTYFUT&exchange=NFO&product=FUT&quantity=50&average_price=18019.5&last_price=18100.5

-return: {
  "Success": "Data inserted successfully!"
}

```

**2. Get All Data**
```
-Request: Get

-link: http://127.0.0.1:8000/position/get

-return: [
  {
    "userid": "XYZ123",
    "tradingsymbol": "NIFTYFUT",
    "exchange": "NFO",
    "product": "FUT",
    "quantity": 50,
    "average_price": 18019.5,
    "last_price": 18100.5,
    "m2m": null
  }
]
```

**3. Get Data Status By TradingSymbol**
```
-Request: Get

-link: http://127.0.0.1:8000/position/get_by_tradingsymbol?tradingsymbol=NIFTYFUT

-return:[
  {
    "userid": "XYZ123",
    "tradingsymbol": "NIFTYFUT",
    "exchange": "NFO",
    "product": "FUT",
    "quantity": 50,
    "average_price": 18019.5,
    "last_price": 18100.5,
    "m2m": null
  }
]

```

**5. Update Position**
```
-Request: Put

-link: http://127.0.0.1:8000/position/update?quantity=100&average_price=18020&last_price=18150&tradingsymbol=NIFTYFUT

-return: {
  "Sucess": "Positon updated!"
}
```

### PRICE
We have only 3 instrument data base and of 3 timeframe:
1. SBIN (1m, 5m, 15m)
2. NIFTY (1m, 5m, 15m)
3. BTCUSD (1m, 5m, 15m)

It has 5 endpoints:

**1.Get spot price**
Returns Random price
```
-Request: get

-link: http://127.0.0.1:8000/paperPrice/getSpot?instrument=BANKNIFTY

-return: {
  "Instrument": "BANKNIFTY",
  "LTP": 2616.02,
  "Volumne": 881399.24
}

```

**2. Generate Price**
Generate Price Data

```
-Request: Get

-link: http://127.0.0.1:8000/paperPrice/generatePrice?instrument=SBIN&startPrice=500&volatility=0.001&timeframe=5Min

-return: [
  {
    "Datetime": "09:15",
    "Instrument": "SBIN",
    "Open": 496.94,
    "High": 532.7,
    "Low": 484.25,
    "Close": 500.48,
    "timeframe": "5Min"
  },
  {
    "Datetime": "09:20",
    "Instrument": "SBIN",
    "Open": 524.96,
    "High": 532.87,
    "Low": 482.61,
    "Close": 500.29,
    "timeframe": "5Min"
  }
]
```

**3. Get All Data**
```
-Request: Get

-link: http://127.0.0.1:8000/paperPrice/getHisData?instrument=SBIN&timeframe=5Min

-return: [
  {
    "Datetime": "2022-10-28 09:15:00",
    "Open": 579.950012207,
    "High": 580.950012207,
    "Low": 579.450012207,
    "Close": 579.549987793,
    "Adj Close": 579.549987793,
    "Volume": 0,
    "Instrument": "SBIN",
    "Timeframe": "1m"
  },
  {
    "Datetime": "2022-10-28 09:16:00",
    "Open": 579.6500244141,
    "High": 580,
    "Low": 578.1500244141,
    "Close": 578.1500244141,
    "Adj Close": 578.1500244141,
    "Volume": 95020,
    "Instrument": "SBIN",
    "Timeframe": "1m"
  }
]
```

**4. Get All data by DateTime**
```
-Request: Get

-link: http://127.0.0.1:8000/paperPrice/getDataByDate?instrument=SBIN&sdate=08%2F11%2F2022+22%3A5522&edate=08%2F11%2F2022+22%3A5522&timeframe=%221m%22

-return:[
  {
    "Datetime": "2022-10-28 10:14:00",
    "Open": 574.6500244141,
    "High": 575.8499755859,
    "Low": 574.6500244141,
    "Close": 575.8499755859,
    "Adj Close": 575.8499755859,
    "Volume": 44501,
    "Instrument": "SBIN",
    "Timeframe": "1m"
  },
  {
    "Datetime": "2022-10-28 10:15:00",
    "Open": 575.9000244141,
    "High": 576.3499755859,
    "Low": 575.450012207,
    "Close": 575.6500244141,
    "Adj Close": 575.6500244141,
    "Volume": 39475,
    "Instrument": "SBIN",
    "Timeframe": "1m"
  }
]

```

**5. Get All data by N**
```
-Request: Get

-link: http://127.0.0.1:8000/paperPrice/getDataByN?instrument=SBIN&n=10&timeframe=%221m%22

-return:[
  {
    "Datetime": "2022-10-28 09:15:00",
    "Open": 579.950012207,
    "High": 580.950012207,
    "Low": 579.450012207,
    "Close": 579.549987793,
    "Adj Close": 579.549987793,
    "Volume": 0,
    "Instrument": "SBIN",
    "Timeframe": "1m"
  },
  {
    "Datetime": "2022-10-28 09:16:00",
    "Open": 579.6500244141,
    "High": 580,
    "Low": 578.1500244141,
    "Close": 578.1500244141,
    "Adj Close": 578.1500244141,
    "Volume": 95020,
    "Instrument": "SBIN",
    "Timeframe": "1m"
  }
]

```

**6. Delete**
Delete data from database
```
-Request: Delete

-link: http://127.0.0.1:8000/paperPrice/delete?instrument=SBIN&timeframe=1Min

-return: {
  "Success": "Deleted Successfully"
}
```

**6. Delete By Datetime**
Delete data from database
```
-Request: Delete

-link: http://127.0.0.1:8000/paperPrice/deleteByDatetime?instrument=SBIN&sdate=08%2F11%2F2022+22%3A55me=5Min

-return: {
  "Success": "Deleted successfully"
}
```