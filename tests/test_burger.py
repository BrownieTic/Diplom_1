import pytest
from unittest.mock import Mock

import praktikum.ingredient_types as IngredientType
from praktikum.bun import Bun

class TestBurger:
    
    def test_set_buns_sets_price(self, burger, create_bun):
        burger.set_buns(create_bun)
        assert burger.bun.price == 100


    def test_set_buns_sets_name(self, burger, create_bun):
        burger.set_buns(create_bun)
        assert burger.bun.name == 'black bun'

    def test_set_buns_change_bun_name(self, create_bun_for_burger):
        bun = Bun('sweet bun', 1)
        create_bun_for_burger.set_buns(bun)
        assert create_bun_for_burger.bun.name == 'sweet bun'

    def test_set_buns_change_bun_price(self, create_bun_for_burger):
        bun = Bun('sweet bun', 1)
        create_bun_for_burger.set_buns(bun)
        assert create_bun_for_burger.bun.price == 1

    @pytest.mark.parametrize('attribute, expected',[
        ('type', IngredientType.INGREDIENT_TYPE_FILLING),
        ('name', 'cutlet'),
        ('price', 100)])
    def test_add_ingredient_add_one_attribute_ingredient_in_list(self, burger, create_one_ingredient, attribute, expected):
        burger.add_ingredient(create_one_ingredient)
        assert getattr(burger.ingredients[0], attribute) == expected

    def test_remove_ingredient_remove_correct_ingredient_name(self, create_two_ingredients_for_burger):
        create_two_ingredients_for_burger.remove_ingredient(0)
        assert create_two_ingredients_for_burger.ingredients[0].name == 'hot sauce'

    def test_remove_ingredient_remove_correct_ingredient_price(self, create_two_ingredients_for_burger):
        create_two_ingredients_for_burger.remove_ingredient(0)
        assert create_two_ingredients_for_burger.ingredients[0].price == 200

    def test_remove_ingredient_after_remove_correct_len(self, create_two_ingredients_for_burger):
        create_two_ingredients_for_burger.remove_ingredient(0)
        assert len(create_two_ingredients_for_burger.ingredients) == 1  

    def test_remove_ingredient_minus_1_in_len(self, create_two_ingredients_for_burger):
        create_two_ingredients_for_burger.remove_ingredient(0)
        assert len(create_two_ingredients_for_burger.ingredients) == 1

    @pytest.mark.parametrize('index, new_index', [[1,0],[0,1]])
    def test_move_ingredient_move_both_direction(self, create_two_ingredients_for_burger, index, new_index):
        burger = create_two_ingredients_for_burger
        first_ingredient = burger.ingredients[0]
        second_ingredient = burger.ingredients[1]
        burger.move_ingredient(index, new_index)
        assert burger.ingredients[0] is second_ingredient
        assert burger.ingredients[1] is first_ingredient

    def test_move_ingredient_len_same_after(self, create_two_ingredients_for_burger):
        create_two_ingredients_for_burger.move_ingredient(1, 0)
        assert len(create_two_ingredients_for_burger.ingredients) == 2

    def test_get_price_calculates_two_buns_with_mock(self, burger):
        bun = Mock()
        bun.get_price.return_value = 1
        ingredient = Mock()
        ingredient.get_price.return_value = 0
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 2

    def test_get_price_calculates_ingredients_with_mock(self, burger):
        bun = Mock()
        bun.get_price.return_value = 0

        ingredient_1 = Mock()
        ingredient_1.get_price.return_value = 150

        ingredient_2 = Mock()
        ingredient_2.get_price.return_value = 50

        burger.set_buns(bun)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert burger.get_price() == 200
        ingredient_1.get_price.assert_called_once_with()
        ingredient_2.get_price.assert_called_once_with()

    def test_get_price_get_true_price_for_full_burger(self, create_full_burger):
        assert create_full_burger.get_price() == 500

    def test_get_receipt_without_ingredients(self, create_bun_for_burger):   
        expected_receipt = ( 
            "(==== black bun ====)\n" 
            "(==== black bun ====)\n" 
            "\n"
            "Price: 200" )
        assert create_bun_for_burger.get_receipt() == expected_receipt

    def test_get_receipt_with_mock_bun(self, create_two_ingredients_for_burger):   
        bun = Mock()
        bun.get_name.return_value = 'sweet'
        bun.get_price.return_value = 0
        create_two_ingredients_for_burger.set_buns(bun)
        expected_receipt = ( 
            "(==== sweet ====)\n" 
            "= filling cutlet =\n" 
            "= sauce hot sauce =\n" 
            "(==== sweet ====)\n" 
            "\n"
            "Price: 300" )
        assert create_two_ingredients_for_burger.get_receipt() == expected_receipt

    def test_get_receipt_full_burger(self, create_full_burger):   
        expected_receipt = ( 
            "(==== black bun ====)\n" 
            "= filling cutlet =\n" 
            "= sauce hot sauce =\n" 
            "(==== black bun ====)\n" 
            "\n"
            "Price: 500" )
        assert create_full_burger.get_receipt() == expected_receipt
    