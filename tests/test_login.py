from selenium import webdriver
from SeleniumAutomationPractise.pageobjects.swagLabLogin import Login
import pytest

from SeleniumAutomationPractise.testData.logindata import Login_Data


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_checklogin(self, setup, get_data):
        obj = Login(self.driver)
        obj.get_username().send_keys(get_data["username"])
        obj.get_password().send_keys(get_data["password"])
        obj.get_loginbtn().click()
        x = obj.get_page().text
        assert x == 'PRODUCTS'

    @pytest.fixture(params=Login_Data.Login_Data_1)
    def get_data(self, request):
        return request.param

    def test_login_error(self, setup,get_data_2):
        obj1 = Login(self.driver)
        obj1.get_username().send_keys(get_data_2["username"])
        obj1.get_password().send_keys(get_data_2["password"])
        obj1.get_loginbtn().click()
        error = obj1.get_error().text
        assert "username and password" in error

    @pytest.fixture(params= Login_Data.Login_data_2)
    def get_data2(self, request):
        return request.param




