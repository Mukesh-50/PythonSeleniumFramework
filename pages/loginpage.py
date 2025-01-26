from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    #email_field = (By.ID, "email1")
   #or
    email_field_value="email1"

    password_field_value="password1"
   #or
    #password_field = (By.ID, "password1")

    login_button_value="submit-btn"
   #or
    #login_button = (By.CLASS_NAME, "submit-btn")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def login_to_application(self, email, password):
        self.type_element(email,self.email_field_value,"id") # calling 'type_element' method from 'SeleniumDriver' class from 'selenium_driver' file from 'base' package
        #Or
        #self.driver.find_element(*self.email_field).send_keys(email)

        self.type_element(password,self.password_field_value,"id")
        #or
        #self.driver.find_element(*self.password_field).send_keys(password)

        self.click_element(self.login_button_value,"class")
        #or
        #self.driver.find_element(*self.login_button).click()
