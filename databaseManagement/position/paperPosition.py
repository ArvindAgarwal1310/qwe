import sqlite3
import pandas as pd


class PaperPosition:
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
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS paper_positions (
            `userid` varchar(45) DEFAULT NULL,
            `tradingsymbol` varchar(45) DEFAULT NULL,
            `exchange` varchar(45) DEFAULT NULL,
            `product` varchar(45) DEFAULT NULL,
            `quantity` int DEFAULT NULL,
            `average_price` decimal(18,2) DEFAULT NULL,
            `last_price` decimal(18,2) DEFAULT NULL,
            `margin_required` decimal (18,2) DEFAULT Null,
            `m2m` decimal(18,2) DEFAULT NULL
            )''')
            self.sqliteConnection.commit()

        except Exception as e:
            exit(print(f'{e}: while connting to the {DatabaseName}!'))

    def insert_position_paper(self, userid, tradingsymbol, exchange, product, quantity, average_price, last_price):
        try:
            query = "INSERT INTO paper_positions(userid, tradingsymbol, exchange, product, quantity, average_price, last_price) VALUES('{}','{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                userid, tradingsymbol, exchange, product, quantity, average_price, last_price)
            cur = self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return {"Success": "Data inserted successfully!"}
        except Exception as e:
            return {'Error': f"{e}, while inserting data!"}

    def get_positions_paper(self):
        try:
            query = "SELECT * FROM paper_positions".format()
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {"Error": f"{e}, while fetching data!"}

    def get_positions_by_tradingsymbol_paper(self, tradingsymbol):
        try:
            query = "SELECT * FROM paper_positions where tradingsymbol = '{}'".format(
                tradingsymbol)
            df = pd.read_sql(query, con=self.sqliteConnection)
            return df
        except Exception as e:
            return {'Error': f"{e}"}

    def update_position_paper(self, quantity, average_price, last_price, tradingsymbol):
        try:
            query = "Update paper_positions set quantity = '{}', average_price = '{}', last_price = '{}' where tradingsymbol = '{}'".format(
                quantity, average_price, last_price, tradingsymbol)
            cur = self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return {"Sucess": "Positon updated!"}
        except Exception as e:
            return {'Error': f"{e}"}

    def update_position_margin(self, tradingsymbol, margin_required, m2m):
        try:
            query = "Update paper_positions set margin_required = '{}', m2m = '{}' where tradingsymbol = '{}'".format(
                margin_required, m2m, tradingsymbol)
            cur = self.sqliteConnection.cursor()
            cur.execute(query)
            self.sqliteConnection.commit()
            return {"Sucess": "Positon updated!"}
        except Exception as e:
            return {'Error': f"{e}"}

    def delete_positions_by_tradingsymbol_paper(self, tradingsymbol):
        try:
            query = "DELETE FROM paper_positions where tradingsymbol = '{}'".format(
                tradingsymbol)
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            return {"Sucess": "Deleted Successfully"}
        except Exception as e:
            return {'Error': f"{e}"}
