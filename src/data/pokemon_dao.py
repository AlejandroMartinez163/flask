from data.models.pokemon import Pokemon

class PokemonDao():
    def __init__(self,db) -> None:
        self.db = db

    def get_all(self):
        cursor=self.db.cursor()
        cursor.execute('SELECT * FROM pokemon')
        data=cursor.fetchall()
        pokemon_lista = []

        for pokemons in data:
            pokemon_lista.append(Pokemon(pokemons[0],pokemons[1],pokemons[2]))
        
        return pokemon_lista

    def addPokemon(self,pokemon):
            cursor=self.db.cursor()
            cursor.execute('INSERT INTO pokemon (idpokemon,nombre,tipo) VALUES (%s,%s,%s)',(pokemon.idpokemon,pokemon.nombre,pokemon.tipo))
            self.db.commit()

    def deletePokemon(self,idpokemon):
            cursor=self.db.cursor()
            cursor.execute('DELETE FROM pokemon WHERE idpokemon=%s',(idpokemon,))
            self.db.commit()