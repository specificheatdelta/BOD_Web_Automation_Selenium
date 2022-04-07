from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging


class SeleniumDriver():

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element Found")
        except NoSuchElementException:
            self.log.info("Element not found")
        return element

    def element_click(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(f'Clicked on element with locator: {locator} locator_type: {locator_type}')
        except NoSuchElementException:
            self.log.info(f'Cannot click on the element with locator: {locator} locator_type: {locator_type}')
            print_stack()

    def send_keys(self,data, locator, locator_type = 'id'):
        try:
            element = self.get_element(locator,locator_type)
            element.send_keys(data)
            self.log.info(f'Send data on element with locator: {locator} and locatorType: {locator_type}')
        except NoSuchElementException:
            self.log.info(f'Cannot send data on the element with locator: {locator}')
            print_stack()

    def is_element_present(self, locator, locator_type):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except NoSuchElementException:
            self.log.info("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locator_type="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            print(f'Waiting for maximum :: " {str(timeout)}:: seconds for element to be clickable')
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type,
                                                             'stopFilter_stops-0')))
            self.log.info('Element appeared on the web page')
        except:
            self.log.info('Element not appeared on the web page')
            print_stack()
        return element