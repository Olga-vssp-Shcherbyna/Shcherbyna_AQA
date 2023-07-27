from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class TranslatePage(BasePage):
    URL = "https://translate.google.com.ua/?hl=uk&sl=uk&tl=en"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        time.sleep(2)
        self.driver.get(TranslatePage.URL)

    def try_translate(self, text):
        # Знаходимо поле, в яке будемо вводити текст для перекладу

        login_elem = self.driver.find_element(By.CLASS_NAME, "er8xn")

        # Вводимо текст
        login_elem.send_keys(text)

    def check_translated_text(self, expected_text):
        time.sleep(3)
        return self.driver.find_element(By.CLASS_NAME, "ryNqvb").text == expected_text

    def check_svg_button_text(self, expected_text):
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "tQLSFf").click()
        time.sleep(3)
        return self.driver.find_element(By.CLASS_NAME, "vz0Gtd").text == expected_text
