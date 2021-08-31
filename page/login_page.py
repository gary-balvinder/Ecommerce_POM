from selenium.webdriver.common.by import By
from locators.locators import LoginLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Finding Web Elements=========================================

    def get_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, LoginLocators.username_)

    def get_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, LoginLocators.password_)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, LoginLocators.login_button)

        # Performing actions on Web Elements=============================
    def enter_username(self, username):
        self.get_username().send_keys(username)

    def enter_password(self, password):
        self.get_password().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()
