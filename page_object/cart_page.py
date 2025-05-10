from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class CartPage(BasePage):
    SHOPPING_CART = (By.CSS_SELECTOR, '[title="Shopping Cart"]')
    QUANTITY = (By.CSS_SELECTOR, '[name="quantity"]')

    @allure.step("Открытие карзины")
    def open_cart(self):
        self.logger.info(
            f"{self.class_name}: Open page {self.browser.base_url + '/en-gb?route=checkout/cart'}"
        )

        self.browser.get(self.browser.base_url + "/en-gb?route=checkout/cart")

    @allure.step("Проверка количества товара")
    def check_product_quantity_in_cart(self):
        quantity = self.is_element_visible(self.QUANTITY)
        quantity = quantity.get_attribute("value")
        self.logger.info(f"{self.class_name}: Verify product quantity {quantity} == 1")
        assert quantity == "1"
