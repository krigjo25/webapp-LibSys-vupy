#   Python Libraries
import datetime as dt
from os import getenv
from typing import Dict, List, Any

#   Third-party Libraries
from dotenv import load_dotenv

#   Internal Libraries
from core_files import db
from lib.modal.db_init import Book
from .database_connection import MariaDB

load_dotenv()

class UtilityTools:

    def __init__(self):
        #   Initialize the logger
        pass

    def Purge(self, BID: str) -> None:

        book = Book.query.get(BID)

        if book:
            db.session.delete(book)
            db.session.commit()
            print(f"Purged: {BID}")
        else:
            print(f"Book not found: {BID}")

    def Maintenance(self) -> None:
        pass
