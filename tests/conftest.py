import pytest
import json
from selenium import webdriver
from os.path import exists

CONFIG_PATH = "../config.json"

@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)

@pytest.fixture(autouse=True, scope='function')
def setup(request, config):
    # before test
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    if config["headless"]:
        options.add_argument("--headless")
    if "chromedriver" in config and exists(config["chromedriver"]):
        request.cls.driver = webdriver.Chrome(config["chromedriver"], options=options)
        request.cls.config = config
    else:
        raise Exception("chromedriver location is not set or not found")
    yield
    # after test
    request.cls.driver.close()