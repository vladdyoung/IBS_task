from selenium.webdriver.common.by import By


class MainPageLocators:
    GET_USERS_BTN = (By.CSS_SELECTOR, '[data-id="users"]')
    STATUS_CODE_OF_METHODS = (By.CSS_SELECTOR, '.response-title')
    RESPONSE_BODY_OF_METHODS = (By.CSS_SELECTOR, '[data-key="output-response"]')
