#   Importing Standard Libraries
import uuid as ID
from typing import List, Optional

#   Importing Third-party Libraries
from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request, Response
from sqlalchemy.exc import IntegrityError

load_dotenv()

#   Importing Internal Libraries
from core_files import app, db
from lib.modal.db_init import Book
from lib.config.log_config import MethodWatcher
from lib.utils.maintenance import UtilityTools


logger = MethodWatcher()
logger.FileHandler()

class BookManager(MethodView):

    def __init__(self, *args, **kwargs):

        #   Initialize the logger
        self.origins = '*'
        
        self.logger = logger
        self.tool = UtilityTools()

    def get(self) -> Response:
        books = Book.query.all()
        books_dict = [book.ConvertToDict() for book in books]
        return self.response(books=books_dict)
    
    def post(self) -> Response:

        #  Fetch the requested data
        data = request.get_json()

        #   Log the data which is retrieved
        self.logger.warn(f"Data retrieved")

        if data:
            for key, value in data.items():
                self.logger.info(f"{key} : {value}")
        self.logger.warn(f"END OF LIST")

        #   Ensure that the data is not None
        if data is None: 
            self.logger.error(f"{request.headers} | {request.method}")
            return self.response(500)

        #   Initialize a new book object
        
        book = Book()
        for key, value in data.items():

            #   Ensure the integrity for the value, and book
            if value is not None and hasattr(book, key) and key != 'id':
                setattr(book, key, value)

        try:
            #   Commit the changes to the database
            db.session.add(book)
            db.session.commit()

        except IntegrityError as e:
            self.logger.error(f"Error : {e}")
            return self.response(405, message="Already exists within the database")

        return self.response(201)
    
    def put(self, BID: str) -> Response:

        separator = ','
        
        #   fetch the current book
        book = Book.query.get(BID)
        if not book:
            return self.response(404, BID=BID)

        #   Initialize the response and fetch the request data
        data = request.get_json()
        if not data:
            return self.response(405, message="No data provided")

        
        #   Update the book object
        for key, value in data.items():

            #   Ensure the integrity for the value, and book
            if value is not None and hasattr(book, key) and key != 'id':

                #   Ensure the key is reviewers
                if key == "reviewers":
                    
                    review_parts = str(value).split(separator)
                    self.logger.info(f"Data retrieved test: {review_parts} ")
                    if len(review_parts) > 1:
                        setattr(book, 'rating', review_parts[1])
                        setattr(book, 'reviewers', review_parts[0])

                setattr(book, key, value)

        db.session.commit()
        
        #   Success response
        self.logger.info(f"Data retrieved: {data} ")
        books = Book.query.all()
        books_dict = [book.ConvertToDict() for book in books]
        return self.response(200, books=books_dict)

    def delete(self, BID: str) -> Response:
        
        if BID is not None:
            self.tool.Purge(BID)
            return self.response(200, BID=BID)

        return self.response(405)

    def response(self, status: int = 200, message: Optional[str] = None, BID: Optional[str] = None, books: Optional[List] = None) -> Response:

        response = {}

        match (status):

            #   Request successful
            case 200:
                response['books'] = books
                response['status'] = status

                if not message:
                    response['message'] = "The operation was successful !"
    
                if not books and status == 200 and request.method == 'GET':
                    response['message'] = "Books was not found !"

                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | response : {response}")

            case 201:

                response['status'] = status
                if not message:
                    response['message'] = "Successfully added a new entry to the database."

                self.logger.warn(f"\tMethod : {request.method} | Book ID : {BID}")
            #   Not Found
            case 404:
                response['status'] = status
                if not message:
                    response['message'] = "Checked everywhere, the book was not found."

                self.logger.error(f"\tMethod : {request.method} | Book ID : {BID}")

            #   Method not allowed
            case 405:
                response['status'] = status
                if not message:

                    response['message'] = "Something smells fishy, ensure the request method is correct."
                
                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | Book ID : {BID}")
            case 500:
                response['status'] = status

                if not message:
                    response['message'] = "An error occurred while attempting to process the request"
                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | Book ID : {BID}")

        return jsonify(response)