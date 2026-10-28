import allure

from data import URL
from helpers import login_user
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Stellar Burgers Tests")
class TestStellarBurgers:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_navigation_to_constructor(self, driver):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)

        driver.get(URL.BASE_URL)
        constructor_page.wait_for_page_to_load()

        order_feed_page.click_order_feed_button()
        constructor_page.click_constructor_button()

        assert constructor_page.get_current_url() == URL.BASE_URL

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_navigation_to_order_feed(self, driver):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)

        driver.get(URL.BASE_URL)
        constructor_page.wait_for_page_to_load()
        constructor_page.click_order_feed_button()

        assert order_feed_page.get_current_url() == URL.ORDER_FEED_URL

    @allure.title("Проверка появления окна с деталями ингредиента")
    def test_ingredient_modal_appears(self, driver):
        constructor_page = ConstructorPage(driver)

        driver.get(URL.BASE_URL)
        constructor_page.wait_for_page_to_load()
        constructor_page.click_on_ingredient()

        assert constructor_page.is_ingredient_modal_displayed()

    @allure.title("Проверка закрытия окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        constructor_page = ConstructorPage(driver)

        driver.get(URL.BASE_URL)
        constructor_page.wait_for_page_to_load()
        constructor_page.click_on_ingredient()

        assert constructor_page.is_ingredient_modal_displayed()

        constructor_page.close_ingredient_modal()

        assert not constructor_page.is_ingredient_modal_displayed()

    @allure.title("Проверка увеличения счётчика ингредиента")
    def test_ingredient_counter_increases(self, driver):
        constructor_page = ConstructorPage(driver)

        driver.get(URL.BASE_URL)
        constructor_page.wait_for_page_to_load()

        initial_count = constructor_page.get_ingredient_counter_value()

        constructor_page.add_ingredient_to_order()
        constructor_page.wait.until(lambda current_driver: constructor_page.get_ingredient_counter_value() > initial_count)
        new_count = constructor_page.get_ingredient_counter_value()

        assert new_count > initial_count

    @allure.title("Проверка счётчиков и появления заказа в разделе «В работе»")
    def test_order_creation_updates_counters_and_feed(self, driver, create_user):
        constructor_page = ConstructorPage(driver)
        order_feed_page = OrderFeedPage(driver)

        driver.get(URL.LOGIN_URL)
        constructor_page.wait_for_page_to_load()

        login_user(driver, create_user["email"], create_user["password"])

        constructor_page.click_order_feed_button()

        initial_total = order_feed_page.get_total_orders_count()
        initial_today = order_feed_page.get_today_orders_count()

        constructor_page.click_constructor_button()
        constructor_page.add_ingredient_to_order()
        constructor_page.click_create_order_button()

        order_number = constructor_page.get_order_number().strip()

        assert order_number, "Номер созданного заказа не отображается"

        constructor_page.close_order_modal()
        constructor_page.click_order_feed_button()

        constructor_page.wait.until(lambda current_driver: (order_feed_page.get_total_orders_count() > initial_total
                and order_feed_page.get_today_orders_count() > initial_today))

        new_total = order_feed_page.get_total_orders_count()
        new_today = order_feed_page.get_today_orders_count()

        assert new_total > initial_total
        assert new_today > initial_today

        constructor_page.wait.until(lambda current_driver: any(order_number in order
                for order in order_feed_page.get_orders_in_progress()))

        orders_in_progress = order_feed_page.get_orders_in_progress()

        assert any(order_number in order for order in orders_in_progress), (f"Заказ с номером {order_number} " "не появился в разделе «В работе»")
