import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import URL
from helpers import generate_email, generate_password
from locators import TestLocators


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
    wait = WebDriverWait(driver, 20)

    email = generate_email()
    password = generate_password()

    driver.get(URL.REGISTER_URL)

    wait.until(lambda current_driver: not any(overlay.is_displayed() for overlay in current_driver.find_elements(*TestLocators.MODAL_OVERLAY)))

    name_input = wait.until(EC.visibility_of_element_located(TestLocators.REG_NAME_INPUT))
    email_input = wait.until(EC.visibility_of_element_located(TestLocators.REG_EMAIL_INPUT))
    password_input = wait.until(EC.visibility_of_element_located(TestLocators.REG_PASSWORD_INPUT))

    name_input.send_keys("Sergei Fedotov")
    email_input.send_keys(email)
    password_input.send_keys(password)

    wait.until(lambda current_driver: not any(overlay.is_displayed() for overlay in current_driver.find_elements(*TestLocators.MODAL_OVERLAY)))

    register_button = wait.until(EC.element_to_be_clickable(TestLocators.REG_BUTTON))
    register_button.click()

    wait.until(lambda current_driver: (current_driver.current_url != URL.REGISTER_URL))

    return {"email": email, "password": password}