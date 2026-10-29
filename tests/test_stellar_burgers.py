import allure

from data import URL
from pages.base_page import BasePage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Stellar Burgers Tests")
class TestStellarBurgers:
    
    @allure.step("Открытие главной страницы конструктора")
    def open_constructor(self, driver):
        base_page = BasePage(driver)
        base_page.open_url(URL.BASE_URL)
        base_page.wait_for_page_to_load()
        return ConstructorPage(driver)

    @allure.step("Авторизация пользователя")
    def login_user(self, driver, user):
        base_page = BasePage(driver)
        base_page.open_url(URL.LOGIN_URL)
        base_page.wait_for_page_to_load()

        login_page = LoginPage(driver)
        login_page.login(user["email"], user["password"])

    @allure.step("Создание заказа")
    def create_order(self, driver, user):
        self.login_user(driver, user)

        constructor_page = ConstructorPage(driver)
        constructor_page.add_ingredient_to_order()
        constructor_page.click_create_order_button()

        order_number = constructor_page.get_order_number()
        constructor_page.close_order_modal()

        return order_number

    @allure.title("Переход в конструктор")
    def test_navigation_to_constructor(self, driver):
        constructor_page = self.open_constructor(driver)
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.click_order_feed_button()
        constructor_page.click_constructor_button()

        assert constructor_page.get_current_url() == URL.BASE_URL

    @allure.title("Переход в ленту заказов")
    def test_navigation_to_order_feed(self, driver):
        constructor_page = self.open_constructor(driver)
        constructor_page.click_order_feed_button()

        order_feed_page = OrderFeedPage(driver)

        assert order_feed_page.get_current_url() == URL.ORDER_FEED_URL

    @allure.title("Появление окна с деталями ингредиента")
    def test_ingredient_modal_appears(self, driver):
        constructor_page = self.open_constructor(driver)
        constructor_page.click_on_ingredient()

        assert constructor_page.is_ingredient_modal_displayed()

    @allure.title("Закрытие окна с деталями ингредиента")
    def test_close_ingredient_modal(self, driver):
        constructor_page = self.open_constructor(driver)
        constructor_page.click_on_ingredient()
        constructor_page.close_ingredient_modal()

        assert not constructor_page.is_ingredient_modal_displayed()

    @allure.title("Увеличение счётчика ингредиента после добавления")
    def test_ingredient_counter_increases(self, driver):
        constructor_page = self.open_constructor(driver)
        initial_count = constructor_page.get_ingredient_counter_value()

        constructor_page.add_ingredient_to_order()
        constructor_page.wait_for_ingredient_counter_to_increase(
            initial_count
        )
        new_count = constructor_page.get_ingredient_counter_value()

        assert new_count > initial_count

    @allure.title("Отображение номера после создания заказа")
    def test_order_number_is_displayed(self, driver, create_user):
        order_number = self.create_order(driver, create_user)

        assert order_number

    @allure.title("Увеличение общего счётчика заказов")
    def test_total_orders_count_increases(self, driver, create_user):
        self.login_user(driver, create_user)

        constructor_page = ConstructorPage(driver)
        constructor_page.click_order_feed_button()

        order_feed_page = OrderFeedPage(driver)
        initial_count = order_feed_page.get_total_orders_count()

        constructor_page.click_constructor_button()
        constructor_page.add_ingredient_to_order()
        constructor_page.click_create_order_button()
        constructor_page.get_order_number()
        constructor_page.close_order_modal()

        constructor_page.click_order_feed_button()
        order_feed_page.wait_for_total_orders_count_to_increase(
            initial_count
        )
        new_count = order_feed_page.get_total_orders_count()

        assert new_count > initial_count       

    @allure.title("Увеличение счётчика заказов за сегодня")
    def test_today_orders_count_increases(self, driver, create_user):
        self.login_user(driver, create_user)

        constructor_page = ConstructorPage(driver)
        constructor_page.click_order_feed_button()

        order_feed_page = OrderFeedPage(driver)
        initial_count = order_feed_page.get_today_orders_count()

        constructor_page.click_constructor_button()
        constructor_page.add_ingredient_to_order()
        constructor_page.click_create_order_button()
        constructor_page.get_order_number()
        constructor_page.close_order_modal()

        constructor_page.click_order_feed_button()
        order_feed_page.wait_for_today_orders_count_to_increase(
            initial_count
        )
        new_count = order_feed_page.get_today_orders_count()

        assert new_count > initial_count       

    @allure.title("Появление созданного заказа в разделе «В работе»")
    def test_created_order_appears_in_progress(self, driver, create_user):
        order_number = self.create_order(driver, create_user)

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_order_feed_button()
        order_feed_page.wait_for_orders_in_progress(order_number)

        assert order_feed_page.is_order_in_progress(order_number)
