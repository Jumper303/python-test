import random
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage

class TestClass:

    def test_login(self, setup):
        login_page = LoginPage(self.driver, self.config)
        login_page.open_page()
        assert "Cypress Real World App" in self.driver.title
        login_page.login(self.config["username"], self.config["password"])
        login_page.find_sign_out()

    def test_signup(self, setup):
        random_string = "random" + str(random.randint(0, 1000000))
        signup_page = SignUpPage(self.driver, self.config)
        signup_page.open_page()
        signup_page.register_user(random_string, random_string, random_string, random_string, random_string)
        login_page = LoginPage(self.driver, self.config)
        login_page.login(random_string, random_string)
        login_page.find_sign_out()
