#   Python Libraries
import sys
from typing import List, Any

#   Third-party Libraries
import mariadb # type: ignore (Library lacks type stubs)

#   Internal Libraries
from lib.config.env_config import settings

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
            self.conn = mariadb.connect( # type: ignore
                host=settings.H0ST,
                user=settings.MASTER,
                port=settings.PORT,
                password=settings.PASSWORD,
                database=settings.DATABASE
            )
            self.cur = self.conn.cursor() # type: ignore
        except mariadb.Error as e: # type: ignore
            print(f"Error connecting to the database: \n {e}")
            sys.exit(1)

    def close_connection(self) -> None:
        self.conn.close() # type: ignore

    def select_from_table(self, database: str, query: str) -> List[List[Any]]:
        self.conn.database = database # type: ignore
        self.cur.execute(query) # type: ignore
        sql = self.cur.fetchall() # type: ignore
        sql_data: List[List[Any]] = [list(i) for i in sql] # type: ignore
        return sql_data

    def row_count(self, database: str, query: str) -> int:
        self.conn.database = database # type: ignore
        self.cur.execute(query) # type: ignore

        self.cur.fetchall() # type: ignore

        return self.cur.rowcount() # type: ignore

    def update_table (self, database: str, query: str) -> None:

        #   Database selection
        self.conn.database = database # type: ignore

        #   Executes the query and close the connection

        self.cur.execute(query) # type: ignore
        self.conn.close() # type: ignore

        return

    def call_procedure (self, database: str, query: str) -> None:

        #   Database Connection 
        self.conn.database = database # type: ignore

        #   calling a procedure
        self.cur.callproc(f'{query}') # type: ignore

        return

    def create_database(self, name:str) -> None:

        query:str = f'CREATE DATABASE IF NOT EXISTS {name}'
        self.cur.execute(query) # type: ignore
        self.conn.database = name # type: ignore

        return

    def drop_database(self, name:str) -> None:

        query:str = f'DROP DATABASE IF NOT EXISTS {name}'
        self.cur.execute(query) # type: ignore

        return

    def drop_table(self, database:str, name:str) -> None:

        self.conn.database = database # type: ignore

        query:str = f'DROP TABLE IF EXISTS {name};'
        self.cur.execute(query) # type: ignore
        return
