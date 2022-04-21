from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self, result_message):
        file_name = result_message + '.' + str(round(time.time() * 1000)) + '.png'
        screen_shot_directory = '../screenshots/'
        relative_file_name = screen_shot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destionation_file_name = os.path.join(current_directory,relative_file_name)
        destionation_directory = os.path.join(current_directory,screen_shot_directory)

        try:
            if not os.path.exists(destionation_directory):
                os.makedirs(destionation_directory)
            self.driver.save_screenshot(destionation_file_name)
            self.log.info(f'Screenshot saved to directory {destionation_file_name}')
        except:
            self.log.error('Exception occured in saving Screenshot')
            print_stack()


    def get_title(self):
        return self.driver.title

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

    def get_element_list(self, locator, locator_type='id'):
        element= None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info(f'Element list found with locator: {locator} and locator Type: {locator_type}')
        except:
            self.log.info(f'Element list not found with locator: {locator} and locator Type: {locator_type}')
        return element

    def element_click(self, locator='', locator_type='id', element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(f'Clicked on element with locator: {locator} locator_type: {locator_type}')
        except NoSuchElementException:
            self.log.info(f'Cannot click on the element with locator: {locator} locator_type: {locator_type}')
            print_stack()

    def send_keys(self, data, locator='', locator_type= 'id'):
        try:
            if locator:
                element = self.get_element(locator,locator_type)
            element.send_keys(data)
            self.log.info(f'Send data on element with locator: {locator} and locatorType: {locator_type}')
        except NoSuchElementException:
            self.log.info(f'Cannot send data on the element with locator: {locator}')
            print_stack()

    def get_text(self, locator='', locator_type='id', element= None, info=''):
        try:
            if locator:
                self.log.debug('In locator condition')
                element = self.get_element(locator, locator_type)
            self.log.debug('Before finding text')
            text = element.text
            self.log.debug(f'After finding the element, size is: {str(len(text))}')
            if len(text) == 0:
                text = element.get_attribute('innerText')
            if len(text) != 0:
                self.log.info(f'Getting text on element :: {info}')
                self.log.info(f"The text is :: {text}'")
                text = text.strip()
        except:
            self.log.error(f'Failed to get text on element {info}')
            print_stack()
            text = None
        return text

    def is_element_present(self, locator='', locator_type='id', element=''):
        try:
            if locator:
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

    def is_element_displayed(self, locator='',locator_type='', element= None):
        is_displayed = False
        try:
            if locator:
                element= self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info(f'Element is displayed with locator: {locator} and locator type: {locator_type}')
            else:
                self.log.info(f'Element not displayed with locator: {locator} and locator type: {locator_type}')

            return is_displayed
        except:
            print('Element not found')
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
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info('Element appeared on the web page')
        except:
            self.log.info('Element not appeared on the web page')
            print_stack()
        return element

    def clear_text_field(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                element.clear()
                return True
            else:
                self.log.info("Element not found")
                return False
        except NoSuchElementException:
            self.log.info("Element not found")
            return False

    def scroll_browser(self, direction='up'):
        if direction == 'up':
            self.driver.execute_script('window.scrollBy(0,-1000);')

        if direction == 'down':
            self.driver.execute_script('window.scrollBy(0,1000);')

    def get_element_attribute_value(self, attribute, element= None, locator='', locator_type='id'):
        """
        Required
        :param attribute: attribute whose value to find
        Optional
        :param element: Element whose attribute to find.
        :param locator: Locator of the element.
        :param locator_type: Locator type to find the element.
        :return: return attribute value
        """

        if locator:
            element = self.get_element(locator=locator, locator_type=locator_type)
        value = element.get_attribute(attribute)
        return value

    def is_enabled(self, locator, locator_type='id', info= ''):
        """
        Check if element is enabled

        Required:
        :param locator: locator of the element to check
        Optional:
        :param locator_type: Type of the locator(id(default),xpath, css, class, linkText
        :param info: Information about the element, label/name of the element
        :return: return if element is enabled or disabled
        """

        element = self.get_element(locator,locator_type)
        enabled = False
        try:
            attribute_value = self.get_element_attribute_value(element=element, attribute='disabled')
            if attribute_value is None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute='class')
                self.log.info(f'Attribute value from Application Web UI -->: {value}')
                enabled = not ('disabled' in value)
            if enabled:
                self.log.info(f'Element:: "{info}" is enabled')
            else:
                self.log.info(f'Element:: "{info}" is disabled')
        except:
            self.log.error(f'Element :: "{info}" state could not be found')
        return enabled

    def hover_over(self, locator='', locator_type='id'):
        if locator:
            element = self.get_element(locator=locator, locator_type=locator_type)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        try:
            if locator:
                element = self.get_element(locator=locator, locator_type=locator_type)
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
        except NoSuchElementException:
            self.log.info("Element not found")
            return False

    # def switch_frame_by_index(self, locator, locator_type='xpath'):
    #     """
    #     Required
    #     :param locator: locator of the element
    #     Optional:
    #     :param locator_type: Default value is xpath. Locator type of the element
    #     :return:  Index of iframes
    #     """
    #
    #     result = False
    #     try:
    #         iframe_list = self.get_element_list('//iframe', locator_type='xpath')
    #         self.log.info('Length of iframe list:')
    #         self.log.info(str(len(iframe_list)))
    #         for i in range(len(iframe_list)):
    #             self.sw