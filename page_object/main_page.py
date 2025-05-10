from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
import allure


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

    @allure.step("Открытие галавной страницы")
    def open_main_page(self):
        self.logger.info(f"{self.class_name}: Open page {self.browser.base_url}")
        self.browser.get(self.browser.base_url)
        return self

    @allure.step("Проверка наличия элементов")
    def verify_elements(self):
        elements = [self.LOGO, self.MENU, self.SEARCH, self.CAROUSEL, self.FOOTER]
        for locator in elements:
            self.logger.info(
                f"{self.class_name}: Verify  element {locator} exists on the page"
            )
            self.is_element_visible(locator)

    @allure.step("Получениее списка продуктов на главной странице")
    def get_product_on_main_page(self):
        return self.get_elements(self.PRODUCT_LIST_ON_MAIN_PAGE)

    @allure.step("Выбор продукта")
    def click_product(self, index):
        self.logger.info(
            f"{self.class_name}: Click on the product with index = {index}"
        )
        self.get_product_on_main_page()[index].click()

    @allure.step("Клик по дропдауну с валютой")
    def click_currency_dropdown(self):
        self.logger.info(f"{self.class_name}: Click currency dropdown")
        self.click_element(self.CURRENCY_DROPDOWN)

    @allure.step("Выбор валюты")
    def choose_currency(self):
        self.logger.info(f"{self.class_name}: Choose eur currency")
        self.click_element(self.EUR_CURRENCY)
