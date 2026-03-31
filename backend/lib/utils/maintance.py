#   Utility tools for the application

#   Import the necessary dependencies
import uuid as ID

from core_files import app, db
from lib.modal.db_init import Book
from lib.config.log_config import UtilityWatcher


log = UtilityWatcher()
log.FileHandler()

class UtilityTools(object):

    def __init__(self):

        #   Initializing the logger
        self.log = log

    def Check(self, BID:str):
    
        """
            *  Ensure that the element exists in the dictionary

            param: ID, Argument
            param: ID
            return: True or False
        """
            
        for book in self.books:

            #   Ensure that the element exists in the dictionary
            if book['id'] == BID:

                self.log.info(f"Book with ID: {BID} exists in the dictionary.")
                return True

            self.log.warn(f"Book with ID: {BID} does not exist in the dictionary.")
        return False

    def Purge(self, ID:str):
        """
            *  Delete the book from the dictionary

            param: BID
            return: None
        """
        book = Book().query.get(ID)

        #   Ensure that the element exists in the dictionary
        if book:
            db.session.delete(book)
            db.session.commit()
            return "Book Deleted Successfully"

        return "Book was not found in the dictionary"
    
