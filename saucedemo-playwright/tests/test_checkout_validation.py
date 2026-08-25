from playwright.sync_api import sync_playwright


def test_checkout_without_information():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open SauceDemo
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Add product to cart
        page.click("#add-to-cart-sauce-labs-backpack")

        # Open cart
        page.click(".shopping_cart_link")

        # Checkout
        page.click("#checkout")

        # Click Continue without filling information
        page.click("#continue")

        # Verify error message
        error_message = page.locator('[data-test="error"]')

        assert error_message.is_visible()
        assert error_message.inner_text() == "Error: First Name is required"

        browser.close()