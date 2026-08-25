from playwright.sync_api import sync_playwright


def test_add_to_cart():
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

        # Verify product is in the cart
        product = page.locator(".inventory_item_name")
        assert product.inner_text() == "Sauce Labs Backpack"

        browser.close()