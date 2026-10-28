from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import TestLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_page_to_load(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        self.wait.until(EC.visibility_of_element_located(TestLocators.HEADER_CONSTRUCTOR_BUTTON))

        self.wait.until(lambda driver: not any(overlay.is_displayed()for overlay in driver.find_elements(*TestLocators.MODAL_OVERLAY)))

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable_element_with_wait(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_on_element(self, locator):
        element = self.find_clickable_element_with_wait(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def get_current_url(self):
        return self.driver.current_url