import time

from src.PageObjects.AuthVkPage import AuthVkPage
from src.PageObjects.HomeLkPage import HomeLkPage
from src.PageObjects.BillboardPage import BillboardPage
from src.utils.configParseUtils import vk_login, vk_password
from src.utils.bilbordUtils import BillboardUtils


def test_auth(browser):
    auth_vk_page = AuthVkPage(browser)
    auth_vk_page.go_to_site()
    auth_vk_page.input_email(vk_login)
    auth_vk_page.input_password(vk_password)
    auth_vk_page.click_button()

    home_lk_page = HomeLkPage(browser)
    time.sleep(1)
    home_lk_page.call_menu()
    time.sleep(1)
    home_lk_page.select_lk()
    home_lk_page.select_my_ad()

    billboard_page = BillboardPage(browser)
    billboard_page.wait_preloader()
    billboard_page.drop_all_filters()
    billboard_page.select_checkboxes()
    billboard_page.select_community()
    billboard_utils = BillboardUtils(browser)
    # billboard_utils.wait_element_click()
    # time.sleep(20)
    # billboard_page.delete_groups()
    billboard_utils.click_checkbox()

    billboard_utils.call_context_menu()
    billboard_utils.select_change_in_context_menu()
    # time.sleep(5)
    billboard_page.add_groups()

    # billboard_page.delete_group()
    time.sleep(4)
    billboard_page.page_refresh()
    # billboard_page.wait_preloader2()
    time.sleep(20)
    # billboard_utils.wait_element_click()
    result = billboard_utils.check_result()
    assert ['5 шт.', '5 шт.', '5 шт.'] == result
