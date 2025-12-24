import pytest
from app import create_app


@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test.
    """
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    """
    Flask test client for sending HTTP requests.
    """
    return app.test_client()


def test_app_starts(client):
    """
    Test that the Flask application starts successfully
    and the home page is reachable.
    """
    response = client.get("/")
    assert response.status_code == 200


def test_secret_key_is_set(app):
    """
    Test that SECRET_KEY is configured.
    This ensures basic application configuration is loaded.
    """
    assert app.config["SECRET_KEY"] is not None

def test_rooms_object_attached_to_app(app):
    """
    Test that shared rooms object is available in the app instance.
    """
    assert hasattr(app, "rooms")
