import pytest

from selenium import webdriver
from data import URL
from helpers import generate_email, generate_password
from pages.constructor_page import ConstructorPage
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
def constructor_page(driver):
    return ConstructorPage(driver).open()


@pytest.fixture
def create_user(driver):
    registration_page = RegistrationPage(driver).open()

    email = generate_email()
    password = generate_password()

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