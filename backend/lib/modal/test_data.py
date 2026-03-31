from .db_init import Book
from uuid import uuid4
alchemist = Book(
    rating = 4.5,
    title = "The Alchemist",
    author = "Paulo Coelho",
    reviewers = "Books.com",
    published_by = "HarperCollins",
    img_path = "./src/assets/img/the_alchemist.jpeg",
    genre = "Adventure, Quest, Drama, Fantasy, Fiction, Philosophical fiction",
    description = "The Alchemist is a novel by Brazilian author Paulo Coelho that was first published in 1988. Originally written in Portuguese, it became an international bestseller translated into some 70 languages as of 2016. An allegorical novel, The Alchemist follows a young Andalusian shepherd in his journey to the pyramids of Egypt, after having a recurring dream of finding a treasure there.",
)

secrets = Book(
    rating = 4.2,
    title = "The Secret",
    reviewers = "Books.com",
    author = "Rhonda Byrne",
    published_by = "Atria Books",
    description = '"The Secret" presents a philosophy that empowers individuals to take control of their lives by harnessing the power of their thoughts.',
    img_path = "./src/assets/img/the_secret.jpeg",
    genre = "Self-help book, Personal development",
)