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
    # Стандартная обработка результата теста
    outcome = yield
    rep = outcome.get_result()

    # Прикрепляем данные только при падении теста (можно расширить для других случаев)
    if rep.when == "call" and rep.failed:
        browser = item.funcargs.get("browser")
        if browser:
            # Скриншот при падении
            allure.attach(
                browser.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    # Сохраняем результат для других хуков/фикстур
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def logger(request):
    log_level = request.config.getoption("--log_level")
    test_logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler("example.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    test_logger.addHandler(file_handler)
    test_logger.setLevel(level=log_level)
    test_logger.info(f"Test {request.node.name} started at {datetime.datetime.now()}")
    yield test_logger
    test_logger.info(f"Test {request.node.name} finished at {datetime.datetime.now()}")


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

    # Прикрепляем capabilities браузера в Allure
    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON,
    )

    driver.logger = logger
    driver.test_name = request.node.name
    driver.base_url = base_url
    driver.implicitly_wait(5)

    logger.info(f"Browser {browser_name} started")
    yield driver
    logger.info(f"Browser {browser_name} closed")
    driver.quit()