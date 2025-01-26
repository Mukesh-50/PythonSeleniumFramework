from selenium import webdriver

from utilities.config_reader import ConfigReader


class WebDriverFactory():
    def __init__(self,browser):
        config=ConfigReader()
        self.browser=config.get_browser()
        self.baseurl=config.get_app_url()
        self.implicit_wait=config.get_implicit_wait()
        self.page_load=config.get_page_load()
        self.script_time=config.get_script_time()
        self.timeout=config.get_timeout()

    def getWebDriverInstance(self):

        if self.browser=="chrome":
            driver=webdriver.Chrome()
        elif self.browser=="firefox":
            driver=webdriver.Firefox()
        elif self.browser=="edge":
            driver=webdriver.Edge()
        elif self.browser=="safari":
            driver=webdriver.Safari()
        else:
            driver=webdriver.Chrome()

        #driver.implicitly_wait(self.implicit_wait)
        #or
        driver.implicitly_wait(self.timeout.get("implicit_wait"))

        #driver.set_page_load_timeout(self.page_load)
        #or
        driver.set_page_load_timeout(self.timeout.get("page_load_timeout"))

        #driver.set_script_timeout(self.script_time)
        #or
        driver.set_script_timeout(self.timeout.get("script_timeout"))

        driver.maximize_window()
        driver.get(self.baseurl)

        return driver