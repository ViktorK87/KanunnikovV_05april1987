from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

class Altaivita:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://altaivita.ru/"
            )
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    def add_product(self, delay):
        with allure.step("Находим поле для вводв в поиск"):
            input_delay = self._driver.find_element(By.CSS_SELECTOR, '.searchpro__field-input.js-searchpro__field-input.digi-instant-search.jc-ignore')
            input_delay.clear()
        with allure.step("Вводим название товара"):
            input_delay.send_keys(delay)
            input_delay.send_keys(Keys.ENTER)
        sleep(4)
        with allure.step("Находим кнопку добавить"):
            btn_product = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located(( By.CSS_SELECTOR, 'button[tabindex="-1"]')))
        btn_product.click()
        with allure.step("Проверяем, что кнопка изменилась"):
            counter_plus = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                '[class="digi-product__cart-counter_plus"]'
            )))
        return counter_plus.is_displayed()
        
    def enter_cart(self):
        with allure.step("Добавляем в корзину товар"):
            self.add_product("золотой корень")
        with allure.step("Нажимаем кнопку входа в корзину"):
            self._driver.find_element(By.CSS_SELECTOR, '[class="header__basket js-basket-wrapper"]').click()
        sleep(3)
        WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                '[class="dropdown-go-over link-gray ga_link_to_cart"]'
            ))).click()
        sleep(3)
        with allure.step("проверяем, что появилась надпись Ваша корзина"):
            bool =  self._driver.find_element(By.CSS_SELECTOR, 'span[style="font-size:22px; color: #343434;"]').is_displayed()
            self._driver.quit()
        return bool
        
        
        
    

