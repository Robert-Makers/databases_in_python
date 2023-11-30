from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes = [Recipe(row['id'], row['name'], row['cooking_time'], row['rating']) for row in rows]
        return recipes

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM recipes WHERE id = %s', [id])
        recipes = [Recipe(row['id'], row['name'], row['cooking_time'], row['rating']) for row in rows]
        return recipes[0]