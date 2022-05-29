import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path='D:\\Study\\Drivers\\chromedriver.exe')
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()
    request.cls.driver = driver # driver will be automatically passed to class driver
    yield
    driver.close()

    #add to use setup in baseclass
    #add multibrowser hook