from playwright.sync_api import sync_playwright


def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open SauceDemo
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Open menu
        page.click("#react-burger-menu-btn")

        # Click Logout
        page.click("#logout_sidebar_link")

        # Verify back to login page
        assert page.locator("#login-button").is_visible()

        browser.close()