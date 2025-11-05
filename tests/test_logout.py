from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..data import *
from ..locators import *

# Logout пользователя
class TestLogoutUser:

    def test_logout_user(self, driver):
        
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.LOGIN_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AuthPageLocators.EMAIL_INPUT_XPATH))).send_keys(EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT_XPATH).send_keys(PSWD)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON_XPATH).click()

        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.EXIT_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.LOGIN_AND_REGISTRATION_BUTTON_XPATH)))

        assert all([len(driver.find_elements(*MainPageLocators.AVATAR_USER_CLASS_NAME)) == 0, 
            len(driver.find_elements(*MainPageLocators.TITLE_USERNAME_XPATH)) == 0
        ]), "Условия успешного логаута не выполнены"
