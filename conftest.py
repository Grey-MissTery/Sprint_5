import pytest
from selenium import webdriver
from data import BASE_URL  # Импортируем из data.py

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()