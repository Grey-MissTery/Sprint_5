from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..data import *
from ..locators import *
from ..helpers import *

# Все тесты регистрации в одном классе
class TestRegistration:

    def test_registration_new_user(self, driver):
        email = generate_email_correct()
        pswd = generate_password()
        
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.LOGIN_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AuthPageLocators.REGIST_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.EMAIL_INPUT_XPATH))).send_keys(email)
        driver.find_element(*RegistPageLocators.PASSWORD_INPUT_XPATH).send_keys(pswd)
        driver.find_element(*RegistPageLocators.SUDMIT_PASSWORD_INPUT_XPATH).send_keys(pswd)
        driver.find_element(*RegistPageLocators.REGIST_BUTTON_XPATH).click()

        assert all([
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.AVATAR_USER_CLASS_NAME))).is_displayed(),
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.TITLE_USERNAME_XPATH))).text == 'User.'
        ]), "Условия успешной регистрации не выполнены"

    def test_registration_existing_user(self, driver):
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.LOGIN_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AuthPageLocators.REGIST_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.EMAIL_INPUT_XPATH))).send_keys(EMAIL)
        driver.find_element(*RegistPageLocators.REGIST_BUTTON_XPATH).click()

        assert all([
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.ERROR_XPATH))).text == 'Ошибка',
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.EMAIL_FIELD_XPATH))).value_of_css_property("border-color") == 'rgb(255, 105, 114)',
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.PASSWORD_FIELD_XPATH))).value_of_css_property("border-color") == 'rgb(255, 105, 114)',
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.REPEATED_PASSWORD_FIELD_XPATH))).value_of_css_property("border-color") == 'rgb(255, 105, 114)'
        ]), "Не все условия ошибки регистрации существующего пользователя выполнены"
        
    def test_registration_new_user_invalid_email(self, driver):
        email = generate_email_invalid()
                
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.LOGIN_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AuthPageLocators.REGIST_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.EMAIL_INPUT_XPATH))).send_keys(email)
        driver.find_element(*RegistPageLocators.REGIST_BUTTON_XPATH).click()
        
        assert all([
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.ERROR_XPATH))).text == 'Ошибка',
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.EMAIL_FIELD_XPATH))).value_of_css_property("border-color") == 'rgb(255, 105, 114)',
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.PASSWORD_FIELD_XPATH))).value_of_css_property("border-color") == 'rgb(255, 105, 114)',
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.REPEATED_PASSWORD_FIELD_XPATH))).value_of_css_property("border-color") == 'rgb(255, 105, 114)'
        ]), "Не все условия ошибки регистрации выполнены"