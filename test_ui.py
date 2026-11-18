from playwright.sync_api import Page, expect


def test_open_main_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")

def test_login_success(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products")).to_be_visible()

def test_login_locked_user(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text("locked out")
    expect(page).to_have_url("https://www.saucedemo.com/")
    