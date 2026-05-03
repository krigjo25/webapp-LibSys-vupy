from typing import Any
from flask import Response
from core_files import app, db
from lib.modal.db_init import Book
from lib.endpoints.book_resource import BookManager
from lib.modal.test_data import alchemist, secrets

def initialize_database():
    """Initializes the database and seeds it with test data if empty."""
    with app.app_context():
        db.create_all()
        if Book.query.count() == 0:
            db.session.add(alchemist)
            db.session.add(secrets)
            db.session.commit()
            print("Database initialized and seeded with test data.")

# Register Routes
book_view = BookManager.as_view('book_api')
app.add_url_rule('/', view_func=book_view, methods=['GET', 'POST'])
app.add_url_rule('/<BID>', view_func=book_view, methods=['GET', 'PUT', 'DELETE'])

@app.after_request
def after_request(response: Response) -> Response:
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    initialize_database()
    app.run(host='0.0.0.0', port=5000, debug=True)
