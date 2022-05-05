import pytest
import json
from selenium import webdriver

CONFIG_PATH = "../config.json"

@pytest.fixture(scope='session')
def config():
    config_file = open(CONFIG_PATH)
    return json.load(config_file)

@pytest.fixture(autouse=True, scope='function')
def setup(request, config):
    # before test
    request.cls.driver = webdriver.Chrome(config["chromedriver"])
    request.cls.config = config
    yield
    # after test
    request.cls.driver.close()