import allure

from pages.base_page import BasePage
from locators import TestLocators


class ConstructorPage(BasePage):

    @allure.step("Переход в ленту заказов")
    def click_order_feed_button(self):
        self.click_on_element(TestLocators.ORDER_FEED_BUTTON)

    @allure.step("Переход в конструктор")
    def click_constructor_button(self):
        self.click_on_element(TestLocators.HEADER_CONSTRUCTOR_BUTTON)

    @allure.step("Выбор ингредиента")
    def click_on_ingredient(self):
        self.click_on_element(TestLocators.INGREDIENT_CARD)

    @allure.step("Проверка отображения окна ингредиента")
    def is_ingredient_modal_displayed(self):
        return self.is_element_visible(TestLocators.INGREDIENT_MODAL)

    @allure.step("Закрытие окна ингредиента")
    def close_ingredient_modal(self):
        self.click_on_element(TestLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_invisible(TestLocators.INGREDIENT_MODAL)

    @allure.step("Получение значения счётчика ингредиента")
    def get_ingredient_counter_value(self):
        return int(self.get_text(TestLocators.INGREDIENT_COUNTER))

    @allure.step("Ожидание увеличения счётчика ингредиента")
    def wait_for_ingredient_counter_to_increase(self, initial_count):
        self.wait_for_counter_increase(
            TestLocators.INGREDIENT_COUNTER,
            initial_count
        )   

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_to_order(self):
        self.drag_and_drop_with_js(
            TestLocators.INGREDIENT_CARD,
            TestLocators.CONSTRUCTOR_DROP_AREA
        )

    @allure.step("Нажатие кнопки создания заказа")
    def click_create_order_button(self):
        self.click_on_element(TestLocators.CREATE_ORDER_BUTTON)

    @allure.step("Закрытие окна заказа")
    def close_order_modal(self):
        self.wait_for_element_visible(TestLocators.ORDER_MODAL)
        self.click_child_element(
            TestLocators.ORDER_MODAL,
            TestLocators.MODAL_CLOSE_BUTTON
        )
        self.wait_for_element_invisible(TestLocators.ORDER_MODAL)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        locator = TestLocators.ORDER_NUMBER_IN_MODAL
        self.wait_for_text_not_in(locator, ("", "9999"))
        return self.get_text(locator).strip()
