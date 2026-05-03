# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false
#   Database tables for the app

from core_files import db # type: ignore (Circular or complex import)
import datetime as dt
from sqlalchemy import Column, Integer, String, REAL, ForeignKey, Date, Numeric, BigInteger
from sqlalchemy.orm import relationship
from typing import Dict, Any

class Author(db.Model): # type: ignore
    __tablename__ = "Authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    bio = Column(String(500), nullable=True)

    books = relationship("Book", back_populates="author_rel")

    def __repr__(self) -> str:
        return f"<Author {self.first_name} {self.last_name}>"

class Book(db.Model): # type: ignore
    __tablename__ = "Books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False, unique=True)
    author_id = Column(Integer, ForeignKey('Authors.id'), nullable=False)
    price = Column(Numeric(6, 2), nullable=False, default=0.0)
    qty = Column(Integer, nullable=False, default=1)
    genre = Column(String(255), nullable=False)
    subgenre = Column(String(255), nullable=True)
    rating = Column(REAL, nullable=True, default=0.0)
    
    # Fields kept for frontend compatibility (as requested)
    description = Column(String(1000), nullable=True)
    img_path = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    published_by = Column(String(255), nullable=True)

    author_rel = relationship("Author", back_populates="books")
    lendings = relationship("Lended", back_populates="book_rel")

    def __repr__(self) -> str:
        return f"<Book {self.title} (ID: {self.id})>"

class Member(db.Model): # type: ignore
    __tablename__ = "Members"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    membership_number = Column(BigInteger, unique=True, nullable=False)
    membership_date = Column(Date, nullable=False, default=dt.date.today)

    lendings = relationship("Lended", back_populates="member_rel")

    def __repr__(self) -> str:
        return f"<Member {self.first_name} {self.last_name}>"

class Lended(db.Model): # type: ignore
    __tablename__ = "Lended"
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('Books.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('Authors.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('Members.id'), nullable=False)
    borrow_date = Column(Date, nullable=False, default=dt.date.today)
    return_date = Column(Date, nullable=False)
    isLate = Column(Integer, nullable=False, default=0)
    isMissing = Column(Integer, nullable=False, default=0)

    book_rel = relationship("Book", back_populates="lendings")
    member_rel = relationship("Member", back_populates="lendings")

class TerminatedBook(db.Model): # type: ignore
    __tablename__ = "TerminatedBooks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('Authors.id'), nullable=False)
    qty = Column(Integer, nullable=False)
    isTerminated = Column(Integer, nullable=False, default=1)

class ReturnedBook(db.Model): # type: ignore
    __tablename__ = "ReturnedBooks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('Authors.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('Members.id'), nullable=False)
    return_date = Column(Date, nullable=False, default=dt.date.today)

class MissingBook(db.Model): # type: ignore
    __tablename__ = "MissingBooks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('Authors.id'), nullable=False)
    member_id = Column(Integer, ForeignKey('Members.id'), nullable=False)
    report_date = Column(Date, nullable=False, default=dt.date.today)
    fine_amount = Column(Numeric(6, 2), nullable=False, default=0.0)
