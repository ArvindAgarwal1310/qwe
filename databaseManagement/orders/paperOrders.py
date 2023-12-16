import sqlite3
import pandas as pd


class PaperOrders:
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
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS paper_orders (
            `userid` varchar(45) DEFAULT NULL,
            `order_id` INTEGER PRIMARY KEY NOT NULL,
            `tradingsymbol` varchar(45) DEFAULT NULL,
            `quantity` decimal(18,2) DEFAULT NULL,
            `exchange` varchar(45) DEFAULT NULL,
            `transaction_type` varchar(45) DEFAULT NULL,
            `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `product` varchar(45) DEFAULT NULL,
            `order_type` varchar(45) DEFAULT NULL,
            `price` decimal(18,2) DEFAULT NULL,
            `stoploss_trigger_price` decimal(18,2) DEFAULT NULL,
            `status` varchar(45) DEFAULT NULL,
            `intent` varchar(45) DEFAULT 'FRESH',
            `StopLossStatus` varchar(45) DEFAULT 'None',
            `remarks` varchar(45) DEFAULT NULL
            )''')
            self.sqliteConnection.commit()

        except Exception as e:
            exit(print(f'{e}: while connting to the {DatabaseName}!'))

    def insert_paper_orders(self, userid, order_id, trading_symbol, qty, exchange, trans_type, timestamp, product, order_type, price, stoploss_trigger, status):
        try:
            query = "INSERT INTO paper_orders(userid, order_id, tradingsymbol, quantity, exchange, transaction_type, timestamp, product, order_type, price, stoploss_trigger_price, status) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                userid, order_id, trading_symbol, qty, exchange, trans_type, timestamp, product, order_type, price, stoploss_trigger, status)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {'Success': "Inserted succefully!"}
        except Exception as e:
            return {'Error': f"{e}, while inserting data!!"}

    def get_paper_orders(self):
        try:
            query = "SELECT * FROM paper_orders"
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {'Error': f"{e}, while fetching data"}

    def update_SLtrigger_price_orders(self, stoploss_trigger, order_id):
        try:
            query = "Update paper_orders set stoploss_trigger_price = '{}' where order_id = '{}'".format(
                stoploss_trigger, order_id)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {'Success': 'Sl Updated successfully'}
        except Exception as e:
            return {'Error': f"{e}, while updating SL"}

    def update_order_status_orders(self, status, order_id):
        try:
            query = "Update paper_orders set status = '{}' where order_id = '{}'".format(
                status, order_id)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {'Success': 'Order status updated!!'}
        except Exception as e:
            return {'Error': f'{e}, while updating order Status!!'}

    def update_complete_orders(self, order_id, price):
        try:
            query = "update paper_orders set status = 'COMPLETE', price = '{}' where order_id = '{}'".format(
                price, order_id)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {'Success': 'order Updated!'}
        except Exception as e:
            return {'Error': f'{e}, while updating order!'}

    def get_orderHistory_orders(self, order_id):
        try:
            query = "Select status, '' as status_message FROM paper_orders where order_id = '{}'".format(
                order_id)
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {'Error': f"{e}, while Fetching data!!"}

    def get_list_orders(self, sdate, edate, status):
        try:
            query = "Select order_id, tradingsymbol as instrument, exchange, quantity as qty, transaction_type from paper_orders where (timestamp between '{}' AND '{}') AND status = '{}'".format(
                sdate, edate, status)
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {"Error": f"{e}, while fetching data!!"}

    def delete_orderHistory_orders(self, order_id):
        try:
            query = "DELETE FROM paper_orders where order_id = '{}'".format(
                order_id)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {"Success": " Delete Successfully"}
        except Exception as e:
            return {'Error': f"{e}"}

    def delete_list_orders(self, sdate, edate, status):
        try:
            query = "DELETE from paper_orders where (timestamp between '{}' AND '{}') AND status = '{}'".format(
                sdate, edate, status)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {"Error": f"{e}"}
