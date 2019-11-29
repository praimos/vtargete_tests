from src.PageObjects.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_log(opa):
    with open("file.log", "a+") as log:
        log.write(opa)


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
    LOCATOR_DELETE_ITEM_MENU = (By.CSS_SELECTOR, "body > div:nth-child(14) > div.el-scrollbar > div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li.el-select-dropdown__item")
    LOCATOR_SELECT_ACTION = (By.XPATH, "//input[@placeholder=\"Выберите действие\"]")
    LOCATOR_ALL_GROUPS = (By.XPATH, "//label[contains(@class, \"box\")]")
    LOCATOR_ENTER_ON_FORM = (By.XPATH, "//button[@class='el-button el-button--info el-button--mini']")
    LOCATOR_SAVE_CHANGES = (By.XPATH, "//*[@id=\"app\"]/section/section/header/div/div[1]/div[4]/button[2]")
    LOCATOR_SEARCH_G = (By.XPATH, "//input[@placeholder=\"Название...\"]")


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

    def delete_group(self):
        self.find_element(BillboardPageLocators.LOCATOR_SELECT_ACTION).click()
        self.driver.set_page_load_timeout(15)
        menu_item = self.find_elements(BillboardPageLocators.LOCATOR_DELETE_ITEM_MENU)
        menu_item.click()
        list_groups = self.find_elements(BillboardPageLocators.LOCATOR_ALL_GROUPS)
        if list_groups != '':
            for group in list_groups:
                group.click()
        self.find_element(BillboardPageLocators.LOCATOR_ENTER_ON_FORM).click()
        self.find_element(BillboardPageLocators.LOCATOR_SAVE_CHANGES).click()

    def add_groups(self):
        self.find_element(BillboardPageLocators.LOCATOR_SEARCH_G).send_keys("Cats")
        groups = self.find_elements(BillboardPageLocators.LOCATOR_ALL_GROUPS)
        index = 5
        for item in groups:
            if index != 0:
                item.click()
                index -= 1
            else:
                break
        self.find_element(BillboardPageLocators.LOCATOR_ENTER_ON_FORM).click()
        self.find_element(BillboardPageLocators.LOCATOR_SAVE_CHANGES).click()


