from allure_commons.types import AttachmentType
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import time
from page.page import FlipkartWebElements
from config import credentials
import allure
import pytest

base_url = "https://www.flipkart.com/"
search_item = "pendrive"
options = Options()
options.headless = True
driver = Chrome(ChromeDriverManager().install(), options=options)
fwe = FlipkartWebElements(driver)


class ECommerce(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #driver.maximize_window()
        driver.get(base_url)


    @classmethod
    def tearDownClass(cls):
        driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @allure.title("Test for checking the website title")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("Website opened")
    # @pytest.mark.skip
    def test_001_Open_the_Website(self):
        self.assertIn("Online Shopping", driver.title)
        time.sleep(1)

    # @pytest.mark.skip
    @allure.title("Login Test")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Logged in")
    def test_002_Login(self):
        fwe.login(credentials.username, credentials.password)
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)

    # @pytest.mark.skip
    @allure.title("Search Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Search Item")
    def test_003_Search_results(self):
        fwe.search_bar(search_item)
        self.assertIn("pendrive", driver.current_url)
        fwe.brand()
        time.sleep(1)
        fwe.product()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

    # @pytest.mark.skip
    @allure.title("Add item to the cart test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("add to cart")
    def test_004_Add_to_cart(self):
        fwe.add_to_cart()
        time.sleep(2)

    # @pytest.mark.skip
    @allure.title("Remove item from cart test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step("Remove")
    def test_005_Remove_from_cart(self):
        fwe.remove_from_cart()
        time.sleep(1)

    # @pytest.mark.skip
    @allure.title("Invalid Login Test")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Invalid Login")
    def test_006_Login(self):
        driver.delete_all_cookies()
        driver.get("https://www.flipkart.com/")
        fwe.login(credentials.username, credentials.invalid_password)
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)

        element1 = driver.find_element(By.CSS_SELECTOR, "._2KpZ6l._2doB4z")
        m = element1.is_displayed()
        self.assertEqual("False", m, "Login Failed")


if __name__ == '__main__':
    unittest.main()
