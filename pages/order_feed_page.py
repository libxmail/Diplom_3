import allure

from pages.base_page import BasePage
from locators import TestLocators


class OrderFeedPage(BasePage):

    @allure.step("Переход в ленту заказов")
    def click_order_feed_button(self):
        self.click_on_element(TestLocators.ORDER_FEED_BUTTON)

    @allure.step("Получение общего количества заказов")
    def get_total_orders_count(self):
        return int(self.get_text(TestLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_text(TestLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Получение списка заказов в работе")
    def get_orders_in_progress(self):
        return self.get_elements_text(
            TestLocators.ORDER_IN_PROGRESS_LIST
        )

    @allure.step("Ожидание увеличения общего количества заказов")
    def wait_for_total_orders_count_to_increase(self, initial_count):
        self.wait_for_counter_increase(
            TestLocators.TOTAL_ORDERS_COUNTER,
            initial_count
        )

    @allure.step("Ожидание увеличения количества заказов за сегодня")
    def wait_for_today_orders_count_to_increase(self, initial_count):
        self.wait_for_counter_increase(
            TestLocators.TODAY_ORDERS_COUNTER,
            initial_count
        )

    @allure.step("Ожидание появления заказа в списке «В работе»")
    def wait_for_orders_in_progress(self, order_number):
        self.wait_for_text_in_elements(
            TestLocators.ORDER_IN_PROGRESS_LIST,
            order_number
        )
    @allure.step("Проверка наличия заказа в разделе «В работе»")
    def is_order_in_progress(self, order_number):
        orders = self.get_orders_in_progress()
        return any(
            order_number in order
            for order in orders
        )
    