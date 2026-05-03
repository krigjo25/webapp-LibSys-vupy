import pytest
from app import app

def test_app_exists():
    assert app is not None

def test_app_config():
    assert not app.testing
    app.config['TESTING'] = True
    assert app.testing
