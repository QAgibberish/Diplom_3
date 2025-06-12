import pytest
from selenium import webdriver
from data.url import *
from pages.auth_page import AuthPage
from data.data import Credentials

@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(auth_form)
    auth_page = AuthPage(driver)
    auth_page.login(Credentials.email, Credentials.password)
    return driver