from pokedex import app
import database
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    title = "Pokedex"

    if request.method == 'POST':
        data = request.form.to_dict()
        repo = database.Pokemons()
        pokemon = repo.get(name=data['pokemonName'])
        if pokemon:
            title = f"{pokemon.name} - {pokemon.id} - Pokedex"
            return render_template('stats.html', title=title, pokemon=pokemon, image=f'{pokemon.name.lower()}.png')
    return render_template('stats.html', title=title)