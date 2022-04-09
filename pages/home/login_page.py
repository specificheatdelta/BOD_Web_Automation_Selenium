from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ###### LOCATORS #############
    _login_link = 'Log In'
    _email_field = 'capture_signIn_signInEmailAddress'
    _password_field = 'capture_signIn_currentPassword'
    _login_button = 'sign-in-button'

    def click_login_link(self):
        # self.get_login_link().click()
        self.element_click(self._login_link, locator_type='link')

    def enter_email(self, username):
        # self.get_email_field().send_keys(username)
        self.send_keys(data=username, locator=self._email_field)

    def enter_password(self, password):
        # self.get_password_field().send_keys(password)
        self.send_keys(data=password, locator=self._password_field)

    def click_login_button(self):
        # self.get_login_button().click()
        self.element_click(locator=self._login_button, locator_type='class')

    def clear_email(self):
        self.clear_text_field(locator=self._email_field)

    def clear_password(self):
        self.clear_text_field(locator=self._password_field)

    def login(self, username="", password=""):
        if self.driver.current_url == 'https://stage.beachbodyondemand.com/':
            self.click_login_link()
        else:
            pass
        self.clear_email()
        self.clear_password()
        self.enter_email(username)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        result = self.is_element_present(locator='#app-wrapper > div.PromotionBarStyled__Container-sc-1jdo0zd-0.gXMMdp > div > div > h4',
                                         locator_type='css')
        return result

    def verify_login_failed(self):
        result = self.is_element_present(
            locator='//div[contains(text(),"Incorrect username or password. Please try again.")]',
            locator_type='xpath')
        return result

    def verify_home_page_title(self):
        # if 'Beachbody on Demand' in self.get_title():
        #     return True
        # else:
        #     self.log.error(self.get_title())
        #     return False
        ### Below is coming from the basepage class
        return self.verify_page_title('Beachbody on Demand')



        ######### METHODS REPLACED WITH SELENIUMDRIVER CLASS METHODS ###########

        # def get_login_link(self):
        #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
        #
        # def get_email_field(self):
        #     return self.driver.find_element(By.ID, self._email_field)
        #
        # def get_password_field(self):
        #     return self.driver.find_element(By.ID, self._password_field)
        #
        # def get_login_button(self):
        #     return self.driver.find_element(By.CLASS_NAME, self._login_button)

        # login_button = self.driver.find_element(By.CLASS_NAME, 'sign-in-button')
        # login_button.click()
