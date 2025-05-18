import pytest
import logging
import datetime
import allure
import json
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run tests (chrome, edge, firefox)")
    parser.addoption("--url", default="http://192.168.1.105:8081/", help="Base OpenCart URL")
    parser.addoption("--log_level", default="INFO")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "setup":
        browser = item.funcargs.get("browser")
        if browser:
            allure.attach(
                name=browser.session_id,
                body=json.dumps(browser.capabilities, indent=4, ensure_ascii=False),
                attachment_type=allure.attachment_type.JSON,
            )

    if rep.when == "call" and rep.failed:
        browser = item.funcargs.get("browser")
        if browser:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def logger(request):
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler("example.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info(
        "=====> Test %s started %s" % (request.node.name, datetime.datetime.now())
    )

    yield logger
    logger.info(
        "=====> Browser %s opened at %s" % (request.node.name, datetime.datetime.now())
    )


@pytest.fixture
def browser(request, logger):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.logger = logger
    driver.test_name = request.node.name
    driver.base_url = base_url
    driver.implicitly_wait(5)

    yield driver
    driver.quit()