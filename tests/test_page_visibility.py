from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.admin_page import AdminPage
from page_object.catalog_page import CatalogPage
from page_object.main_page import MainPage
from page_object.product_page import ProductPage
from page_object.registration_page import RegistrationPage


def test_main_page_elements(browser):
    browser.get(browser.base_url)

    elements = [
        (By.CSS_SELECTOR, "header #logo"),
        (By.CSS_SELECTOR, "nav#menu"),
        (By.CSS_SELECTOR, "div#search"),
        (By.CSS_SELECTOR, "div.carousel"),
        (By.CSS_SELECTOR, "footer"),
    ]

    for locator in elements:
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(locator))


def test_catalog_page_elements(browser):
    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")

    elements = [
        (By.CSS_SELECTOR, "div#product-category"),
        (By.CSS_SELECTOR, "div.list-group"),
        (By.CSS_SELECTOR, "div.product-thumb"),
        (By.CSS_SELECTOR, "div#content h2"),
        (By.CSS_SELECTOR, "ul.pagination"),
    ]

    for locator in elements:
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(locator))


def test_product_page_elements(browser):
    browser.get(f"{browser.base_url}/en-gb/product/desktops/apple-cinema")

    elements = [
        (By.CSS_SELECTOR, "div#product-info"),
        (By.CSS_SELECTOR, "div.col-sm h1"),
        (By.CSS_SELECTOR, "div.col-sm h2"),
        (By.CSS_SELECTOR, "button#button-cart"),
        (By.CSS_SELECTOR, "div#tab-description"),
    ]

    for locator in elements:
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(locator))


def test_admin_page_elements(browser):
    browser.get(f"{browser.base_url}/administration/")

    elements = [
        (By.CSS_SELECTOR, "div.card-header"),
        (By.CSS_SELECTOR, "#input-username"),
        (By.CSS_SELECTOR, "#input-password"),
        (By.CSS_SELECTOR, "button.btn-primary"),
        (By.CSS_SELECTOR, "#footer"),
    ]

    for locator in elements:
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(locator))


def test_registration_page_elements(browser):
    browser.get(f"{browser.base_url}/en-gb?route=account/register")

    elements = [
        (By.CSS_SELECTOR, "#input-firstname"),
        (By.CSS_SELECTOR, "#input-lastname"),
        (By.CSS_SELECTOR, "#input-email"),
        (By.CSS_SELECTOR, "#input-password"),
        (By.CSS_SELECTOR, "button.btn-primary"),
    ]

    for locator in elements:
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(locator))


def test_main_page_elements(browser):
    (MainPage(browser).open_main_page().verify_elements())


def test_catalog_page_elements(browser):
    (CatalogPage(browser).open_catalog_page().verify_elements())


def test_product_page_elements(browser):
    (ProductPage(browser).open_product_page().verify_elements())


def test_admin_page_elements(browser):
    (AdminPage(browser).open_admin_page().verify_elements())


def test_registration_page_elements(browser):
    (RegistrationPage(browser).open_registration_page().verify_elements())
