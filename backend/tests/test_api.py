import pytest
import json
from app import app, db, initialize_database
from lib.modal.db_init import Book, Author

@pytest.fixture(scope='function')
def test_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            # Simplified seed for testing
            author1 = Author(first_name="Test", last_name="Author")
            db.session.add(author1)
            db.session.commit()
            book1 = Book(title="My Test Book", author_id=author1.id, genre="Test", description="A test book.")
            db.session.add(book1)
            db.session.commit()
        yield testing_client
        with app.app_context():
            db.drop_all()

def test_get_books(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/ ' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'books' in data
    assert len(data['books']) == 1
    assert data['books'][0]['title'] == 'My Test Book'
    assert data['books'][0]['author'] == 'Test Author'

def test_create_book(test_client):
    """
    GIVEN a Flask application
    WHEN the '/ ' page is posted to (POST)
    THEN check that a new book is created
    """
    response = test_client.post('/', 
                                 data=json.dumps(dict(title='Another Test Book', 
                                                      author='New Author', 
                                                      genre=['Fiction'],
                                                      description='...',
                                                      published_by='Test Publisher')),
                                 content_type='application/json')
    assert response.status_code == 201
    
    # Check if the author and book were created
    with app.app_context():
        assert Author.query.filter_by(first_name="New").count() == 1
        assert Book.query.filter_by(title="Another Test Book").count() == 1

def test_update_book(test_client):
    """
    GIVEN a Flask application
    WHEN an existing book is updated (PUT)
    THEN check that the book is updated
    """
    # First get the ID of the book to update
    book_id = None
    with app.app_context():
        book = Book.query.filter_by(title="My Test Book").first()
        book_id = book.id

    response = test_client.put(f'/{book_id}', 
                               data=json.dumps(dict(title='My Updated Test Book')),
                               content_type='application/json')
    assert response.status_code == 200
    
    with app.app_context():
        book = Book.query.get(book_id)
        assert book.title == 'My Updated Test Book'

def test_delete_book(test_client):
    """
    GIVEN a Flask application
    WHEN an existing book is deleted (DELETE)
    THEN check that the book is deleted
    """
    book_id = None
    with app.app_context():
        book = Book.query.filter_by(title="My Test Book").first()
        book_id = book.id

    response = test_client.delete(f'/{book_id}')
    assert response.status_code == 200

    with app.app_context():
        book = Book.query.get(book_id)
        assert book is None
