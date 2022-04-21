from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class DashboardPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    ###### LOCATORS #############
    _profile_name_class = 'Headline1dm-sue2mw-0 HeaderStyled__ProfileName-mwxchp-5'
    _shop_header_locator_text = 'shop'

    def verify_navigate_to_dashboard(self):
        result = self.is_element_present(locator=self._profile_name_class, locator_type='class')
        return result