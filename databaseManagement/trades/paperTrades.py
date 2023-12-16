import sqlite3
import pandas as pd


class PaperTrade:
    def __init__(self, DatabaseName: str):
        '''
        DatabaseName (str): Name of the database (e.g. paperDatabase.db)
        '''

        try:
            # Connect to DB and create a cursor
            self.sqliteConnection = sqlite3.connect(
                DatabaseName, check_same_thread=False)
            self.cursor = self.sqliteConnection.cursor()

            # create table
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS paper_trades (
            `userid` varchar(45) DEFAULT NULL,
            `trade_id` INTEGER PRIMARY KEY NOT NULL,
            `order_id` int DEFAULT NULL,
            `tradingsymbol` varchar(45) DEFAULT NULL,
            `exchange` varchar(45) DEFAULT NULL,
            `average_price` decimal(18,2) DEFAULT NULL,
            `quantity` int DEFAULT NULL,
            `transaction_type` varchar(45) DEFAULT NULL,
            `timestamp` datetime DEFAULT NULL
            )''')

            self.sqliteConnection.commit()

        except Exception as e:
            exit(print(f'{e}: while connting to the {DatabaseName}!'))

    def insert_trade(self, tradeid, userid, order_id, exchange, tradingsymbol, average_price, quantity, transaction_type, timestamp):
        try:
            query = "INSERT INTO paper_trades(userid, trade_id, order_id, exchange, tradingsymbol, average_price, quantity, transaction_type, timestamp)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(userid,
                                                                                                                                                                                                                     tradeid, order_id, exchange, tradingsymbol, average_price, quantity, transaction_type, timestamp)
            cur = self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return {"Success": "Inserted Successfully"}
        except Exception as e:
            return {"Error": f"{e}"}

    def GetTradeByDate(self, startdate, enddate):
        try:
            query = "Select * from paper_trades where timestamp between '{}' and '{}'".format(
                startdate, enddate)
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {"Error": f"{e}"}

    def GetTradeByOrderID(self, order_id):
        try:
            query = "SELECT average_price, timestamp as exchange_timestamp, tradingsymbol FROM paper_trades where order_id = '{}'".format(
                order_id)
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {"Error": f"{e}"}

    def getTrade(self):
        try:
            query = "Select * from paper_trades"
            df = pd.read_sql(query, self.sqliteConnection)
            return df
        except Exception as e:
            return {"Error": f"{e}"}

    def deleteTradeByDate(self, startdate, enddate):
        try:
            query = "Delete from paper_trades where timestamp between '{}' and '{}'".format(
                startdate, enddate)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {"Error": f"{e}"}

    def deleteTradeByOrderID(self, order_id):
        try:
            query = "Delete FROM paper_trades where order_id = '{}'".format(
                order_id)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {"Error": f"{e}"}
