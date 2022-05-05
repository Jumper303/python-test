from base.page_base import PageBase

class SignUpPage(PageBase):
    def __init__(self, driver, config):
        super().__init__(driver)
        self.config = config

    def open_page(self):
        self.driver.get(self.config["base_url"] + "/signup")

    def register_user(self, first_name, last_name, username, password, confirm_password):
        self.type("firstName", first_name)
        self.type("lastName", last_name)
        self.type("username", username)
        self.type("password", password)
        self.type("confirmPassword", confirm_password)
