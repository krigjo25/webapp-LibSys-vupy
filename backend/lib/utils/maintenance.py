#   Third-party Libraries
from dotenv import load_dotenv

#   Internal Libraries
from core_files import db # type: ignore (Library lacks type stubs)
from lib.modal.db_init import Book

load_dotenv()

class UtilityTools:

    def __init__(self):
        #   Initialize the logger
        pass

    def Purge(self, BID: str) -> None:

        book = Book.query.get(BID) # type: ignore (Library lacks type stubs)

        if book:
            db.session.delete(book) # type: ignore (Library lacks type stubs)
            db.session.commit() # type: ignore (Library lacks type stubs)
            print(f"Purged: {BID}")
        else:
            print(f"Book not found: {BID}")

    def Maintenance(self) -> None:
        pass
