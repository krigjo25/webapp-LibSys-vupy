import pytest
from app import app

def test_app_exists():
    assert app is not None

def test_app_config_toggle():
    initial_state = app.testing
    app.config['TESTING'] = not initial_state
    assert app.testing != initial_state
    # Reset to original state
    app.config['TESTING'] = initial_state
    assert app.testing == initial_state
