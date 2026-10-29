import allure

from pages.base_page import BasePage
from locators import TestLocators


class RegistrationPage(BasePage):

    @allure.step("Ввод имени при регистрации")
    def enter_name(self, name):
        self.enter_text(TestLocators.REG_NAME_INPUT, name)

    @allure.step("Ввод электронной почты при регистрации")
    def enter_email(self, email):
        self.enter_text(TestLocators.REG_EMAIL_INPUT, email)

    @allure.step("Ввод пароля при регистрации")
    def enter_password(self, password):
        self.enter_text(TestLocators.REG_PASSWORD_INPUT, password)

    @allure.step("Нажатие кнопки регистрации")
    def click_register_button(self):
        self.click_on_element(TestLocators.REG_BUTTON)

    @allure.step("Ожидание завершения регистрации")
    def wait_for_registration_success(self, register_url):
        self.wait_for_url_to_differ(register_url)        

    @allure.step("Регистрация пользователя")
    def register(self, name, email, password, register_url):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register_button()
        self.wait_for_registration_success(register_url)
