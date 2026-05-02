#   Utility tools for the application

#   Import the necessary dependencies
import uuid as ID
from typing import Optional

from core_files import app, db
from lib.modal.db_init import Book
from lib.config.log_config import UtilityWatcher


log = UtilityWatcher()
log.FileHandler()

class UtilityTools(object):

    def __init__(self):

        #   Initializing the logger
        self.log = log

    def Check(self, BID: str) -> bool:
    
        """
            *  Ensure that the element exists in the database

            param: BID
            return: True or False
        """
        book = Book.query.get(BID)
        if book:
            self.log.info(f"Book with ID: {BID} exists in the database.")
            return True

        self.log.warn(f"Book with ID: {BID} does not exist in the database.")
        return False

    def Purge(self, BID: str) -> str:
        """
            *  Delete the book from the database

            param: BID
            return: Status message
        """
        book = Book.query.get(BID)

        #   Ensure that the element exists
        if book:
            db.session.add(book) # Just to be sure it's in the session if needed, but query.get usually attaches it
            db.session.delete(book)
            db.session.commit()
            return "Book Deleted Successfully"

        return "Book was not found in the database"
    
