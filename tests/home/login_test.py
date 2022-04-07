from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.home.login_page import LoginPage
import unittest
from base.selenium_driver import SeleniumDriver
import pytest

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

    @pytest.mark.run(order=3)
    def test_valid_login(self):
        # self.driver.get(self.baseUrl)
        self.lp.login('fahadbod@yopmail.com', 'Beach1234')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR,
                            'body > div.GroupsModalStyled__StyledGroupsModal-gbomg-14.jKoVmT > div > div > div > div > div > div > img').click()
        self.driver.implicitly_wait(8)
        result = self.lp.verify_login_successful()
        assert result == True


    @pytest.mark.run(order=1)
    def test_invalid_password_login(self):
        # self.driver.get(self.baseUrl)
        self.lp.login('fahadbod@yopmail.com', 'Beach')
        self.driver.implicitly_wait(10)
        result = self.lp.verify_login_failed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_invalid_email_login(self):
        # self.driver.get(self.baseUrl)
        self.lp.login('fahad45@yopmail.com', 'Beach1234')
        self.driver.implicitly_wait(10)
        result = self.lp.verify_login_failed()
        assert result == True

