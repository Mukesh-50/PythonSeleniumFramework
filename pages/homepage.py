from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class HomePage(SeleniumDriver):
    welcome_field="welcomeMessage"
    side_menu="//img[@alt='menu']"
    logout_field="//button[normalize-space()='Sign out']"

    def get_welcome_text_new_3(self):
        element = self.get_element(self.welcome_field, "class")
        if element:
            return element.text
        else:
            self.log.warning(f"Element with locator '{self.welcome_field}' not found")
            return None

    def get_welcome_text_new_3(self):
        element = self.get_element(self.welcome_field, "class")
        if element:
            return element.text
        else:
            self.log.warning(f"Element with locator '{self.welcome_field}' not found")
            return None

    
    def __init__(self,driver):
        super().__init__(driver)
        print("Call Constructor")
        print("Cons Called again By Mukesh")
        main
        self.driver=driver

    def get_welcome_text_new(self):
        element = self.get_element(self.welcome_field, "class")
        if element:
            return element.text
        else:
            self.log.warning(f"Element with locator '{self.welcome_field}' not found")
            return None

    def get_welcome_text(self):
        element = self.get_element(self.welcome_field, "class")
        if element:
            return element.text
        else:
            self.log.warning(f"Element with locator '{self.welcome_field}' not found")
            return None

    def get_welcome_text_new_2(self):
        element = self.get_element(self.welcome_field, "class")
        if element:
            return element.text
        else:
            self.log.warning(f"Element with locator '{self.welcome_field}' not found")
            return None

     def get_welcome_text_new_5(self):
        element = self.get_element(self.welcome_field, "class")
        if element:
            return element.text
        else:
            self.log.warning(f"Element with locator '{self.welcome_field}' not found")
            return None
            
    def logout_from_application(self):
        self.click_element(self.side_menu,"xpath")
        self.click_element(self.logout_field,"xpath")

    
