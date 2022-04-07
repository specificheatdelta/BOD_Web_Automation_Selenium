from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='class')
## We can read a fixture inside a fixture
def one_time_setUp(request, browser, osType):
    print('Running MODULE level one time Setup')
    if browser == 'firefox':
        baseUrl = 'https://stage.beachbodyondemand.com/'
        firefox_path = Service("C:/SeleniumDrivers/geckodriver.exe")
        driver = webdriver.Firefox(service=firefox_path)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        print('Running tests on FF')
    else:
        baseUrl = 'https://stage.beachbodyondemand.com/'
        chrome_path = Service("C:/SeleniumDrivers/chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_path)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print('Running MODULE level one time teardown')


@pytest.fixture(scope='module')
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
