
from main_altaivita import Altaivita
import allure
import pytest

altaivita = Altaivita()

@allure.severity("blocker")
@allure.feature("вход в корзину")
@allure.description("корзина")
@allure.title("товары в корзине")
def test_enter_cart():
    res = altaivita.enter_cart()
    print(res.json())
    if res.json() == []:
        assert res.json() == []
    else:
        assert res.json()[0]['quantity'] == 1

@allure.severity("blocker")
@allure.feature("добавление товара")
@allure.description("корзина")
@allure.title("товары")
def test_add_good():
    res = altaivita.add_good_in_cart()
    assert res.json()['new_quantity'] == 1

@allure.severity("blocker")
@allure.feature("удаление")
@allure.description("удаление товара")
@allure.title("корзина")
def test_delete_goods():
    res = altaivita.delete_dood_from_cart()
    assert res.json()['sum_quantity'] == '0'