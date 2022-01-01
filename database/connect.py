import sqlite3
from sqlite3 import Error
import csv


DATABASE = """C:/Users/hsoli/Documents/Developer/Projects/pokedex/pokemon.db"""
CSV_FILE = """C:/Users/hsoli/Documents/Developer/Projects/pokedex/Pokemon.csv"""


def connect(db_file):
    """ Create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn


def create_pokemon_table():
    sql = """CREATE TABLE IF NOT EXISTS pokemon(id integer,
                                                name text,
                                                type_1 text,
                                                type_2 text,
                                                total int,
                                                hp int,
                                                attack int,
                                                defense int,
                                                sp_atk int,
                                                sp_def int,
                                                speed int,
                                                generation int,
                                                legendary text);
                                                """

    conn = connect(DATABASE)

    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)


def fill_table():
    conn = connect(DATABASE)
    c = conn.cursor()
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            c.execute(""" INSERT INTO pokemon(id,name,type_1,type_2,total,hp,attack,
                            defense,sp_atk,sp_def,speed,generation,legendary)
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);""", [*row.values()])
            conn.commit()
        conn.close()

def main():
    create_pokemon_table()
    fill_table()



if __name__ == '__main__':
    main()
