from selenium.webdriver.common.by import By

class AuthLocators:
    EMAIL_INPUT = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    PASSWORD_INPUT = (By.XPATH, "//div[label[contains(text(),'Пароль')]]//input")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")