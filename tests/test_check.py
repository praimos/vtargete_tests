from src.PageObjects.AuthVkPage import AuthVkPage
from src.PageObjects.HomeLkPage import HomeLkPage
from src.PageObjects.BillboardPage import BillboardPage
from src.utils.configParseUtils import vk_login, vk_password


def test_auth(browser):
    auth_vk_page = AuthVkPage(browser)
    auth_vk_page.go_to_site()
    auth_vk_page.input_email(vk_login)
    auth_vk_page.input_password(vk_password)
    auth_vk_page.click_button()

    home_lk_page = HomeLkPage(browser)
    home_lk_page.call_menu()
    home_lk_page.select_lk()
    home_lk_page.select_my_ad()

    billboard_page = BillboardPage(browser)
    billboard_page.wait_preloader()
    billboard_page.drop_all_filters()
    billboard_page.select_checkboxes()
    billboard_page.select_community()
    names = billboard_page.get_table_column_name()
    billboard_page.page_refresh()
    billboard_page.wait_preloader()
    
    assert "Checkboxes" and "Сообщества" in names
