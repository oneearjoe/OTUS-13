from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class Alerts(BasePage):
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success")

    def is_success_alert_displayed(self):
        self.is_element_visible(self.SUCCESS_ALERT)
