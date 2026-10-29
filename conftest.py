import pytest

from selenium import webdriver
from data import URL
from helpers import generate_email, generate_password
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage


@pytest.fixture(params=["chrome", "firefox"], ids=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def create_user(driver):
    base_page = BasePage(driver)
    registration_page = RegistrationPage(driver)

    email = generate_email()
    password = generate_password()

    base_page.open_url(URL.REGISTER_URL)
    base_page.wait_for_page_to_load()

    registration_page.register(
        "Sergei Fedotov",
        email,
        password,
        URL.REGISTER_URL
    )

    return {
        "email": email,
        "password": password
    }
