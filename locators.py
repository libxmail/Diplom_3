from selenium.webdriver.common.by import By


class TestLocators:
    # Поля регистрации
    REG_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/parent::div//input")
    REG_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/parent::div//input")
    REG_PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    # Поля входа
    LOGIN_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/parent::div//input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Навигация
    HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")

    # Ингредиенты
    INGREDIENT_CARD = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__')]")
    INGREDIENT_COUNTER = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__')]" "//p[contains(@class, 'counter_counter__num__')]")

    # Модальные окна
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal__')]")
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal__')]")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal__')]//h2")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal__')]" "//button[contains(@class, 'Modal_modal__close_')]")
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__')]")

    # Область конструктора
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")

    # Счётчики ленты заказов
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']" "/following-sibling::p[contains(@class, 'OrderFeed_number__')]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']" "/following-sibling::p[contains(@class, 'OrderFeed_number__')]")
    ORDER_IN_PROGRESS_LIST = (By.XPATH, "//p[text()='В работе:']" "/following-sibling::ul[contains(@class, 'OrderFeed_orderList__')]//li")