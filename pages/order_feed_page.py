from pages.base_page import BasePage
from locators import TestLocators


class OrderFeedPage(BasePage):

    def click_order_feed_button(self):
        self.click_on_element(TestLocators.ORDER_FEED_BUTTON)

    def get_total_orders_count(self):
        return int(self.get_text(TestLocators.TOTAL_ORDERS_COUNTER))

    def get_today_orders_count(self):
        return int(self.get_text(TestLocators.TODAY_ORDERS_COUNTER))

    def get_orders_in_progress(self):
        elements = self.driver.find_elements(*TestLocators.ORDER_IN_PROGRESS_LIST)
        return [element.text for element in elements]

    def wait_for_total_orders_count_to_increase(self, initial_count):
        self.wait.until(lambda driver: int(driver.find_element(*TestLocators.TOTAL_ORDERS_COUNTER).text) > initial_count)

    def wait_for_today_orders_count_to_increase(self, initial_count):
        self.wait.until(lambda driver: int(driver.find_element(*TestLocators.TODAY_ORDERS_COUNTER).text) > initial_count)
