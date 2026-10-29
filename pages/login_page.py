import allure

from pages.base_page import BasePage
from locators import TestLocators


class LoginPage(BasePage):

    @allure.step("Ввод электронной почты")
    def enter_email(self, email):
        self.enter_text(TestLocators.LOGIN_EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.enter_text(TestLocators.LOGIN_PASSWORD_INPUT, password)

    @allure.step("Нажатие кнопки входа")
    def click_login_button(self):
        self.click_on_element(TestLocators.LOGIN_BUTTON)

    @allure.step("Ожидание появления кнопки создания заказа")
    def wait_for_login_success(self):
        self.wait_for_element_visible(
            TestLocators.CREATE_ORDER_BUTTON
        )

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_login_success()
