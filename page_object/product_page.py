from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_INFO = (By.CSS_SELECTOR, "div#product-info")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.col-sm h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm h2")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button#button-cart")
    DESCRIPTION_TAB = (By.CSS_SELECTOR, "div#tab-description")

    def open_product_page(self):
        self.browser.get(self.browser.base_url + "/en-gb/product/desktops/apple-cinema")
        return self

    def verify_elements(self):
        elements = [
            self.PRODUCT_INFO,
            self.PRODUCT_TITLE,
            self.PRODUCT_PRICE,
            self.ADD_TO_CART_BUTTON,
            self.DESCRIPTION_TAB,
        ]
        for locator in elements:
            self.is_element_visible(locator)

    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)
