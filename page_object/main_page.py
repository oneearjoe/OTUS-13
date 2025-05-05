from selenium.webdriver.common.by import By
from page_object.base_page import BasePage


class MainPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "header #logo")
    MENU = (By.CSS_SELECTOR, "nav#menu")
    SEARCH = (By.CSS_SELECTOR, "div#search")
    CAROUSEL = (By.CSS_SELECTOR, "div.carousel")
    FOOTER = (By.CSS_SELECTOR, "footer")
    ADD_TO_CART = (By.CSS_SELECTOR, '[title="Add to Cart"]')
    PRODUCT_LIST_ON_MAIN_PAGE = (By.CSS_SELECTOR, "div.product-thumb")
    CURRENCY_DROPDOWN = (
        By.CSS_SELECTOR,
        '[id="form-currency"] [data-bs-toggle="dropdown"]',
    )
    EUR_CURRENCY = (By.CSS_SELECTOR, 'a.dropdown-item[href="EUR"]')

    def open_main_page(self):
        self.browser.get(self.browser.base_url)
        return self

    def verify_elements(self):
        elements = [self.LOGO, self.MENU, self.SEARCH, self.CAROUSEL, self.FOOTER]
        for locator in elements:
            self.is_element_visible(locator)

    def get_product_on_main_page(self):
        return self.get_elements(self.PRODUCT_LIST_ON_MAIN_PAGE)

    def click_product(self, index):
        self.get_product_on_main_page()[index].click()

    def click_currency_dropdown(self):
        self.click_element(self.CURRENCY_DROPDOWN)

    def choose_currency(self):
        self.click_element(self.EUR_CURRENCY)
