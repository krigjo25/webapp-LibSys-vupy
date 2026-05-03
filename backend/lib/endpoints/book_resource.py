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
from sqlalchemy.orm import joinedload
from pydantic import ValidationError

load_dotenv()

#   Importing Internal Libraries
from core_files import db # type: ignore (Circular or complex import)
from lib.modal.db_init import Book, Author
from lib.modal.schemas import BookCreate, BookUpdate, BookSchema
from lib.config.log_config import MethodWatcher
from lib.utils.maintenance import UtilityTools

logger = MethodWatcher()
logger.file_handler() # type: ignore (Library lacks type stubs in base class Log)

class BookManager(MethodView):

    def __init__(self, *args: Any, **kwargs: Any):
        self.origins = '*'
        self.logger = logger
        self.tool = UtilityTools()

    def _get_or_create_author(self, author_name: str) -> Author:
        """Finds an author by name or creates a new one."""
        first_name, last_name = author_name.split(" ", 1) if " " in author_name else (author_name, "")
        
        author = Author.query.filter_by(first_name=first_name, last_name=last_name).first()
        if not author:
            author = Author(first_name=first_name, last_name=last_name)
            db.session.add(author)
            db.session.commit()
        return author

    def get(self) -> Response:
        books = Book.query.options(joinedload(Book.author_rel)).all()
        books_dict = [BookSchema.from_orm_model(book).model_dump(by_alias=True) for book in books]
        return self.response(books=books_dict)

    def post(self) -> Response:
        json_data = request.get_json()
        if not json_data: 
            return self.response(400, message="No data provided")

        try:
            book_data = BookCreate(**json_data)
            
            author = self._get_or_create_author(book_data.author)
            
            book = Book(
                title=book_data.title,
                author_id=author.id,
                genre=", ".join(book_data.genre),
                description=book_data.description,
                published_by=book_data.published_by,
                year=book_data.year,
                img_path=book_data.img_path,
                rating=book_data.rating
            )
            db.session.add(book)
            db.session.commit()

        except ValidationError as e:
            return self.response(422, message=str(e.errors()))
        except IntegrityError as e:
            return self.response(409, message="A book with this title already exists.")

        return self.response(201, BID=str(book.id))

    def put(self, BID: str) -> Response:
        try:
            book_id_int = int(BID)
        except ValueError:
            return self.response(400, message="Invalid Book ID format.")

        book = Book.query.get(book_id_int)
        if not book:
            return self.response(404, BID=BID)

        json_data = request.get_json()
        if not json_data:
            return self.response(400, message="No data provided")

        try:
            update_data = BookUpdate(**json_data)
            update_dict = update_data.model_dump(exclude_unset=True)

            if 'author' in update_dict:
                author = self._get_or_create_author(update_dict['author'])
                book.author_id = author.id
                del update_dict['author'] # No direct 'author' field on Book model

            for key, value in update_dict.items():
                if key == "genre" and value is not None:
                    setattr(book, key, ", ".join(value))
                elif hasattr(book, key):
                    setattr(book, key, value)

            db.session.commit()

        except ValidationError as e:
            return self.response(422, message=str(e.errors()))

        books = Book.query.options(joinedload(Book.author_rel)).all()
        books_dict = [BookSchema.from_orm_model(book).model_dump(by_alias=True) for book in books]
        return self.response(200, books=books_dict)

    def delete(self, BID: Optional[str]) -> Response:
        if BID is None:
            return self.response(405)
        
        try:
            book_id_int = int(BID)
            # Purge logic needs to be updated for integer IDs if it's still used
            # For now, just delete the book directly
            book = Book.query.get(book_id_int)
            if book:
                db.session.delete(book)
                db.session.commit()
                return self.response(200, BID=BID)
            else:
                return self.response(404, BID=BID)
        except (ValueError, IntegrityError) as e:
            return self.response(500, message=f"Error deleting book: {e}")


    def response(self, status: int = 200, message: Optional[str] = None, BID: Optional[str] = None, books: Optional[List[Any]] = None) -> Response:
        response: dict[str, Any] = {}
        if books is not None:
            response['books'] = books
        response['status'] = status
        
        # Default messages based on status
        if message is None:
            if status == 200:
                message = "The operation was successful."
            elif status == 201:
                message = "Successfully added a new entry to the database."
            elif status == 400:
                message = "Bad Request. The server could not understand the request due to invalid syntax."
            elif status == 404:
                message = "The requested resource could not be found."
            elif status == 405:
                message = "Method Not Allowed."
            elif status == 409:
                message = "Conflict with existing resource."
            elif status == 422:
                message = "Unprocessable Entity. The request was well-formed but was unable to be followed due to semantic errors."
            elif status == 500:
                message = "Internal Server Error."
            else:
                message = "An unknown status occurred."

        response['message'] = message
        
        if BID is not None:
            response['BID'] = BID

        return jsonify(response), status
