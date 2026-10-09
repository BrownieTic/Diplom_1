import pytest

from praktikum.database import Database
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as IngredientType

@pytest.fixture(scope="function")
def burger():
    burger = Burger()
    return burger

@pytest.fixture(scope="function")
def create_bun():
    bun = Bun('black bun', 100)
    return bun

@pytest.fixture(scope="function")
def create_bun_for_burger(burger, create_bun):
    burger.set_buns(create_bun)
    return burger

@pytest.fixture(scope="function")
def create_one_ingredient():
    ingredient = Ingredient(IngredientType.INGREDIENT_TYPE_FILLING, 'cutlet', 100)
    return ingredient

@pytest.fixture(scope="function")
def create_two_ingredients_for_burger(burger):
    ingredient1 = Ingredient(IngredientType.INGREDIENT_TYPE_FILLING, 'cutlet', 100)
    ingredient2 = Ingredient(IngredientType.INGREDIENT_TYPE_SAUCE, 'hot sauce', 200)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    return burger

@pytest.fixture(scope="function")
def create_full_burger(create_bun, create_two_ingredients_for_burger):
    create_two_ingredients_for_burger.set_buns(create_bun)
    return create_two_ingredients_for_burger

@pytest.fixture(scope="function")
def database():
    db = Database()
    return db
