from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_open_main_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

def test_login_success(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()

def test_login_locked_user(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("locked out")
    expect(page).to_have_url("https://www.saucedemo.com/")
    