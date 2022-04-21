from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from base.web_driver_factory import WebDriverFactort
from pages.home.login_page import LoginPage
import pytest


@pytest.fixture(scope='class')
## We can read a fixture inside a fixture
def one_time_setUp(request, browser, osType):
    print('Running MODULE level one time Setup')
    web_driver_factory = WebDriverFactort(browser)
    driver = web_driver_factory.web_driver_instance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print('Running MODULE level one time teardown')


@pytest.fixture()
def setUp(request, browser, osType):
    print('Running method level Setup')
    if browser == 'firefox':
        print('Running tests on FF')
    else:
        print('Running tests on Chrome')
    yield
    print('Running method level teardown')


def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help='Type of operating system')


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def osType(request):
    return request
