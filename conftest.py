import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope='class')
def driver():
    project_root = os.path.abspath(os.path.dirname(__file__))
    driver_path = os.path.join(project_root, 'drivers', 'chromedriver.exe')

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def env_vars():
    return {
        "url": os.getenv('URL'),
        "standard_user": os.getenv('STANDARD_USER'),
        "locked_out_user": os.getenv('LOCK_OUT_USER'),
        "password": os.getenv('PASSWORD')
    }
