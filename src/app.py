from flask import Flask, render_template, request, redirect, url_for
from data.pokemon_dao import PokemonDao
from data.tipo_dao import TipoDao
from data.models.pokemon import Pokemon
from data.models.tipo import Tipo
from database import db

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/pokedex')
def pokedex():
    pokemon_dao : PokemonDao = PokemonDao(db)
    return render_template('pokedex.html', pokedex=pokemon_dao.get_all())



@app.route('/tipos')
def tipo():
    tipo_dao : TipoDao = TipoDao(db)
    return render_template('tipo.html', tipos=tipo_dao.get_all())



@app.route('/newtipo')
def new_tipo():
    return render_template('add_tipo.html')



@app.route('/newpokemon')
def new_pokemon():
    return render_template('add_pokemon.html')



@app.route('/addPokemons', methods=['POST'])
def add_pokemon():   
    if request.method == 'POST':
        idpokemon = request.form['idpokemon']
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        
        pokemon = Pokemon(idpokemon,nombre,tipo)
        pokemon_dao : PokemonDao = PokemonDao(db)
        pokemon_dao.addPokemon(pokemon)

    return redirect(url_for('new_pokemon'))



@app.route('/addTipo', methods=['POST'])
def add_tipo():
    if request.method == 'POST':
        idtipo = request.form['idtipo']
        elemento = request.form['elemento']
        afinidad = request.form['afinidad']
        
        tipo_tabla = Tipo(idtipo,elemento,afinidad)
        tipo_dao : TipoDao = TipoDao(db)
        tipo_dao.addTipo(tipo_tabla)
        
    return redirect(url_for('new_tipo'))


@app.route('/deleteTipo/<string:idtipo>')
def delete_tipo(idtipo):
    tipo_dao : TipoDao = TipoDao(db)
    tipo_dao.deleteTipo(idtipo)
    return redirect(url_for('tipo'))



@app.route('/deletePokemon/<string:idpokemon>')
def delete_pokemon(idpokemon):
    pokemon_dao : PokemonDao = PokemonDao(db)
    pokemon_dao.deletePokemon(idpokemon)
    return redirect(url_for('pokedex'))



if __name__ == '__main__':
    app.run(port=5000)
