import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.chitai-gorod.ru")
HEADLESS = os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes")
IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture()
def driver():
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(IMPLICIT_WAIT)
    yield driver
    driver.quit()
