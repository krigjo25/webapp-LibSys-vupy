# Entry point for the application

# Importing the required libraries
from core_files import app, db, logger

#   Import application repositories
from lib.endpoints.book_resource import BookMananger
from lib.modal.test_data import alchemist, secrets

#   Initialize the database and add the preloaded data
with app.app_context():
    db.create_all()
    #db.session.add_all([alchemist, secrets])
    db.session.commit()

#   Endpoints
Mananger = BookMananger()
app.add_url_rule('/', view_func=Mananger.as_view('get', methods=['GET', 'POST']))
app.add_url_rule('/<BID>', view_func=Mananger.as_view('update', methods=['PUT', 'DELETE']))    

#   Log the application configurations
logger.warn('Application Configurations START')

for key, value in app.config.items():
    logger.info(f"{key} : {value}")

logger.warn('Application Configurations END')

#   Disable the cache
@app.after_request
def after_request(response):
    response.headers['Expires'] = 0
    response.headers['Pragma'] = "no-cache"
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    return response

#   Run the program
if __name__ == '__main__': app.run()