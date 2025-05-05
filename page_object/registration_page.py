import time

from selenium.webdriver.common.by import By
from page_object.base_page import BasePage
from faker import Faker


class RegistrationPage(BasePage):
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, 'input[name="agree"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content > h1")

    fake = Faker()

    def open_registration_page(self):
        self.browser.get(self.browser.base_url + "/en-gb?route=account/register")
        return self

    def verify_elements(self):
        elements = [
            self.FIRSTNAME_INPUT,
            self.LASTNAME_INPUT,
            self.EMAIL_INPUT,
            self.PASSWORD_INPUT,
            self.CONTINUE_BUTTON,
        ]
        for locator in elements:
            self.is_element_visible(locator)

    def fill_in_reg_form(self):
        self.input_value(self.FIRSTNAME_INPUT, self.fake.first_name())
        self.input_value(self.LASTNAME_INPUT, self.fake.last_name())
        self.input_value(self.EMAIL_INPUT, self.fake.email())
        self.input_value(self.PASSWORD_INPUT, "123Qwe")
        self.click_element(self.PRIVACY_CHECKBOX)
        self.click_element(self.CONTINUE_BUTTON)

    def is_success_register_message(self):
        time.sleep(1)
        msg = self.get_element(self.SUCCESS_MESSAGE)
        print(f"{msg.text}")
        assert "Your Account Has Been Created!" in msg.text
