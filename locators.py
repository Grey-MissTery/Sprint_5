from selenium.webdriver.common.by import By

class MainPageLocators: 
    LOGIN_BUTTON_XPATH = (By.XPATH, "//button[text()='Вход и регистрация']") 
    AVATAR_USER_CLASS_NAME = (By.CLASS_NAME, "svgSmall")      
    TITLE_USERNAME_XPATH = (By.XPATH, "//h3[@class='profileText name']")  
    EXIT_BUTTON_XPATH = (By.XPATH, "//button[text()='Выйти']")
    LOGIN_AND_REGISTRATION_BUTTON_XPATH = (By.XPATH, "//button[text()='Вход и регистрация']") 
    POST_ADD_BUTTON_XPATH = (By.XPATH, "//button[text()='Разместить объявление']") 

class AuthPageLocators:   
    EMAIL_INPUT_XPATH = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT_XPATH = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Войти')]") 
    REGIST_BUTTON_XPATH = (By.XPATH, "//button[text()='Нет аккаунта']")   

class RegistPageLocators: 
    EMAIL_INPUT_XPATH = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT_XPATH = (By.XPATH, "//input[@name='password']")
    SUDMIT_PASSWORD_INPUT_XPATH = (By.XPATH, "//input[@name='submitPassword']")
    REGIST_BUTTON_XPATH = (By.XPATH, "//button[text()='Создать аккаунт']")    
    ERROR_XPATH = (By.XPATH, "//span[@class='input_span__yWPqB']")
    EMAIL_FIELD_XPATH = (By.XPATH, "//input[@placeholder='Введите Email']/parent::div")
    PASSWORD_FIELD_XPATH = (By.XPATH, "//input[@placeholder='Пароль']/parent::div")
    REPEATED_PASSWORD_FIELD_XPATH = (By.XPATH, "//input[@placeholder='Повторите пароль']/parent::div")

class AdCreationPageLocators:
    MODAL_NOTIFICATION_XPATH = (By.XPATH, "//form[@class='popUp_shell__LuyqR']")
    TITLE_NOTIFICATION_XPATH = (By.XPATH, "//h1[@class='h1']") 
    AD_TITLE_INPUT_XPATH = (By.XPATH, "//input[@placeholder='Название']")
    AD_DESCRIPTION_INPUT_XPATH = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    AD_PRICE_INPUT_XPATH = (By.XPATH, "//input[@placeholder='Стоимость']")
    CATEGORY_DROP_DOWN_XPATH = (By.XPATH, "//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']")
    CATEGORY_VALUE_BOOK_XPATH = (By.XPATH, "//span[contains(text(), 'Книги')]") 
    SITY_DROP_DOWN_XPATH = (By.XPATH, "//input[@name='city']//following-sibling::button")
    SITY_VALUE_EKAT_XPATH = (By.XPATH, "//span[contains(text(), 'Екатеринбург')]") 
    CONDITION_RADIO_BUTTONS_XPATH = (By.XPATH,"//div[@class='radioUnput_inputRegular__FbVbr']")
    PUBLISH_BUTTON_XPATH = (By.XPATH,"//button[text()='Опубликовать']")

class MyProfileLocators:
    MY_ADS_DESC_XPATH = (By.XPATH, "//div[contains(@class, 'description')]")
    MY_AD_XPATH = (By.XPATH, ".//div[@class='about']/h2") 
