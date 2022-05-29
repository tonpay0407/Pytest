from selenium.webdriver.common.by import By
import pytest

from SeleniumAutomationPractise.testData.logindata import Login_Data


class Login:

    def __init__(self, driver):
        self.driver = driver

    username_locator = (By.XPATH, "//input[@placeholder='Username']")
    password_locator = (By.XPATH, "//input[@placeholder='Password']")
    loginbtn_loc = (By.ID, "login-button")
    new_page = (By.XPATH, "//span[contains(text(), 'Products')]")
    error_msg = (By.XPATH, "//h3[@data-test='error']")

    def get_username(self):
        return self.driver.find_element(*Login.username_locator)

    def get_password(self):
        return self.driver.find_element(*Login.password_locator)

    def get_loginbtn(self):
        return self.driver.find_element(*Login.loginbtn_loc)

    def get_page(self):
        return self.driver.find_element(*Login.new_page)

    def get_error(self):
        return self.driver.find_element(*Login.error_msg)








