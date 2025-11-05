from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from ..data import *
from ..helpers import *
from ..locators import *

# Создание объявления авторизованным пользователем
class TestAdCreationByAuthorizedUser:

    def test_ad_creation_by_authorized_user(self, driver):
        
        email = generate_email_correct()
        pswd = generate_password()
        ad_title = generate_title()
        ad_description = generate_description()
        ad_price= generate_price()

        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.LOGIN_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AuthPageLocators.REGIST_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((RegistPageLocators.EMAIL_INPUT_XPATH))).send_keys(email)
        driver.find_element(*RegistPageLocators.PASSWORD_INPUT_XPATH).send_keys(pswd)
        driver.find_element(*RegistPageLocators.SUDMIT_PASSWORD_INPUT_XPATH).send_keys(pswd)
        driver.find_element(*RegistPageLocators.REGIST_BUTTON_XPATH).click()

        WebDriverWait(driver, TIMEOUT).until_not(EC.visibility_of_element_located((AdCreationPageLocators.MODAL_NOTIFICATION_XPATH)))
        WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable((MainPageLocators.POST_ADD_BUTTON_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AdCreationPageLocators.AD_TITLE_INPUT_XPATH))).send_keys(ad_title)
        driver.find_element(*AdCreationPageLocators.AD_DESCRIPTION_INPUT_XPATH).send_keys(ad_description)
        driver.find_element(*AdCreationPageLocators.AD_PRICE_INPUT_XPATH).send_keys(ad_price)
        driver.find_element(*AdCreationPageLocators.CATEGORY_DROP_DOWN_XPATH).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AdCreationPageLocators.CATEGORY_VALUE_BOOK_XPATH))).click()
        driver.find_element(*AdCreationPageLocators.SITY_DROP_DOWN_XPATH).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AdCreationPageLocators.SITY_VALUE_EKAT_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AdCreationPageLocators.CONDITION_RADIO_BUTTONS_XPATH))).click()
        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((AdCreationPageLocators.PUBLISH_BUTTON_XPATH))).click()
        driver.get(PROF_PAGE_URL)

        assert all([
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MyProfileLocators.MY_ADS_DESC_XPATH))),
            WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((MyProfileLocators.MY_AD_XPATH))).text == ad_title
        ]), "Условия успешного отображения объявления в блоке 'Мои объявления' не выполнены"

# Создание объявления неавторизованным пользователем

    def test_ad_creation_by_unauthorized_user(self, driver):

        WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located((MainPageLocators.POST_ADD_BUTTON_XPATH))).click()

        assert all([
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located(AdCreationPageLocators.MODAL_NOTIFICATION_XPATH)),
            WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located(AdCreationPageLocators.TITLE_NOTIFICATION_XPATH)).text == 'Чтобы разместить объявление, авторизуйтесь'
        ]), "Условия успешного отображения модального окна не выполнены"
