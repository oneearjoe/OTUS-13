import pytest
import logging
import datetime
import allure
import json

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
        default="http://192.168.1.105:8081/",
        help="Base OpenCart URL",
    )
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler("example.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(
        "=====> Test %s started %s" % (request.node.name, datetime.datetime.now())
    )

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON,
    )

    driver.log_level = logging.INFO
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info(
        "=====> Browser %s opened at %s" % (request.node.name, datetime.datetime.now())
    )

    driver.base_url = base_url
    driver.implicitly_wait(5)

    yield driver

    if request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name=request.function.__name__,
            attachment_type=allure.attachment_type.PNG,
        )

    driver.quit()
