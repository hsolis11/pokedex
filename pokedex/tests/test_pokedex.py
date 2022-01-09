import os

import pytest

# import the app
from pokedex import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_empty(client):

    rv = client.get('/')
    assert rv.status_code == 200
    pkm = client.post('/', data={'pokemonName': 'charizard'})
    print('\n', pkm.data)
    assert pkm.status_code == 200