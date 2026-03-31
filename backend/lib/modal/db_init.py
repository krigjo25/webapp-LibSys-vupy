#   Database tables for the app

from core_files import db
#   Importing the required modules

import datetime as dt
from uuid import uuid4
from sqlalchemy import Column, Integer, String, REAL

class Book(db.Model):
    """
        *   Books model class
        *   Initialize the class model
    """

    __tablename__ = "Books"
    id = Column(Integer, unique=True, autoincrement=True)
    bookID = Column(String, primary_key=True, nullable=False, default= lambda: uuid4().hex)

    genre = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    img_path = Column(String(100), nullable=True)
    reviewers = Column(String(100), nullable=True)
    published_by = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    rating = Column(REAL, nullable=True, default=0.0)
    title = Column(String(100), nullable=False, unique=True)
    year = Column(Integer, nullable=True, default=dt.datetime.now(dt.UTC))
    
    def __repr__(self):
        return f"<Book title : {self.title} Book id : {self.bookID} row : {self.id}>"
    
    def ConvertToDict(self):

        seperator = ","

        year = str(self.year).split('-')

        return {
            'id': self.bookID,
            'title': self.title,
            'author': self.author,
            'year': year[0],
            'genre': str(self.genre).split(seperator),
            'description': self.description,
            'path': self.img_path,
            'reviews': {'name':self.reviewers,
                        'rating': self.rating}
        }