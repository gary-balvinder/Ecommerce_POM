from selenium.webdriver.common.by import By
from locators.locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCart:

    def __init__(self, driver):
        self.driver = driver
    # Add to cart ---------------------------------------------------------------------------
    # Finding Web Elements==========================================================

    def get_add_to_cart(self):
        cart_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginLocators.add_to_cart)))
        return cart_button

    def get_cart_button(self):
        return self.driver.find_element(By.XPATH, LoginLocators.cart)

    # Performing actions on Web Elements=============================================
    def click_add_to_cart_button(self):
        self.get_add_to_cart().click()

    def click_cart_button(self):
        self.get_cart_button().click()


