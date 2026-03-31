#   Python Libraries
import sys
from typing import List

#   Third-party Libraries
import mariadb
from dotenv import load_dotenv
load_dotenv()

#   Selecting, Inserting or updates a table
class MariaDB:

    '''         mariaDB

        Connects to the preferably used database from
        mariaDB. with Commands, such as SELECT, INSERT,
        UPDATE, CREATE DATABASE, CREATE TABLE
                
        the function also calls a procedure and a function.
    '''

    def __init__(self) -> None:
        try:
            self.conn: mariadb.Connection = mariadb.connect(
                host=getenv('H0ST'),
                user=getenv('MASTER'),
                port=int(getenv('PORT')),
                password=getenv('PASSWORD'),
                database=getenv('database')
            )
            self.cur: mariadb.Cursor = self.conn.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to the database: \n {e}")
            sys.exit(1)

    def close_connection(self) -> None:
        self.conn.close()

    def select_from_table(self, database: str, query: str) -> List[List[str]]:
        self.conn.database = database
        self.cur.execute(query)
        sql = self.cur.fetchall()
        sql_data: List[List[str]] = [list(i) for i in sql]
        return sql_data

    def row_count(self, database: str, query: str) -> int:
        self.conn.database = database
        self.cur.execute(query)

        self.cur.fetchall()

        return self.cur.rowcount()

    def update_table (self, database, query):

        #   Database selection
        self.conn.database = database

        self.database = database

        #   Executes the query and close the connection

        self.cur.execute(query)
        self.conn.close()

        return

    def call_procedure (self, database, query):

        #   Database Connection 
        self.conn.database = database

        #   calling a procedure
        self.cur.callproc(f'{query}')

        return

    def create_database(self, name:str) -> None:

        query:str = f'CREATE DATABASE IF NOT EXISTS {name}'
        self.cur.execute(query)
        self.conn.database = name

        msg:str = ''
        if self.conn == True: msg = f'{name}, were successfully created'
        else: msg = ' An error occurred'

        return

    def drop_database(self, name:str) -> None:

        query:str = f'DROP DATABASE IF NOT EXISTS {name}'
        self.cur.execute(query)

        msg:str = ''
        if self.conn == False: msg = f'{name}, were successfully deleted'
        else: msg = ' An error occurred'

        return

    def drop_table(self, database:str, name:str) -> None:

        self.conn.database = database

        query:str = f'DROP TABLE IF EXISTS {name};'
        self.cur.execute(query)
        return