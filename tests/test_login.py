from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..data import *
from ..locators import *

# Login пользователя
class TestLoginUser:

    def test_login_user(self, driver):

        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.LOGIN_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AuthPageLocators.EMAIL_INPUT_XPATH))).send_keys(EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT_XPATH).send_keys(PSWD)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON_XPATH).click()

        assert all([
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.AVATAR_USER_CLASS_NAME))),
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.TITLE_USERNAME_XPATH))).text == 'User.',
        ]), "Условия успешной регистрации не выполнены"
