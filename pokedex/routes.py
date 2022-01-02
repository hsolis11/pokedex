from pokedex import app


@app.route('/')
def hello_world():  # put application's code here
    repo = database.Pokemons()
    pokemon = repo.get(id=4)
    return render_template('stats.html', pokemon=pokemon, image='charmander.png')