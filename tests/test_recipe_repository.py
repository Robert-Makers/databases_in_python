from lib.recipe import Recipe
from lib.recipe_repository import RecipeRepository

'''
Test return all recipes
'''
def test_return_all_recipes(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repo = RecipeRepository(db_connection)
    recipes = repo.all()

    assert recipes == [
        Recipe(1,'Lasagna', 60, 4),
        Recipe(2, 'Pizza', 20, 5),
        Recipe(3, 'Mushroom Soup', 10, 2),
        Recipe(4, 'Fajitas', 30, 4)
    ]
    
'''
I can retrieve one recipe by searching by id
'''
def test_get_recipe_by_id(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repo = RecipeRepository(db_connection)
    recipe = repo.find(2)

    assert recipe == Recipe(2, 'Pizza', 20, 5)