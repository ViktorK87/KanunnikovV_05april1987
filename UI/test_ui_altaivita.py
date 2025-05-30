from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
from main_altaivita import Altaivita



browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

altaivita = Altaivita(browser)

@allure.severity("blocker")
@allure.title("Добавление товара в корзину")
@allure.feature("товары")
@allure.description("Ввод названия товара в поиск")
def test_add_product_in_cart():
    assert altaivita.add_product("золотой корень") == True
   
@allure.severity("blocker")
@allure.title("Вход в козину")
@allure.feature("Корзина")
@allure.description("Просмотр товара в корзине")   
def test_enter_cart():
   assert  altaivita.enter_cart() == True