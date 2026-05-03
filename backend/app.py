import logging
from flask import Flask, Response
import alchemist  # type: ignore
import secrets    # type: ignore

def create_app() -> Flask:
    app = Flask(__name__)
    # ... application setup ...
    return app

app = create_app()

@app.after_request
def after_request(response: Response) -> Response:
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
