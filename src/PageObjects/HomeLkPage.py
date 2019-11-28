from src.PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By


class HomeLkPageLocators:
    LOCATOR_SELECT_AD = (By.XPATH, "//input[@placeholder=\"Выберите объявления для управления\"]")
    LOCATOR_LK_IN_MENU = (By.XPATH, "//span[text()=\"Личный кабинет\"]")
    LOCATOR_MY_AD_IN_SUB_MENU = (By.XPATH, "//span[text()=\"Мои объявления\"]")


class HomeLkPage(BasePage):

    def call_menu(self):
        self.find_element(HomeLkPageLocators.LOCATOR_SELECT_AD).click()

    def select_lk(self):
        self.find_element(HomeLkPageLocators.LOCATOR_LK_IN_MENU).click()

    def select_my_ad(self):
        self.find_element(HomeLkPageLocators.LOCATOR_MY_AD_IN_SUB_MENU).click()