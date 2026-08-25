from playwright.sync_api import sync_playwright


def test_checkout():
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

        # Fill checkout information
        page.fill("#first-name", "Imroatul")
        page.fill("#last-name", "Aulia")
        page.fill("#postal-code", "12345")

        # Continue to overview
        page.click("#continue")

        # Finish order
        page.click("#finish")

        # Verify successful order
        confirmation = page.locator(".complete-header")
        assert confirmation.inner_text() == "Thank you for your order!"

        browser.close()