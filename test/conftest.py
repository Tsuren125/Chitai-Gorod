import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


base_url = "https://www.chitai-gorod.ru/"


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(7)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='50%'")
    driver.get(base_url)
    yield driver
    driver.quit()
