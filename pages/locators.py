from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT = (By.ID, "id_registration-password1")
    PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
