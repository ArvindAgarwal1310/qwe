import sqlite3
import pandas as pd


class PaperHolding:
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
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS paper_holding (
            `userid` varchar(45) DEFAULT NULL,
            `tradingsymbol` varchar(45) DEFAULT NULL,
            `exchange` varchar(45) DEFAULT NULL,
            `product` varchar(45) DEFAULT NULL,
            `quantity` int DEFAULT NULL,
            `t1_quantity` int DEFAULT NULL,
            `realised_quantity` int DEFAULT NULL,
            `used_quantity` int DEFAULT NULL,
            `collateral_quantity` int DEFAULT NULL,
            `average_price` decimal(18,2) DEFAULT NULL,
            `last_price` decimal(18,2) DEFAULT NULL,
            `pnl` decimal(18,2) DEFAULT NULL
            )''')
            self.sqliteConnection.commit()

        except Exception as e:
            exit(print(f'{e}: while connting to the {DatabaseName}!'))

    def insert_holding_paper(self, userid, tradingsymbol, exchange, product, quantity, average_price, last_price, t1_quantity=0, realised_quantity=0, used_quantity=0, collateral_quantity=0):
        try:
            pnl = float(quantity)*(float(last_price)-float(average_price))
            query = "INSERT INTO paper_holding(userid, tradingsymbol, exchange, product, quantity, average_price, last_price, pnl, t1_quantity, realised_quantity, used_quantity, collateral_quantity) VALUES('{}','{}','{}','{}','{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                userid, tradingsymbol, exchange, product, quantity, average_price, last_price, pnl, t1_quantity, realised_quantity, used_quantity, collateral_quantity)
            cur = self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return {"Success": "Data inserted successfully!"}
        except Exception as e:
            return {'Error': f"{e}, while inserting data!"}

    def get_holding_paper(self):
        try:
            query = "SELECT * FROM paper_holding".format()
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {"Error": f"{e}, while fetching data!"}

    def get_holding_by_tradingsymbol_paper(self, tradingsymbol):
        try:
            query = "SELECT * FROM paper_holding where tradingsymbol = '{}'".format(
                tradingsymbol)
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {'Error': f"{e}"}

    def update_holding_paper(self, quantity, average_price, last_price, tradingsymbol):
        try:
            pnl = float(quantity)*(float(last_price)-float(average_price))
            query = "Update paper_holding set quantity = '{}', average_price = '{}', last_price = '{}', pnl='{}' where tradingsymbol = '{}'".format(
                quantity, average_price, last_price, pnl, tradingsymbol)
            cur = self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return {"Sucess": "Holding updated!"}
        except Exception as e:
            return {'Error': f"{e}"}

    def update_quantity_holding_paper(self, tradingsymbol, quantity, t1_quantity=0, realised_quantity=0, used_quantity=0, collateral_quantity=0):
        try:
            query = f"Update paper_holding set quantity='{quantity}', t1_quantity='{t1_quantity}', realised_quantity='{realised_quantity}', used_quantity='{used_quantity}', collateral_quantity='{collateral_quantity}' where tradingsymbol='{tradingsymbol}'"
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {"Success": "Holding quantity updated!"}
        except Exception as e:
            return {"Error": f"{e}"}

    def delete_holding_by_tradingsymbol_paper(self, tradingsymbol):
        try:
            query = "DELETE FROM paper_holding where tradingsymbol = '{}'".format(
                tradingsymbol)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {"Success": "Deleted Successfully"}
        except Exception as e:
            return {'Error': f"{e}"}
