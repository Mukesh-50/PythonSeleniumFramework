import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base.webdriverfactory import WebDriverFactory
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from utilities.excel_utils import ExcelUtils


@pytest.mark.usefixtures("setup")
class TestLoginScenario():
    file_path = os.path.join(os.path.dirname(__file__), "..", "testdata", "testdata.xlsx")

    @pytest.mark.parametrize("email,password", ExcelUtils.get_excel_data(file_path, "login_credentials"))
    def test_login(self, email, password):
        login = LoginPage(self.driver)

        # login.enter_email("admin@email.com") #calling a method from 'LoginPage' class

        # login.enter_password("admin@123")

        # login.click_on_login()

        # Or
        login.login_to_application(email, password)

        home = HomePage(self.driver)

        welcome_msg = home.get_welcome_text()

        assert "Welcome" in welcome_msg

        home.logout_from_application()
