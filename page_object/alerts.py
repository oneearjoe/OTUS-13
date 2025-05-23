from page_object.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class Alerts(BasePage):
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert-success")

    @allure.step("Проверка что успешны алерт появился")
    def is_success_alert_displayed(self):
        self.logger.info(f"{self.class_name}: Verify Success alert is displayed")

        self.is_element_visible(self.SUCCESS_ALERT)
