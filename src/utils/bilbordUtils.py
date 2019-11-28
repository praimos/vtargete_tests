from src.PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By


class BillboardUtils(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.list_index = [62291058, 62291041, 62291068]

    def click_checkbox(self):
        for item in self.list_index:
            self.find_element((By.XPATH, f"//div[@row-id={item}]//span[@class=\"ag-selection-checkbox\"]"),
                              time=15).click()

    def check_result(self):
        result_list = []
        for item in self.list_index:
            result_list.append(
                self.find_element((By.XPATH, f"//div[@row-id=\"{item}\"]/div[contains(text(), \"шт.\")]"),
                                  time=15).text())
        return result_list
