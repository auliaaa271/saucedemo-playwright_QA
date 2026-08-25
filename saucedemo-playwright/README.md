# SauceDemo Playwright Automation Testing

## Project Overview

This project is a UI automation testing project for the SauceDemo web application using Playwright with Python.

The project focuses on testing the login, shopping cart, checkout, and logout functionalities.

Both positive and negative test scenarios are included.

## Tools & Technologies

- Python
- Playwright
- Pytest
- Visual Studio Code

## Test Scenarios

### Login Testing

- Valid Login
- Invalid Login

### Shopping Cart Testing

- Add Product to Cart
- Multiple Products in Cart
- Remove Product from Cart

### Checkout Testing

- Checkout Without Information
- Successful Checkout

### Logout Testing

- Successful Logout

## Test Coverage

| Module   | Test Scenario                | Type     |
| -------- | ---------------------------- | -------- |
| Login    | Valid Login                  | Positive |
| Login    | Invalid Login                | Negative |
| Cart     | Add Product to Cart          | Positive |
| Cart     | Multiple Products in Cart    | Positive |
| Cart     | Remove Product from Cart     | Positive |
| Checkout | Checkout Without Information | Negative |
| Checkout | Successful Checkout          | Positive |
| Logout   | Successful Logout            | Positive |

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Project Structure

```text
saucedemo-playwright/
│
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_checkout_validation.py
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_multiple_products.py
│   └── test_remove_product.py
│
├── README.md
└── requirements.txt
```
