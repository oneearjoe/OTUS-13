from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.admin_page import AdminPage
from page_object.catalog_page import CatalogPage
from page_object.main_page import MainPage
from page_object.product_page import ProductPage
from page_object.registration_page import RegistrationPage


def test_main_page_elements(browser):
    MainPage(browser).open_main_page().verify_elements()


def test_catalog_page_elements(browser):
    CatalogPage(browser).open_catalog_page().verify_elements()


def test_product_page_elements(browser):
    ProductPage(browser).open_product_page().verify_elements()


def test_admin_page_elements(browser):
    AdminPage(browser).open_admin_page().verify_elements()


def test_registration_page_elements(browser):
    RegistrationPage(browser).open_registration_page().verify_elements()
