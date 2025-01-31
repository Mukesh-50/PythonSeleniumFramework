import configparser
import os


class ConfigReader:
    def __init__(self, config_path="config/config.ini"):
        # print(f"Using config file at: {config_path}")
        self.config = configparser.ConfigParser()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "../config/config.ini")
        self.config.read(config_path)

    def get_value(self, section, key):
        """Returns the value from a given section and key"""
        return self.config.get(section, key)

    def get_browser(self):
        return self.get_value("app", "browser")

    def get_app_url(self):
        return self.get_value("app", "base_url")

    def get_implicit_wait(self):
        return int(self.get_value("timeout", "implicit_wait"))

    def get_page_load(self):
        return int(self.get_value("timeout", "page_load_timeout"))

    def get_script_time(self):
        return int(self.get_value("timeout", "script_timeout"))

    def get_timeout(self):
        """Returns all timeout values as a dictionary"""
        return {
            "implicit_wait": self.get_implicit_wait(),
            "page_load_timeout": self.get_page_load(),
            "script_timeout": self.get_script_time(),
        }
