import allure
from page_object.admin_page import AdminPage
from page_object.catalog_page import CatalogPage
from page_object.main_page import MainPage
from page_object.product_page import ProductPage
from page_object.registration_page import RegistrationPage


@allure.title("проверка элементов на главной странице")
def test_main_page_elements(browser):
    MainPage(browser).open_main_page().verify_elements()


@allure.title("Проверка элементов каталога")
def test_catalog_page_elements(browser):
    CatalogPage(browser).open_catalog_page().verify_elements()


@allure.title("Проверка элементов на странице продукта")
def test_product_page_elements(browser):
    ProductPage(browser).open_product_page().verify_elements()


@allure.title("Проверка элементов на странице логина в админку")
def test_admin_page_elements(browser):
    AdminPage(browser).open_admin_page().verify_elements()


@allure.title("Проверка элементов на странице регистрации пользователей")
def test_registration_page_elements(browser):
    RegistrationPage(browser).open_registration_page().verify_elements()
