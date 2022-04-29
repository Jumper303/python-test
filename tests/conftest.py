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
    # before
    request.cls.driver = webdriver.Chrome('../chromedriver.exe')
    request.cls.config = config
    yield
    # after
    request.cls.driver.close()