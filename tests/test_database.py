import praktikum.ingredient_types as IngredientType

class TestDatabase:
    def test_init_create_3_correct_buns(self, database):
        assert len(database.buns) == 3
        assert database.buns[0].get_name() == 'black bun'
        assert database.buns[0].get_price() == 100
        assert database.buns[1].get_name() == 'white bun'
        assert database.buns[1].get_price() == 200
        assert database.buns[2].get_name() == 'red bun'
        assert database.buns[2].get_price() == 300

    def test_init_create_correct_amount_ingredients_6(self, database):
        assert len(database.ingredients) == 6

    def test_init_create_3_correct_sauces(self, database):
        assert database.ingredients[0].get_type() == IngredientType.INGREDIENT_TYPE_SAUCE
        assert database.ingredients[0].get_name() == 'hot sauce'
        assert database.ingredients[0].get_price() == 100
        assert database.ingredients[1].get_type() == IngredientType.INGREDIENT_TYPE_SAUCE
        assert database.ingredients[1].get_name() == 'sour cream'
        assert database.ingredients[1].get_price() == 200
        assert database.ingredients[2].get_type() == IngredientType.INGREDIENT_TYPE_SAUCE
        assert database.ingredients[2].get_name() == 'chili sauce'
        assert database.ingredients[2].get_price() == 300

    def test_init_create_3_correct_fillings(self, database):
        assert database.ingredients[3].get_type() == IngredientType.INGREDIENT_TYPE_FILLING
        assert database.ingredients[3].get_name() == 'cutlet'
        assert database.ingredients[3].get_price() == 100
        assert database.ingredients[4].get_type() == IngredientType.INGREDIENT_TYPE_FILLING
        assert database.ingredients[4].get_name() == 'dinosaur'
        assert database.ingredients[4].get_price() == 200
        assert database.ingredients[5].get_type() == IngredientType.INGREDIENT_TYPE_FILLING
        assert database.ingredients[5].get_name() == 'sausage'
        assert database.ingredients[5].get_price() == 300

    def test_available_buns_get_correct_list_with_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == 'black bun'
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == 'white bun'
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == 'red bun'
        assert buns[2].get_price() == 300

    def test_available_ingredients_get_correct_list_with_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_type() == IngredientType.INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == 'hot sauce'
        assert ingredients[0].get_price() == 100
        assert ingredients[1].get_type() == IngredientType.INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == 'sour cream'
        assert ingredients[1].get_price() == 200
        assert ingredients[2].get_type() == IngredientType.INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_name() == 'chili sauce'
        assert ingredients[2].get_price() == 300
        assert ingredients[3].get_type() == IngredientType.INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == 'cutlet'
        assert ingredients[3].get_price() == 100
        assert ingredients[4].get_type() == IngredientType.INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == 'dinosaur'
        assert ingredients[4].get_price() == 200
        assert ingredients[5].get_type() == IngredientType.INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_name() == 'sausage'
        assert ingredients[5].get_price() == 300
