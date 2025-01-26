import logging
import os
from datetime import datetime
from traceback import print_stack

from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, \
    ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import utilities.custom_logger as cl


class SeleniumDriver():
    log = cl.customlogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def take_screenshot(self):
        try:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")  # cwd is current working directory

            #timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            timestamp = datetime.now().strftime("%H_%M_%S_%d_%m_%Y")

            file_name=f"Automation_{timestamp}.png"

            filepath=os.path.join(screenshot_dir, file_name)

            self.driver.save_screenshot(filepath)

            return filepath
        except Exception as e:
            print(f"Could not capture screenshot {e}")

            return None

    def get_by_type(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partial_link":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            self.log.info("Locator Type " + locatorType + "not supported")

    def get_element(self, locator, locatorType="id"):
        element = None
        try:
            locatorytype = locatorType.lower()
            bytype = self.get_by_type(locatorytype)
            element = self.driver.find_element(bytype, locator)
            print("Element Found")
            self.log.info("Element Found Using " + locatorType + " with value " + locator)
        except:
            self.log.warning("Element Not Found Using " + locatorType + " with value " + locator)

        return element

    def click_element(self, locator, locatortype="id"):
        try:
            element = self.get_element(locator, locatortype)
            element.click()
            print("Clicked on element")
            self.log.info("Clicked on element with locator value " + locator)
        except:
            self.log.warning("Could not click on element with locator value " + locator)
            print_stack()

    def type_element(self, data, locator, locatortype="id"):
        try:
            element = self.get_element(locator, locatortype)
            element.send_keys(data)
            print("Typed data on element")
            self.log.info("Typed" + data + "on element with locator " + locator)
        except:
            self.log.info("Could not type " + data + "on element with locator " + locator)
            print_stack()

    def waitforelement(self, locator, locatortype="id", timeout=30):
        element = None
        try:
            bytype = self.get_by_type(locatortype)
            wait = WebDriverWait(self.driver, timeout, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, StaleElementReferenceException,
                                                     ElementNotInteractableException, ElementNotVisibleException])
            element = wait.until(expected_conditions.element_to_be_clickable((bytype)))
            print("Element Found With Explicit Conditions")
        except:
            print("Element Not Found Within Time Interval")

        return element
