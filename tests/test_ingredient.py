import praktikum.ingredient_types as IngredientType

class TestIngredient:
    def test_get_price_returns_price_100(self, create_one_ingredient):
        ingredient = create_one_ingredient
        assert ingredient.get_price() == 100

    def test_get_name_returns_cutlet(self, create_one_ingredient):
        ingredient = create_one_ingredient
        assert ingredient.get_name() == 'cutlet'

    def test_get_type_returns_filling(self, create_one_ingredient):
        ingredient = create_one_ingredient
        assert ingredient.get_type() == IngredientType.INGREDIENT_TYPE_FILLING
