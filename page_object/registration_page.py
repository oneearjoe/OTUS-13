import time

from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from faker import Faker
import allure


class RegistrationPage(BasePage):
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, 'input[name="agree"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content > h1")

    fake = Faker()

    @allure.step("Откртыие страницы регистрации")
    def open_registration_page(self):
        self.logger.info(
            f"{self.class_name}: Open page {self.browser.base_url + '/en-gb?route=account/register'}"
        )

        self.browser.get(self.browser.base_url + "/en-gb?route=account/register")
        return self

    @allure.step("Проверка наличия элементов")
    def verify_elements(self):
        elements = [
            self.FIRSTNAME_INPUT,
            self.LASTNAME_INPUT,
            self.EMAIL_INPUT,
            self.PASSWORD_INPUT,
            self.CONTINUE_BUTTON,
        ]
        for locator in elements:
            self.logger.info(
                f"{self.class_name}: Verify  element {locator} exists on the page"
            )

            self.is_element_visible(locator)

    @allure.step("Заполнение формы регистрации")
    def fill_in_reg_form(self):
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        email = self.fake.email()
        self.logger.info(f"{self.class_name}: Enter first_name = {first_name}")
        self.input_value(self.FIRSTNAME_INPUT, first_name)
        self.logger.info(f"{self.class_name}: Enter last_name = {last_name}")
        self.input_value(self.LASTNAME_INPUT, last_name)
        self.logger.info(f"{self.class_name}: Enter email = {email}")
        self.input_value(self.EMAIL_INPUT, email)
        self.logger.info(f"{self.class_name}: Enter password")
        self.input_value(self.PASSWORD_INPUT, "123Qwe")
        self.click_element(self.PRIVACY_CHECKBOX)
        self.click_element(self.CONTINUE_BUTTON)

    @allure.step("Проверка что пользователь зарегестрировался")
    def is_success_register_message(self):
        time.sleep(1)
        msg = self.get_element(self.SUCCESS_MESSAGE)
        self.logger.info(f"{self.class_name}: New account has been registered")
        assert "Your Account Has Been Created!" in msg.text
