from base.page_base import PageBase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(PageBase):
    def __init__(self, driver, config):
        super().__init__(driver)
        self.config = config

    def open_page(self):
        self.driver.get(self.config["base_url"] + "/signin")

    def login(self, username, password):
        self.type("username", username)
        self.type("password", password)

    def find_sign_out(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='sidenav-signout']")))
