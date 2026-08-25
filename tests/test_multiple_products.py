from playwright.sync_api import sync_playwright


def test_multiple_products_in_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open SauceDemo
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Add first product
        page.click("#add-to-cart-sauce-labs-backpack")

        # Add second product
        page.click("#add-to-cart-sauce-labs-bike-light")

        # Open cart
        page.click(".shopping_cart_link")

        # Get products in cart
        products = page.locator(".cart_item")

        # Verify there are 2 products
        assert products.count() == 2

        # Verify first product
        assert page.locator(".inventory_item_name").nth(0).inner_text() == "Sauce Labs Backpack"

        # Verify second product
        assert page.locator(".inventory_item_name").nth(1).inner_text() == "Sauce Labs Bike Light"

        browser.close()