import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests (chrome, edge, firefox)",
    )
    parser.addoption(
        "--url",
        action="store",
        default="http://192.168.1.102:8081/",
        help="Base OpenCart URL",
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.base_url = base_url
    driver.implicitly_wait(5)

    yield driver

    driver.quit()
