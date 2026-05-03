# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false, reportUnknownArgumentType=false, reportCallIssue=false
# The above ignores are used because libraries like Flask, SQLAlchemy, and Pydantic 
# often have complex dynamic members that are difficult for Pylance to track without 
# extensive type stubs.

#   Importing Standard Libraries
from typing import List, Optional, Any

#   Importing Third-party Libraries
from dotenv import load_dotenv
from flask.views import MethodView
from flask import jsonify, request, Response
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError

load_dotenv()

#   Importing Internal Libraries
from core_files import db # type: ignore (Circular or complex import)
from lib.modal.db_init import Book
from lib.modal.schemas import BookCreate, BookUpdate, BookSchema
from lib.config.log_config import MethodWatcher
from lib.utils.maintenance import UtilityTools


logger = MethodWatcher()
logger.file_handler() # type: ignore (Library lacks type stubs in base class Log)

class BookManager(MethodView):

    def __init__(self, *args: Any, **kwargs: Any):

        #   Initialize the logger
        self.origins = '*'

        self.logger = logger
        self.tool = UtilityTools()

    def get(self) -> Response:
        books = Book.query.all()
        books_dict = [BookSchema.from_orm_model(book).model_dump(by_alias=True) for book in books]
        return self.response(books=books_dict)

    def post(self) -> Response:

        #  Fetch the requested data
        json_data = request.get_json()

        #   Log the data which is retrieved
        self.logger.warn(f"Data retrieved") # type: ignore (Library lacks type stubs in base class Log)

        if json_data and isinstance(json_data, dict):
            for key, value in json_data.items():
                self.logger.info(f"{key} : {value}") # type: ignore (Library lacks type stubs in base class Log)
        self.logger.warn(f"END OF LIST") # type: ignore (Library lacks type stubs in base class Log)

        #   Ensure that the data is not None
        if json_data is None: 
            self.logger.error(f"{request.headers} | {request.method}") # type: ignore (Library lacks type stubs in base class Log)
            return self.response(400, message="No data provided")

        try:
            # Validate data using Pydantic
            if not isinstance(json_data, dict):
                return self.response(400, message="Invalid data format")
                
            book_data = BookCreate(**json_data)

            # Initialize a new book object
            book = Book(
                title=book_data.title,
                author=book_data.author,
                genre=", ".join(book_data.genre),
                description=book_data.description,
                published_by=book_data.published_by,
                year=book_data.year,
                img_path=book_data.img_path,
                rating=book_data.rating,
                reviewers=book_data.reviewers
            )

            #   Commit the changes to the database
            db.session.add(book) # type: ignore (Library lacks type stubs)
            db.session.commit() # type: ignore (Library lacks type stubs)

        except ValidationError as e:
            self.logger.error(f"Validation Error: {e.json()}") # type: ignore (Library lacks type stubs in base class Log)
            return self.response(422, message=str(e.errors()))
        except IntegrityError as e:
            self.logger.error(f"Error : {e}") # type: ignore (Library lacks type stubs in base class Log)
            return self.response(405, message="Already exists within the database")

        return self.response(201)

    def put(self, BID: str) -> Response:

        #   fetch the current book
        book = Book.query.get(BID) # type: ignore (Library lacks type stubs)
        if not book:
            return self.response(404, BID=BID)

        #   Initialize the response and fetch the request data
        json_data = request.get_json()
        if not json_data:
            return self.response(405, message="No data provided")

        try:
            # Validate data using Pydantic
            if not isinstance(json_data, dict):
                return self.response(400, message="Invalid data format")

            update_data = BookUpdate(**json_data)
            update_dict = update_data.model_dump(exclude_unset=True)

            #   Update the book object
            for key, value in update_dict.items():
                if key == "genre" and value is not None:
                    setattr(book, key, ", ".join(value))
                elif hasattr(book, key) and key != 'id':
                    setattr(book, key, value)

            db.session.commit() # type: ignore (Library lacks type stubs)

        except ValidationError as e:
            self.logger.error(f"Validation Error: {e.json()}") # type: ignore (Library lacks type stubs in base class Log)
            return self.response(422, message=str(e.errors()))

        #   Success response
        self.logger.info(f"Data retrieved: {json_data} ") # type: ignore (Library lacks type stubs in base class Log)
        books = Book.query.all()
        books_dict = [BookSchema.from_orm_model(book).model_dump(by_alias=True) for book in books]
        return self.response(200, books=books_dict)

    def delete(self, BID: Optional[str]) -> Response:

        if BID is not None:
            self.tool.Purge(BID)
            return self.response(200, BID=BID)

        return self.response(405)

    def response(self, status: int = 200, message: Optional[str] = None, BID: Optional[str] = None, books: Optional[List[Any]] = None) -> Response:

        response: dict[str, Any] = {}

        match (status):

            #   Request successful
            case 200:
                response['books'] = books
                response['status'] = status

                if not message:
                    response['message'] = "The operation was successful !"

                if not books and status == 200 and request.method == 'GET':
                    response['message'] = "Books was not found !"

                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | response : {response}") # type: ignore (Library lacks type stubs in base class Log)

            case 201:

                response['status'] = status
                if not message:
                    response['message'] = "Successfully added a new entry to the database."

                self.logger.warn(f"\tMethod : {request.method} | Book ID : {BID}") # type: ignore (Library lacks type stubs in base class Log)

            case 400:
                response['status'] = status
                response['message'] = message or "Bad Request"
                self.logger.error(f"400 Bad Request: {message}") # type: ignore (Library lacks type stubs in base class Log)

            case 422:
                response['status'] = status
                response['message'] = message or "Unprocessable Entity"
                self.logger.error(f"422 Validation Error: {message}") # type: ignore (Library lacks type stubs in base class Log)

            #   Not Found
            case 404:
                response['status'] = status
                if not message:
                    response['message'] = "Checked everywhere, the book was not found."

                self.logger.error(f"\tMethod : {request.method} | Book ID : {BID}") # type: ignore (Library lacks type stubs in base class Log)

            #   Method not allowed
            case 405:
                response['status'] = status
                if not message:

                    response['message'] = "Something smells fishy, ensure the request method is correct."

                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | Book ID : {BID}") # type: ignore (Library lacks type stubs in base class Log)
            case 500:
                response['status'] = status

                if not message:
                    response['message'] = "An error occurred while attempting to process the request"
                self.logger.warn(f"Headers : {request.headers}\n  Method : {request.method} | Book ID : {BID}") # type: ignore (Library lacks type stubs in base class Log)
            
            case _:
                response['status'] = status
                response['message'] = message or "Unknown Status"

        return jsonify(response)
