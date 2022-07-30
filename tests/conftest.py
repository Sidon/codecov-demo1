import pytest
from api import calc_app, create_app


@pytest.fixture
def app():

    test_app = create_app({
        'TESTING': True,
    })

    test_app = calc_app.create_calculator(test_app)
    yield test_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

