from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PageBase:
    def __init__(self, driver):
        self.driver = driver

    def type(self, id, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id)))
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)
