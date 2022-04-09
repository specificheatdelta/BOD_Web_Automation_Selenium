from pages.home.login_page import LoginPage
import unittest
import time
import pytest
from utilities.test_status import TestStatus
from utilities.util import Util

@pytest.mark.usefixtures('one_time_setUp', 'setUp')
class LoginTests(unittest.TestCase):
    # baseUrl = 'https://stage.beachbodyondemand.com/'
    # chrome_path = Service("C:/SeleniumDrivers/chromedriver.exe")
    # driver = webdriver.Chrome(service=chrome_path)
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    @pytest.fixture(
        autouse=True)  # Using @pytest.fixture(autouse=True) makes the fixture used on all the methods within the class
    def class_setup(self, one_time_setUp):
         self.lp = LoginPage(self.driver)
         self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=3)
    def test_valid_login(self):
        util = Util()
        # self.driver.get(self.baseUrl)
        util.sleep(2)
        self.lp.login('fahadbod@yopmail.com', 'Beach1234')
        util.sleep(7)
        ## New badges popup element below. Has been removed in new web build##
        # self.driver.find_element(By.CSS_SELECTOR,
        #                     'body > div.GroupsModalStyled__StyledGroupsModal-gbomg-14.jKoVmT > div > div > div > div > div > div > img').click()
        result1 = self.lp.verify_home_page_title()
        self.ts.mark(result1,'Title is incorrect') ## Message is always the failed case message
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final('test_valid_login', result2, 'Login test was not successful')



    @pytest.mark.run(order=1)
    def test_invalid_password_login(self):
        # self.driver.get(self.baseUrl)
        self.lp.login('fahadbod@yopmail.com', 'Beach')
        self.driver.implicitly_wait(10)
        result = self.lp.verify_login_failed()
        self.ts.mark_final('test_invalid_password_login', result, 'Invalid password test Failed')


    @pytest.mark.run(order=2)
    def test_invalid_email_login(self):
        # self.driver.get(self.baseUrl)
        self.lp.login('fahad45@yopmail.com', 'Beach1234')
        self.driver.implicitly_wait(10)
        result = self.lp.verify_login_failed()
        self.ts.mark_final('test_invalid_email_login', result, 'Invalid email test Failed')

