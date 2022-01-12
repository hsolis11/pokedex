from pokedex import app
import database
from flask import render_template, request
from forms import SearchForm


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    title = "Pokedex"

    if request.method == 'POST':
        data = request.form.to_dict()
        repo = database.Pokemons()
        form = SearchForm()
        form.process(data['pokemonName'])
        pokemon = None
        if form.is_int:
            pokemon = repo.get(id=form.id)
        if form.is_str:
            pokemon = repo.get(name=form.name)
        if pokemon:
            title = f"{pokemon.name} - {pokemon.id} - Pokedex"
            return render_template('stats.html', title=title, pokemon=pokemon, image=f'{pokemon.name.lower()}.png')
    return render_template('stats.html', title=title)
