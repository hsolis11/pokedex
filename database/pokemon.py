from database.base_connection import Store
from abc import ABC, abstractmethod
import dataclasses
from dataclasses import dataclass


@dataclass
class Pokemon:
    id: int
    name: str
    type_1: str
    type_2: str
    total: int
    hp: int
    attack: int
    defense: int
    sp_atk: int
    sp_def: int
    speed: int
    generation: int
    legendary: bool


class AbstractPokemons(ABC):
    def add(cls, pokemon: Pokemon):
        raise NotImplementedError

    def get(cls, id: int, name: str):
        raise NotImplementedError

    def list(cls):
        raise NotImplementedError


class Pokemons(AbstractPokemons, Store):

    def add(self, pokemon: Pokemon):
        try:
            c = self.conn.cursor()
            c.execute(""" INSERT INTO pokemon(id,name,type_1,type_2,total,hp,attack,
                                        defense,sp_atk,sp_def,speed,generation,legendary)
                                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);""", dataclasses.astuple(pokemon))
            self.complete()
            self.close()

        except Exception as e:
            print(e)

    def get(self, id=None, name=None):
        try:
            c = self.conn.cursor()
            sql = ""
            value = ""
            if id:
                sql = "SELECT * FROM pokemon WHERE id = ?"
                value = (id,)

            if name:
                sql = "SELECT * FROM pokemon WHERE name = ?"
                value = (name,)

            c.execute(sql, value)
            pokemon = c.fetchall()
            if pokemon:
                return Pokemon(*pokemon[0])

        except Exception as e:
            print(e)

    def list(self):
        try:
            pokemons = []
            c = self.conn.cursor()
            c.execute("SELECT * FROM pokemon")
            data = c.fetchall()
            if data:
                for pokemon in data:
                    pokemons.append(Pokemon(*pokemon))
            return pokemons

        except Exception as e:
            print(e)
