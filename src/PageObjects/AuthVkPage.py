from src.PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By


class AuthVkPageLocators:
    LOCATOR_INPUT_EMAIL = (By.XPATH, "//input[@name=\"email\"]")
    LOCATOR_INPUT_PASSWORD = (By.XPATH, "//input[@name=\"pass\"]")
    LOCATOR_BUTTON_ENTER = (By.XPATH, "//button")


class AuthVkPage(BasePage):

    def input_email(self, email):
        email_input = self.find_element(AuthVkPageLocators.LOCATOR_INPUT_EMAIL)
        email_input.send_keys(email)

    def input_password(self, password):
        password_input = self.find_element(AuthVkPageLocators.LOCATOR_INPUT_PASSWORD)
        password_input.send_keys(password)

    def click_button(self):
        self.find_element(AuthVkPageLocators.LOCATOR_BUTTON_ENTER).click()
