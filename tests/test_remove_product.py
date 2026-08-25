from playwright.sync_api import sync_playwright


def test_remove_product_from_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open SauceDemo
        page.goto("https://www.saucedemo.com/")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Add two products
        page.click("#add-to-cart-sauce-labs-backpack")
        page.click("#add-to-cart-sauce-labs-bike-light")

        # Open cart
        page.click(".shopping_cart_link")

        # Verify there are 2 products
        products = page.locator(".cart_item")
        assert products.count() == 2

        # Remove Backpack
        page.click("#remove-sauce-labs-backpack")

        # Verify only 1 product remains
        assert products.count() == 1

        # Verify the remaining product
        remaining_product = page.locator(".inventory_item_name")
        assert remaining_product.inner_text() == "Sauce Labs Bike Light"

        browser.close()
