import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import TestLocators


class BasePage:
    @allure.step("Инициализация базовой страницы")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Ожидание полной загрузки страницы")
    def wait_for_page_to_load(self):
        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )
        self.wait.until(
            EC.visibility_of_element_located(
                TestLocators.HEADER_CONSTRUCTOR_BUTTON
            )
        )
        self.wait.until(
            lambda driver: not any(
                overlay.is_displayed()
                for overlay in driver.find_elements(
                    *TestLocators.MODAL_OVERLAY
                )
            )
        )

    @allure.step("Поиск видимого элемента")
    def find_element_with_wait(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Поиск кликабельного элемента")
    def find_clickable_element_with_wait(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Нажатие на элемент")
    def click_on_element(self, locator):
        element = self.find_clickable_element_with_wait(locator)
        element.click()

    @allure.step("Нажатие на кнопку внутри модального окна")
    def click_child_element(self, parent_locator, child_locator):
        parent = self.find_element_with_wait(parent_locator)
        child = self.wait.until(
            lambda driver: parent.find_element(*child_locator)
        )
        self.wait.until(
            lambda driver: child.is_displayed() and child.is_enabled()
        )
        child.click()

    @allure.step("Ввод текста в поле")
    def enter_text(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание появления элемента")
    def wait_for_element_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание скрытия элемента")
    def wait_for_element_invisible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator):
        try:
            self.wait_for_element_visible(locator)
            return True
        except TimeoutException:
            return False

    @allure.step("Прокрутка элемента в область видимости")
    def scroll_element_into_view(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    @allure.step("Перетаскивание ингредиента в конструктор")
    def drag_and_drop_with_js(self, source_locator, target_locator):
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            source
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            target
        )

        self.wait.until(
            lambda driver: (
                source.is_displayed() and target.is_displayed()
            )
        )

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
        """, source, target)

    @allure.step("Получение текста всех найденных элементов")
    def get_elements_text(self, locator):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
        return [element.text for element in elements]

    @allure.step("Ожидание увеличения счётчика")
    def wait_for_counter_increase(self, locator, initial_count):
        return self.wait.until(
            lambda driver: int(
                driver.find_element(*locator).text
            ) > initial_count
        )

    @allure.step("Ожидание появления корректного текста")
    def wait_for_text_not_in(self, locator, excluded_values):
        return self.wait.until(
            lambda driver: (
                driver.find_element(*locator).text.strip()
                not in excluded_values
            )
        )

    @allure.step("Открытие страницы по URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Ожидание изменения URL")
    def wait_for_url_change(self, previous_url):
        return self.wait.until(
            EC.url_changes(previous_url)
        )

    @allure.step("Ожидание текста в одном из элементов")
    def wait_for_text_in_elements(self, locator, expected_text):
        return self.wait.until(
            lambda driver: any(
                expected_text in element.text
                for element in driver.find_elements(*locator)
            )
        )
    
    @allure.step("Ожидание изменения URL страницы")
    def wait_for_url_to_differ(self, previous_url):
        return self.wait.until(
            lambda driver: driver.current_url != previous_url
        )
    