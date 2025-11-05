import pytest
from selenium import webdriver

BASE_URL = 'https://qa-desk.stand.praktikum-services.ru'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
