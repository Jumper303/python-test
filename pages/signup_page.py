from base.page_base import PageBase

class SignUpPage(PageBase):
    def __init__(self, driver, config):
        super().__init__(driver)
        self.config = config

    def open_page(self):
        self.driver.get(self.config["base_url"] + "/signup")

    def register_user(self, firstName, lastName, username, password, confirmPassword):
        self.type("firstName", firstName)
        self.type("lastName", lastName)
        self.type("username", username)
        self.type("password", password)
        self.type("confirmPassword", confirmPassword)
