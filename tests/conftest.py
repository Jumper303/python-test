import pytest
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from helpers.webdriver_listener import WebDriverListener

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
    request.cls.driver = EventFiringWebDriver(
        webdriver.Chrome(ChromeDriverManager().install(), options=options),
        WebDriverListener()
    )
    request.cls.config = config
    yield
    # after test
    request.cls.driver.close()