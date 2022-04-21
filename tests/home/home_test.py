from pages.home.login_page import LoginPage
from pages.home.home_page import HomePage
import unittest
import pytest
from utilities.test_status import TestStatus
from utilities.util import Util
import os

TestStatus.__test__ = False


@pytest.mark.usefixtures('one_time_setUp', 'setUp')
class HomeTests(unittest.TestCase):
    @pytest.fixture(autouse=True)  # Using @pytest.fixture(autouse=True) makes the fixture used on all the methods within the class
    def class_setup(self, one_time_setUp):
         self.lp = LoginPage(self.driver)
         self.hp = HomePage(self.driver)
         self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_hover_on_profile(self):
        util = Util()
        util.sleep(1)
        self.lp.valid_login()
        util.sleep(15)
        self.hp.hover_profile_link()
        result = self.hp.verify_profile_hover()
        self.ts.mark_final('test_hover_on_profile', result, 'Hover over profile does not work')