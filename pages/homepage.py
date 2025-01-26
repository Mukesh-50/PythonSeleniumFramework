from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class HomePage(SeleniumDriver):
    #welcome_field = (By.CLASS_NAME, "welcomeMessage")
    #Or
    welcome_field="welcomeMessage"
    side_menu="//img[@alt='menu']"
    logout_field="//button[normalize-space()='Sign out']"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_welcome_text(self):
        return self.get_element(self.welcome_field,"class").text
        #or
        #return self.driver.find_element(*self.welcome_field).text

    def logout_from_application(self):
        self.click_element(self.side_menu, locatortype="xpath")
        self.click_element(self.logout_field, locatortype="xpath")
