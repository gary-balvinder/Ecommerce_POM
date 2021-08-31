from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page.login_page import LoginPage
from page.search_page import SearchPage
from page.add_cart import AddCart
from page.remove_page import RemovePage


class FlipkartWebElements():

    def __init__(self, driver):
        self.driver = driver
        self.lp = LoginPage(driver)
        self.st = SearchPage(driver)
        self.ac = AddCart(driver)
        self.rp = RemovePage(driver)

    # # Login Page --------------------------------------------------------------------------

    def login(self, username, password):
        self.lp.enter_username(username)
        self.lp.enter_password(password)
        self.lp.click_login_button()

    # Search results -----------------------------------------------------------------------
    def search_bar(self, search_item):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        self.st.enter_search_term(search_item)
        self.st.click_search()

    def brand(self):
        self.st.click_brand_button()

    def product(self):
        self.st.click_product_button()

    # Add to cart ---------------------------------------------------------------------------
    def add_to_cart(self):
        self.ac.click_add_to_cart_button()

    # Remove from cart ----------------------------------------------------------------------
    def remove_from_cart(self):
        self.rp.click_remove_from_cart_button()
        self.rp.click_remove_button()

