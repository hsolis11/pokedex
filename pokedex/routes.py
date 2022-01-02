from pokedex import app
import database
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    repo = database.Pokemons()
    pokemon = repo.get(id=4)
    return render_template('stats.html', pokemon=pokemon, image='charmander.png')