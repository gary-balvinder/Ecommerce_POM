from selenium.webdriver.common.by import By
from locators.locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RemovePage:

    def __init__(self, driver):
        self.driver = driver

    # Finding Web Elements ============================================================
    def get_remove_from_cart(self):
        try:
            remove_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, LoginLocators.remove_from_cart)))
            return remove_button
        except:
            remove2_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, LoginLocators.remove)))
            return remove2_button

    def get_remove_button(self):
        remove3_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginLocators.remove_button)))
        return remove3_button

    # Performing actions on Web Elements ==============================================
    def click_remove_from_cart_button(self):
        self.get_remove_from_cart().click()

    def click_remove_button(self):
        self.get_remove_button().click()

    # Main function  ==================================================================
    def remove_from_cart(self):
        self.click_remove_from_cart_button()
        self.click_remove_button()
