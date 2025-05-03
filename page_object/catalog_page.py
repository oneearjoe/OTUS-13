from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class CatalogPage(BasePage):
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, "div#product-category")
    LIST_GROUP = (By.CSS_SELECTOR, "div.list-group")
    PRODUCT_THUMB = (By.CSS_SELECTOR, "div.product-thumb")
    CONTENT_HEADER = (By.CSS_SELECTOR, "div#content h2")
    PAGINATION = (By.CSS_SELECTOR, "ul.pagination")
    NEW_PRICE = (By.CSS_SELECTOR, ".price-new")

    def open_catalog_page(self):
        self.browser.get(self.browser.base_url + "/en-gb/catalog/desktops")
        return self

    def verify_elements(self):
        elements = [
            self.PRODUCT_CATEGORY,
            self.LIST_GROUP,
            self.PRODUCT_THUMB,
            self.CONTENT_HEADER,
            self.PAGINATION,
        ]
        for locator in elements:
            self.is_element_visible(locator)

    def verify_price_currency(self):
        prices = self.get_elements(self.NEW_PRICE)
        assert "€" in prices[0].text
