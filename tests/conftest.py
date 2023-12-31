import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv
from utils import attach
import tests


def path(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f'resources/{file_name}'))


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://webdriveruniversity.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '100.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
