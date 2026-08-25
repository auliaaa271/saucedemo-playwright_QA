from playwright.sync_api import sync_playwright


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open SauceDemo
        page.goto("https://www.saucedemo.com/")

        # Enter username and password
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        # Click Login
        page.click("#login-button")

        # Verify successful login
        assert page.url == "https://www.saucedemo.com/inventory.html"

        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.fill("#user-name", "standard_user")
        page.fill("#password", "wrong_password")
        page.click("#login-button")

        error_message = page.locator('[data-test="error"]')

        # Verify error message
        assert error_message.is_visible()
        assert error_message.inner_text() == "Epic sadface: Username and password do not match any user in this service"

        # Show error message in terminal
        print("Error message:", error_message.inner_text())

       