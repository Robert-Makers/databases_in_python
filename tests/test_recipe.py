from lib.recipe import Recipe

'''
Test recipe contructs with name, rating and cooking time
'''
def test_construct_recipe():
    recipe = Recipe(1, 'Enchiladas', 40, 5)
    assert recipe.name == 'Enchiladas'
    assert recipe.cooking_time == 40
    assert recipe.rating == 5

def test_equality():
    recipe_1 = Recipe(1, 'Enchiladas', 40, 5)
    recipe_2 = Recipe(1, 'Enchiladas', 40, 5)
    assert recipe_1 == recipe_2

def test_format_recipe():
    recipe = Recipe(1, 'Enchiladas', 40, 5)
    assert str(recipe) == "Recipe(Enchiladas, 40, 5)"