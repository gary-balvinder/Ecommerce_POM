from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    # Finding Web Elements==============================================
    def get_search_bar(self):
        return self.driver.find_element(By.NAME, LoginLocators.search_bar)

    def get_brand(self):
        brand_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginLocators.brand_)))
        return brand_button

    def get_product(self):
        return self.driver.find_element(By.XPATH, LoginLocators.product_)

    # Performing actions on Web Elements  ===================================
    def enter_search_term(self, search_term):
        self.get_search_bar().send_keys(search_term)

    def click_search(self):
        self.get_search_bar().send_keys(Keys.ENTER)

    def click_brand_button(self):
        self.get_brand().click()

    def click_product_button(self):
        self.get_product().click()
