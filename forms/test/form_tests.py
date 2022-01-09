import pytest
from forms.form import SearchForm


def test_search_form_detect_int():
    pokemon = {'pokemonName': '4'}
    form = SearchForm()
    form.process(pokemon['pokemonName'])
    assert form.valid is True
    assert form.id == 4
    assert form.name == ''


def test_search_form_detect_string():
    pokemon = {'pokemonName': 'Charizard'}
    form = SearchForm()
    form.process(pokemon['pokemonName'])
    assert form.valid is True
    assert form.id == ''
    assert form.name == 'Charizard'


def test_search_form_empty():
    pokemon = {'pokemonName': ''}
    form = SearchForm()
    form.process(pokemon['pokemonName'])
    assert form.valid is False
    assert form.id == ''
    assert form.name == ''
