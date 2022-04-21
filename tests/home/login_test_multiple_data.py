from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.test_status import TestStatus
from utilities.util import Util
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data
import os

TestStatus.__test__ = False
correct_email = os.environ.get('CORRECT_EMAIL')
correct_password = os.environ.get('CORRECT_PASSWORD')
incorrect_email = os.environ.get('INCORRECT_EMAIL')
incorrect_password = os.environ.get('INCORRECT_PASSWORD')


@pytest.mark.usefixtures('one_time_setUp', 'setUp')
@ddt
class LoginTests(unittest.TestCase):
    # baseUrl = 'https://stage.beachbodyondemand.com/'
    # chrome_path = Service("C:/SeleniumDrivers/chromedriver.exe")
    # driver = webdriver.Chrome(service=chrome_path)
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    @pytest.fixture(autouse=True)  # Using @pytest.fixture(autouse=True) makes the fixture used on all the methods within the class
    def class_setup(self, one_time_setUp):
         self.lp = LoginPage(self.driver)
         self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        util = Util()
        # self.driver.get(self.baseUrl)
        util.sleep(2)
        self.lp.login(correct_email, correct_password)
        util.sleep(12)
        result1 = self.lp.verify_home_page_title()
        self.ts.mark(result1,'Title is incorrect') ## Message is always the failed case message
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final('test_valid_login', result2, 'Login test was not successful')



    @pytest.mark.run(order=1)
    @data(*get_csv_data('/Users/speci/PycharmProjects/automation_framework_demo/Invalid_login_test_data.csv'))
    @unpack
    def test_invalid_password_login(self, username, password):
        # self.driver.get(self.baseUrl)
        util = Util()
        self.lp.login(username, password)
        util.sleep(1)
        result = self.lp.verify_login_failed()
        self.ts.mark_final('test_invalid_password_login', result, 'Invalid password test Failed')

    # @pytest.mark.run(order=2)
    # def test_invalid_email_login(self):
    #     # self.driver.get(self.baseUrl)
    #     self.lp.login(incorrect_email, correct_password)
    #     self.driver.implicitly_wait(10)
    #     result = self.lp.verify_login_failed()
    #     self.ts.mark_final('test_invalid_email_login', result, 'Invalid email test Failed')

