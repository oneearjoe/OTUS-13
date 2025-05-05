from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from datetime import datetime

from tests.conftest import browser


class AdminPage(BasePage):

    CARD_HEADER = (By.CSS_SELECTOR, "div.card-header")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    FOOTER = (By.CSS_SELECTOR, "#footer")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#nav-logout")
    MENU_CATALOG_BUTTON = (By.CSS_SELECTOR, "#menu-catalog")
    MENU_CATALOG_PRODUCTS_BTN = (By.XPATH, "//a[text()='Products']")
    ADD_NEW_BTN = (By.CSS_SELECTOR, "a.btn.btn-primary")
    DELETE_BTN = (By.CSS_SELECTOR, "button.btn.btn-danger")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name-1")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    SAVE_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    TAB_DATA = (By.CSS_SELECTOR, "a[href='#tab-data']")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    SEO_TAB = (By.CSS_SELECTOR, "a[href='#tab-seo']")
    PRODUCTS_LIST = (By.CSS_SELECTOR, "#form-product table")
    KEYWORD_INPUT = (By.CSS_SELECTOR, "#input-keyword-0-1")
    PRODUCT_NAME_FILTER = (By.CSS_SELECTOR, "#input-name")
    FILTER_BTN = (By.CSS_SELECTOR, "#button-filter")
    EDIT_BTN = (
        By.CSS_SELECTOR,
        "a.btn.btn-primary[href*='product.form'][aria-label='Edit']",
    )
    CHECK_BOX = (By.CSS_SELECTOR, "input.form-check-input")
    NO_RESULT = (
        By.XPATH,
        "//td[@class='text-center' and contains(text(), 'No results!')]",
    )

    def open_admin_page(self):
        self.browser.get(self.browser.base_url + "/administration/")
        return self

    def verify_elements(self):
        elements = [
            self.CARD_HEADER,
            self.USERNAME_INPUT,
            self.PASSWORD_INPUT,
            self.LOGIN_BUTTON,
            self.FOOTER,
        ]
        for locator in elements:
            self.is_element_visible(locator)

    def login(self):
        self.get_element(self.USERNAME_INPUT)
        self.input_value(self.USERNAME_INPUT, "user")
        self.get_element(self.PASSWORD_INPUT)
        self.input_value(self.PASSWORD_INPUT, "bitnami")
        self.click_element(self.LOGIN_BUTTON)
        self.is_element_visible(self.LOGOUT_BUTTON)

    def logout(self):
        self.get_element(self.LOGOUT_BUTTON)
        self.click_element(self.LOGOUT_BUTTON)
        self.is_element_visible(self.USERNAME_INPUT)

    def open_product_list(self):
        self.click_element(self.MENU_CATALOG_BUTTON)
        self.click_element(self.MENU_CATALOG_PRODUCTS_BTN)

    def add_new_product(self, name):
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.click_element(self.ADD_NEW_BTN)
        self.input_value(self.PRODUCT_NAME_INPUT, name)
        self.input_value(self.META_TAG_TITLE_INPUT, name)
        self.click_element(self.TAB_DATA)
        self.input_value(self.MODEL_INPUT, name)
        self.click_element(self.SEO_TAB)
        self.input_value(self.KEYWORD_INPUT, f"{name}-{current_datetime}")
        self.click_element(self.SAVE_BTN)

    def filter_product_by_name(self, name):
        self.input_value(self.PRODUCT_NAME_FILTER, name)
        self.click_element(self.FILTER_BTN)
        product = self.get_element(self.PRODUCTS_LIST)
        assert name in product.text

    def verify_new_product_in_product_list(self, name):
        assert name in self.get_products_list()

    def delete_product(self):
        self.click_element(self.CHECK_BOX)
        self.click_element(self.DELETE_BTN)
        alert = self.browser.switch_to.alert
        alert.accept()

    def verify_product_has_been_deleted(self):
        no_result = self.get_element(self.NO_RESULT)
        assert "No results!" == no_result.text
