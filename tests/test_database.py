import pytest
import praktikum.ingredient_types as IngredientType

class TestDatabase:
    @pytest.mark.parametrize("num, name", [
        (0, 'black bun'), 
        (1, 'white bun'), 
        (2, 'red bun')])
    def test_init_create_correct_bun_name(self, database, num, name):
        assert database.buns[num].get_name() == name

    @pytest.mark.parametrize("num, price", [
        (0, 100), 
        (1, 200), 
        (2, 300)])
    def test_init_create_correct_bun_price(self, database, num, price):
        assert database.buns[num].get_price() == price

    def test_init_create_correct_amount_buns_3(self, database):      
        assert len(database.buns) == 3

    def test_init_create_correct_amount_ingredients_6(self, database):
        assert len(database.ingredients) == 6

    @pytest.mark.parametrize("num", [
        (0), 
        (1), 
        (2)])
    def test_init_create_3_correct_type_sauces(self, database, num):
        assert database.ingredients[num].get_type() == IngredientType.INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize("num, name", [
        (0, 'hot sauce'), 
        (1, 'sour cream'), 
        (2, 'chili sauce')])
    def test_init_create_3_correct_name_sauces(self, database, num, name):
        assert database.ingredients[num].get_name() == name

    @pytest.mark.parametrize("num, price", [
        (0, 100), 
        (1, 200), 
        (2, 300)])
    def test_init_create_3_correct_price_sauces(self, database, num, price):
        assert database.ingredients[num].get_price() == price

    @pytest.mark.parametrize("num", [
        (3), 
        (4), 
        (5)])
    def test_init_create_3_correct_fillings_type(self, database, num):
        assert database.ingredients[num].get_type() == IngredientType.INGREDIENT_TYPE_FILLING

    @pytest.mark.parametrize("num, name", [
        (3, 'cutlet'), 
        (4, 'dinosaur'), 
        (5, 'sausage')])
    def test_init_create_3_correct_fillings_name(self, database, num, name):
        assert database.ingredients[num].get_name() == name

    @pytest.mark.parametrize("num, price", [
        (3, 100), 
        (4, 200), 
        (5, 300)])
    def test_init_create_3_correct_fillings_price(self, database, num, price):
        assert database.ingredients[num].get_price() == price

    def test_available_buns_returns_correct_list_len(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    @pytest.mark.parametrize('num, name',[
            (0, 'black bun'),
            (1, 'white bun'),
            (2, 'red bun')])
    def test_available_buns_returns_correct_name(self, database, num, name):
        buns = database.available_buns()
        assert buns[num].get_name() == name

    @pytest.mark.parametrize('num, price',[
            (0, 100),
            (1, 200),
            (2, 300)])
    def test_available_buns_returns_correct_prices(self, database, num, price):
        buns = database.available_buns()
        assert buns[num].get_price() == price

    def test_available_ingredients_get_correct_len_6(self, data_available_ingredients):
        assert len(data_available_ingredients) == 6

    @pytest.mark.parametrize("num", [
        (0),
        (1),
        (2)
    ])
    def test_available_ingredients_get_correct_list_with_type_sauces(self, data_available_ingredients, num):
        assert data_available_ingredients[num].get_type() == IngredientType.INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize("num, name", [
        (0, 'hot sauce'),
        (1, 'sour cream'),
        (2, 'chili sauce')
    ])
    def test_available_ingredients_get_correct_list_with_name_sauces(self, data_available_ingredients, num, name):
        assert data_available_ingredients[num].get_name() == name

    @pytest.mark.parametrize("num, price", [
        (0, 100),
        (1, 200),
        (2, 300)
    ])
    def test_available_ingredients_get_correct_list_with_price_sauces(self, data_available_ingredients, num, price):
        assert data_available_ingredients[num].get_price() == price

    @pytest.mark.parametrize("num", [
        (3),
        (4),
        (5)
    ])
    def test_available_ingredients_get_correct_list_with_type_fillings(self, data_available_ingredients, num):
        assert data_available_ingredients[num].get_type() == IngredientType.INGREDIENT_TYPE_FILLING

    @pytest.mark.parametrize("num, name", [
        (3, 'cutlet'),
        (4, 'dinosaur'),
        (5, 'sausage')
    ])
    def test_available_ingredients_get_correct_list_with_name_fillings(self, data_available_ingredients, num, name):
        assert data_available_ingredients[num].get_name() == name

    @pytest.mark.parametrize("num, price", [
        (3, 100),
        (4, 200),
        (5, 300)
    ])
    def test_available_ingredients_get_correct_list_with_price_fillings(self, data_available_ingredients, num, price):
        assert data_available_ingredients[num].get_price() == price        
