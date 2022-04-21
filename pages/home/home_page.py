from base.basepage import BasePage
import utilities.custom_logger as cl
import logging


class HomePage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    ###### LOCATORS #############
    _profile_link_locator_css = '#unification-topNav > div > div > header > div.topNavAccountStyled__MenuOptions-sc-1oihx9h-0.lodnEd > div.dropdownStyled__DropdownWrapper-sc-1akxl18-0.iVfcWy > button > img'
    _shop_header_locator_text = 'shop'
    _bod_header_locator_text = 'Beachbody On Demand'
    _nutrition_header_locator_text = 'Nutrition'
    _BODgroups_header_locator_text = 'BODgroups'
    _JoinUs_header_locator_text = 'Join Us'
    _More_header_locator_text = 'More'
    _profile_email_dropdown_locator_class = 'desktopNavStyled__ItemText-sc-1lvzjju-3'

    def hover_profile_link(self):
        self.hover_over(locator=self._profile_link_locator_css,locator_type='css')

    def verify_profile_hover(self):
        result = self.is_element_present(locator=self._profile_email_dropdown_locator_class,locator_type='class')
        return result

    def navigate_to_dashboard(self):
        self.hover_profile_link()
        self.element_click(locator=self._profile_email_dropdown_locator_class,locator_type='class')


