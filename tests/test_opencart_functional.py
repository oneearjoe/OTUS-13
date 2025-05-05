from page_object.alerts import Alerts
from page_object.cart_page import CartPage
from page_object.catalog_page import CatalogPage
from page_object.main_page import MainPage
from page_object.product_page import ProductPage
from page_object.registration_page import RegistrationPage


def test_user_registration(browser):
    RegistrationPage(browser).open_registration_page()
    RegistrationPage(browser).fill_in_reg_form()
    RegistrationPage(browser).is_success_register_message()


def test_add_to_cart(browser):
    MainPage(browser).open_main_page()
    MainPage(browser).get_product_on_main_page()
    MainPage(browser).click_product(0)
    ProductPage(browser).add_to_cart()
    Alerts(browser).is_success_alert_displayed()
    CartPage(browser).open_cart()
    CartPage(browser).check_product_quantity_in_cart()


def test_currency_switch(browser):
    MainPage(browser).open_main_page()
    MainPage(browser).click_currency_dropdown()
    MainPage(browser).choose_currency()
    CatalogPage(browser).open_catalog_page()
    CatalogPage(browser).verify_price_currency()
