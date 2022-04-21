import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebDriverFactort():

    def __init__(self,browser):
        self.browser = browser

    def web_driver_instance(self):
        baseUrl = os.environ.get('BOD_STAGE_URL')
        if self.browser == 'firefox':
            firefox_path = Service("C:/SeleniumDrivers/geckodriver.exe")
            driver = webdriver.Firefox(service=firefox_path)
        elif self.browser == 'chrome':
            chrome_path = Service("C:/SeleniumDrivers/chromedriver.exe")
            driver = webdriver.Chrome(service=chrome_path)
        elif self.browser == 'IE':
            Ie_path = Service("")## Value needs to be defined. Not driver setup yet
            driver = webdriver.Ie(service=Ie_path)
        else:
            firefox_path = Service("C:/SeleniumDrivers/geckodriver.exe")
            driver = webdriver.Firefox(service=firefox_path)
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        return driver