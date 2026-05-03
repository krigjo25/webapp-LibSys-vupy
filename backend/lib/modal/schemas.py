from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional, Any


class BookBase(BaseModel):
    title: str
    author: str
    genre: List[str]
    description: str
    published_by: str
    year: Optional[int] = None
    img_path: Optional[str] = None
    rating: Optional[float] = 0.0
    reviewers: Optional[str] = None

    @field_validator('genre', mode='before')
    @classmethod
    def split_genres(cls, v: Any) -> List[str]:
        if isinstance(v, str):
            return [g.strip() for g in v.split(',')]
        return v


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[List[str]] = None
    description: Optional[str] = None
    published_by: Optional[str] = None
    year: Optional[int] = None
    img_path: Optional[str] = None
    rating: Optional[float] = None
    reviewers: Optional[str] = None


class ReviewSchema(BaseModel):
    name: Optional[str] = None
    rating: Optional[float] = 0.0


class BookSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str = Field(alias="bookID")
    title: str
    author: str
    year: Optional[str] = None
    genre: List[str]
    description: str
    path: Optional[str] = Field(alias="img_path", default=None)
    reviews: ReviewSchema = Field(default_factory=ReviewSchema)

    @field_validator('year', mode='before')
    @classmethod
    def format_year(cls, v: Any) -> Optional[str]:
        if v is None:
            return None
        return str(v).split('-')[0]

    @field_validator('genre', mode='before')
    @classmethod
    def split_genres(cls, v: Any) -> List[str]:
        if isinstance(v, str):
            return [g.strip() for g in v.split(',')]
        return v

    @classmethod
    def from_orm_model(cls, book: Any) -> "BookSchema":
        return cls(
            bookID=book.bookID,
            title=book.title,
            author=book.author,
            year=book.year,
            genre=book.genre,
            description=book.description,
            img_path=book.img_path,
            reviews=ReviewSchema(name=book.reviewers, rating=book.rating)
        )
