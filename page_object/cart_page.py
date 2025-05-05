from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    SHOPPING_CART = (By.CSS_SELECTOR, '[title="Shopping Cart"]')
    QUANTITY = (By.CSS_SELECTOR, '[name="quantity"]')

    def open_cart(self):
        self.browser.get(self.browser.base_url + "/en-gb?route=checkout/cart")

    def check_product_quantity_in_cart(self):
        quantity = self.is_element_visible(self.QUANTITY)
        quantity = quantity.get_attribute("value")
        assert quantity == "1"


# quantity = WebDriverWait(browser, 10).until(
#    EC.presence_of_element_located((By.CSS_SELECTOR, '[name="quantity"]'))
# )
# quantity = quantity.get_attribute("value")
# assert quantity == "1"
