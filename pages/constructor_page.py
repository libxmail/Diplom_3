from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators import TestLocators


class ConstructorPage(BasePage):

    def click_order_feed_button(self):
        self.click_on_element(TestLocators.ORDER_FEED_BUTTON)

    def click_constructor_button(self):
        self.click_on_element(TestLocators.HEADER_CONSTRUCTOR_BUTTON)

    def click_on_ingredient(self):
        self.click_on_element(TestLocators.INGREDIENT_CARD)

    def is_ingredient_modal_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(TestLocators.INGREDIENT_MODAL))
            return True
        except TimeoutException:
            return False

    def close_ingredient_modal(self):
        self.click_on_element(TestLocators.MODAL_CLOSE_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(TestLocators.INGREDIENT_MODAL))

    def get_ingredient_counter_value(self):
        return int(self.get_text(TestLocators.INGREDIENT_COUNTER))

    def add_ingredient_to_order(self):
        ingredient = self.find_element_with_wait(TestLocators.INGREDIENT_CARD)
        drop_area = self.find_element_with_wait(TestLocators.CONSTRUCTOR_DROP_AREA)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ingredient)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", drop_area)

        self.wait.until(lambda driver: (ingredient.is_displayed() and drop_area.is_displayed()))

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
        """, ingredient, drop_area)

    def click_create_order_button(self):
        self.click_on_element(TestLocators.CREATE_ORDER_BUTTON)

    def close_order_modal(self):
        modal = self.wait.until(EC.visibility_of_element_located(TestLocators.ORDER_MODAL))
        close_button = modal.find_element(*TestLocators.MODAL_CLOSE_BUTTON)

        self.wait.until(lambda driver: (
            close_button.is_displayed()
            and close_button.is_enabled()
            and driver.execute_script("""
                const button = arguments[0];
                const rect = button.getBoundingClientRect();
                const x = rect.left + rect.width / 2;
                const y = rect.top + rect.height / 2;
                const element = document.elementFromPoint(x, y);

                return element === button || button.contains(element);
            """, close_button)))

        close_button.click()

        self.wait.until(EC.invisibility_of_element_located(TestLocators.ORDER_MODAL))

    def get_order_number(self):
        locator = TestLocators.ORDER_NUMBER_IN_MODAL

        self.wait.until(lambda driver: (driver.find_element(*locator).text.strip()not in ("", "9999")))

        return self.get_text(locator).strip()
    