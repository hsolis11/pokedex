from abc import ABC
from models.pokemon import Pokemon


class AbstractPokemons(ABC):
    def add(self, pokemon: Pokemon):
        raise NotImplementedError

    def get(self, id: int, name: str):
        raise NotImplementedError

    def list(self):
        raise NotImplementedError