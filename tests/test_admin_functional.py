
from page_object.admin_page import AdminPage


def test_admin_login_logout(browser):
    AdminPage(browser).open_admin_page()
    AdminPage(browser).login()
    AdminPage(browser).logout()


def test_add_new_product_in_admin(browser):
    name = "Test"
    AdminPage(browser).open_admin_page()
    AdminPage(browser).login()
    AdminPage(browser).open_product_list()
    AdminPage(browser).add_new_product(name)
    AdminPage(browser).open_product_list()
    AdminPage(browser).filter_product_by_name(name)
    AdminPage(browser).delete_product()


def test_remove_product_in_admin(browser):
    name = "Test1"
    AdminPage(browser).open_admin_page()
    AdminPage(browser).login()
    AdminPage(browser).open_product_list()
    AdminPage(browser).add_new_product(name)
    AdminPage(browser).open_product_list()
    AdminPage(browser).filter_product_by_name(name)
    AdminPage(browser).delete_product()
    AdminPage(browser).verify_product_has_been_deleted()
