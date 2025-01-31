from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from utilities.config_reader import ConfigReader


class WebDriverFactory():
    def __init__(self):
        config = ConfigReader()
        self.browser = config.get_browser()
        self.baseurl = config.get_app_url()
        self.implicit_wait = config.get_implicit_wait()
        self.page_load = config.get_page_load()
        self.script_time = config.get_script_time()
        self.timeout = config.get_timeout()
        self.cloud = config.get_value("app", "cloud").lower() == "true"  # Convert to boolean
        self.hub_url = config.get_value("grid", "hub_url")  # Get Selenium Grid URL

    def getWebDriverInstance(self):
        if self.cloud:  # Running on Selenium Grid
            print("Running tests on Selenium Grid...")
            driver = self.getRemoteDriver()
        else:  # Running locally
            print("Running tests locally...")
            driver = self.getLocalDriver()

        # Apply timeout settings
        driver.implicitly_wait(self.timeout.get("implicit_wait"))
        driver.set_page_load_timeout(self.timeout.get("page_load_timeout"))
        driver.set_script_timeout(self.timeout.get("script_timeout"))

        driver.maximize_window()
        driver.get(self.baseurl)

        return driver

    def getRemoteDriver(self):
        """Creates a remote WebDriver session for Selenium Grid execution."""
        options = self.getBrowserOptions()
        print(f"HUB URL {self.hub_url}")
        return webdriver.Remote(command_executor=self.hub_url, options=options)

    def getLocalDriver(self):
        """Creates a local WebDriver instance."""
        if self.browser == "chrome":
            return webdriver.Chrome()
        elif self.browser == "firefox":
            return webdriver.Firefox()
        elif self.browser == "edge":
            return webdriver.Edge()
        elif self.browser == "safari":
            return webdriver.Safari()
        else:
            return webdriver.Chrome()

    def getBrowserOptions(self):
        """Returns the appropriate browser options for Selenium Grid."""
        options_map = {
            "chrome": ChromeOptions(),
            "firefox": FirefoxOptions(),
            "edge": EdgeOptions(),
            "safari": SafariOptions()
        }
        return options_map.get(self.browser, ChromeOptions())  # Default to Chrome if browser not found
