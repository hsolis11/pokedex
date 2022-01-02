import sqlite3

DATABASE = """C:/Users/hsoli/Documents/Developer/Projects/pokedex/pokemon.db"""


def get_connection():
    return sqlite3.connect(DATABASE)


class Store:
    def __init__(self):
        try:
            self.conn = get_connection()
        except Exception as e:
            print(e)
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        # can test for type and handle different situations
        self.close()

    def complete(self):
        self._complete = True

    def close(self):
        if self.conn:
            try:
                if self._complete:
                    self.conn.commit()
                else:
                    self.conn.rollback()
            except Exception as e:
                print(e)
            finally:
                try:
                    self.conn.close()
                except Exception as e:
                    print(e)


