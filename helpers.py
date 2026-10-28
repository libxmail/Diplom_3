import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import TestLocators


def generate_email():
    random_digits = random.randint(1000, 9999)
    return f"sergei_fedotov_53_{random_digits}@yandex.ru"


def generate_password():
    return str(random.randint(100000, 999999))


def login_user(driver, email, password):
    wait = WebDriverWait(driver, 15)

    email_input = wait.until(EC.visibility_of_element_located(TestLocators.LOGIN_EMAIL_INPUT))
    email_input.clear()
    email_input.send_keys(email)

    password_input = wait.until(EC.visibility_of_element_located(TestLocators.LOGIN_PASSWORD_INPUT))
    password_input.clear()
    password_input.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON))
    login_button.click()

    wait.until(EC.visibility_of_element_located(TestLocators.CREATE_ORDER_BUTTON))
