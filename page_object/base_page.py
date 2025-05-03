from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def is_element_visible(self, locator, timeout=5):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def is_elements_visible(self, locators, timeout=5):
        for locator in locators:
            self.is_element_visible(locator, timeout)

    def get_element(self, locator):
        return self.is_element_visible(locator)

    def get_elements(self, locator):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(
            0.3
        ).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.click_element(locator)
        self.get_element(locator).clear()
        for i in text:
            self.get_element(locator).send_keys(i)
