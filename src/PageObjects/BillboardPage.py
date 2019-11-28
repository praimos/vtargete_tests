from src.PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BillboardPageLocators:
    LOCATOR_ECENTERCONTAINER = (By.XPATH, "//div[@ref=\"eCenterContainer\"]")
    LOCATOR_ACTIVITY_IN_GROUPS = (By.XPATH, "//span[text()=\"Активность в сообществах\"]")
    LOCATOR_TABLE_COLUMN_NAME = (By.XPATH, "//div[@role=\"presentation\"]/span[text()]")
    LOCATOR_CHECKBOX_ALL_FILTERS_UNCHECKED = (By.XPATH,
                                              "//div[@ref=\"eSelect\"]/span[contains(@class, \"ag-icon-checkbox-unchecked\")]")
    LOCATOR_CHECKBOX_ALL_FILTERS_CHECKED = (By.XPATH,
                                              "//div[@ref=\"eSelect\"]/span[contains(@class, \"ag-icon-checkbox-checked\")]")
    LOCATOR_CHECKBOX_ALL_FILTERS_INDETERMINATE = (By.XPATH,
                                              "//div[@ref=\"eSelect\"]/span[contains(@class, \"ag-icon-checkbox-indeterminate\")]")
    LOCATOR_PRELOADER = (By.XPATH, "//div[@class=\"el-loading-spinner\"]")
    LOCATOR_FILTER_CHECKBOXES = (By.XPATH, "//span[text()=\"Checkboxes\"]")
    LOCATOR_FILTER_COMMUNITY = (By.XPATH, "//span[text()=\"Сообщества\"]")
    LOCATOR_BUTTON_REFRESH = (By.XPATH, "//span/i[text()=\"refresh\"]")


class BillboardPage(BasePage):

    def wait_visibility_element(self, time=45):
        WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(
                BillboardPageLocators.LOCATOR_ECENTERCONTAINER))

    def click_on_activity_in_groups(self):
        self.find_element(BillboardPageLocators.LOCATOR_ACTIVITY_IN_GROUPS).click()

    def drop_all_filters(self):
        self.find_element(BillboardPageLocators.LOCATOR_CHECKBOX_ALL_FILTERS_INDETERMINATE).click()
        self.find_element(BillboardPageLocators.LOCATOR_CHECKBOX_ALL_FILTERS_CHECKED).click()

    def get_table_column_name(self):
        all_item = self.find_elements(BillboardPageLocators.LOCATOR_TABLE_COLUMN_NAME)
        all_names = [x.text for x in all_item if len(x.text) > 0]
        return all_names

    def wait_preloader(self, time=15):
        WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(
            BillboardPageLocators.LOCATOR_PRELOADER))
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(
            BillboardPageLocators.LOCATOR_PRELOADER))

    def select_checkboxes(self):
        self.find_element(BillboardPageLocators.LOCATOR_FILTER_CHECKBOXES).click()

    def select_community(self):
        self.find_element(BillboardPageLocators.LOCATOR_FILTER_COMMUNITY).click()

    def page_refresh(self):
        self.find_element(BillboardPageLocators.LOCATOR_BUTTON_REFRESH).click()
