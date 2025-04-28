import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin_login_logout(browser):
    browser.get(f"{browser.base_url}/administration")

    username = browser.find_element(By.CSS_SELECTOR, "#input-username")
    username.send_keys("user")

    password = browser.find_element(By.CSS_SELECTOR, "#input-password")
    password.send_keys("bitnami")

    browser.find_element(By.CSS_SELECTOR, "button.btn-primary").click()

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav-logout"))
    )

    browser.find_element(By.CSS_SELECTOR, "#nav-logout").click()

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username"))
    )


def test_add_to_cart(browser):
    browser.get(browser.base_url)

    products = browser.find_elements(By.CSS_SELECTOR, "div.product-thumb")
    browser.execute_script("arguments[0].scrollIntoView();", products[0])
    btn_add_to_cart = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[title="Add to Cart"]'))
    )
    time.sleep(1)
    btn_add_to_cart[0].click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-success"))
    )

    browser.get(f"{browser.base_url}/en-gb?route=checkout/cart")
    quantity = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[name="quantity"]'))
    )
    quantity = quantity.get_attribute("value")
    assert quantity == "1"


def test_currency_switch(browser):
    browser.get(browser.base_url)

    browser.find_element(
        By.CSS_SELECTOR, '[id="form-currency"] [data-bs-toggle="dropdown"]'
    ).click()
    browser.find_element(By.CSS_SELECTOR, 'a.dropdown-item[href="EUR"]').click()

    browser.get(f"{browser.base_url}/en-gb/catalog/desktops")

    prices = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".price-new"))
    )
    assert "€" in prices[0].text
