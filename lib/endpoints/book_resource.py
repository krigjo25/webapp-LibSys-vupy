#  Book's endpoint

#   Importing required dependencies
import uuid as ID

#   Importing  required dependencies
from core_files import app, db
from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
#   Importing custom libraries
from backend.lib.modal.db_init import Book
from backend.lib.config.log_config import MethodWatcher
from backend.lib.utils.maintance import UtilityTools

#   Loading environment variables
load_dotenv()

logger = MethodWatcher()
logger.FileHandler()

class BookMananger(MethodView):

    def __init__(self, *args, **kwargs):

        #   Initialize the logger
        self.orgins = '*'
        
        with app.app_context():
            self.books = Book().query.all()

        self.logger = logger
        self.tool = UtilityTools()
        self.BOOKS = [book.ConvertToDict() for book in self.books]

    def get(self):

        #   Ensure that the request method is GET
        if request.method == 'GET':
            response = self.response(books=self.BOOKS)
            return response

        response = self.response(405, message="Method not allowed")
        self.logger.error(f"Headers : {request.headers}\n Error : {response['message']} \n Status : {response['status']} Method : {request.method}")
        return response
        
    
    def post(self):

        #  Fetch the requested data
        data = request.get_json()

        #   Log the data which is retrieved
        self.logger.warn(f"Data retrieved")

        for key, value in data.items():
            self.logger.info(f"{key} : {value}")
        self.logger.warn(f"END OF LIST")

        #   Ensure that the request method is POST
        if request.method == 'POST':

            #   Ensure that the data is not None
            if data is None: 
                self.logger.error(f"{request.headers} | {request.method}")
                response = self.response(500)
                return response

            #   Initialize a new book object
            
            book = Book()
            for key, value in data.items():

                #   Ensure the integerty for the value, and book
                if value is not None and hasattr(book, key) and key != 'id':
                    
                    
                    setattr(book, key, value)

            try:
                #   Commit the changes to the database
                db.session.add(book)
                db.session.commit()

            except IntegrityError as e:
                self.logger.error(f"Error : {e}")
                return self.response(405, message="Already exists within the database")

            response = self.response(201)

        else:
            response = self.response(405)

        return response
    
    def put(self, BID):

        review = 'reviewers'
        seperator = ','
        #   Ensure that the request method is PUT (Update)

        if request.method == 'PUT':

            #   fetch the current book
            book = Book().query.get(BID)
            #   Initialize the response and fetch the request data
            
            data = request.get_json()

            
            #   Update the book object
            for key, value in data.items():

                #   Ensure the integerty for the value, and book
                if value is not None and hasattr(book, key) and key != 'id':

                    #   Ensure the key is reviewers
                    if key == "reviewers":
                        
                        review = str(value).split(seperator)
                        self.logger.info(f"Data retrieved test: {review} ")
                        setattr(book, 'rating', review[1])
                        setattr(book, 'reviewers', review[0])

                    setattr(book, key, value)

                db.session.commit()
            
            #   Success response
            self.logger.info(f"Data retrieved: {data} ")
            response = self.response(200, books = self.BOOKS)
            

        else:
            response = self.response(500)
            self.logger.error(f"Status : {response['code']} Method : {request.method} Headers : {request.headers}")

        return response

    def delete(self, BID):
        
        #   Ensure that the request method is DELETE
        if request.method == 'DELETE' and BID is not None:
                
                self.tool.Purge(BID)
                response = self.response(200, BID)


        else:
            response = self.response(405)

        return response

    def response(self, status:int = 200, message:Optional[str] = None, BID:Optional[str] = None, books:Optional[List] = None):

        response = {}

        match (status):

            #   Request successful
            case 200:
                response['books'] = books
                response['status'] = status

                if not message:
                    response['message'] = "The operation was sucssessfull !"
    
                if not books:
                    response['message'] = "Books was not found !"

                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | response : {response}")

            case 201:

                response['status'] = status
                if not message:
                    response['message'] = "Successfully added a new entry to the database."

                self.logger.error(f"\tMethod : {request.method} | Book ID : {BID}")
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
                    response['message'] = "An error occured while attempting to process the request"
                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | Book ID : {BID}")




        return jsonify(response)