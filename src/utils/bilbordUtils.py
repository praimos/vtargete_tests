from src.PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By

group_index = ''


class Locators:
    LOCATOR_COUNT_ITEM = (By.XPATH, f"//div[@row-id=\"{group_index}\"]/div[contains(text(), \"шт.\")]")
    LOCATOR_CHECKBOX_ITEM = (By.XPATH, f"//div[@row-id=\"{group_index}\"]/span[contains(@class,\"unchecked\")]")


class BillboardUtils(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.list_index = [62291058, 62291041, 62291068]

    def click_checkbox(self):
        for item in self.list_index:
            global group_index
            group_index = item
            self.find_element(Locators.LOCATOR_CHECKBOX_ITEM).click()

    def check_result(self):
        result_list = []
        for item in self.list_index:
            global group_index
            group_index = item
            result_list.append(self.find_element(Locators.LOCATOR_COUNT_ITEM).text())
        return result_list
