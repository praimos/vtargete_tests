from selenium.webdriver import ActionChains

from src.PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By
from src.PageObjects.BillboardPage import BillboardPageLocators


class BillboardUtils(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.list_index = [62291041, 62291047, 61073610]

    def click_checkbox(self):
        for item in self.list_index:
            self.find_element((By.XPATH, f"//div[@row-id={item}]//span[@class=\"ag-selection-checkbox\"]"),
                              time=15).click()

    def check_result(self):
        result_list = []
        for item in self.list_index:
            res = self.find_element((By.XPATH, f"//div[@row-id=\"{item}\"]/div/span/div")).text
            result_list.append(str(res))
        return result_list

    def call_context_menu(self):
        item = self.list_index[0]
        element = self.find_element((By.XPATH, f"//div[@row-id=\"{item}\"]/div/span"),
                                    time=15)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def select_change_in_context_menu(self):
        self.find_element((By.XPATH, "//*[@id=\"eIcon\"]/span/div[@class=\"el-popover__reference\"]"),
                          time=15).click()
