import pytest

from app import login

@pytest.fixture
def app():
    app = login()
    return app