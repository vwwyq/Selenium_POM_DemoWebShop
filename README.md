# Selenium Page Object Model Automation – Demo Web Shop

## Overview
This project is a **Selenium automation framework built using Python and the Page Object Model (POM) design pattern**.  
It automates a complete user workflow on the demo e-commerce website:

https://demowebshop.tricentis.com

The automated scenario includes:

- User login
- Product navigation
- Adding products to the cart
- Cart verification
- Checkout workflow

The framework is designed with the following principles:

- **Readability** – clear and structured code
- **Maintainability** – separation of locators, logic, and tests
- **Reusability** – reusable page object classes
- **Scalability** – easy to extend with additional pages and test cases

The project uses **PyTest** for test execution and **Excel-based test data** for externalized inputs.

---

# Project Structure
```
.
│   demowebshop.py
│
├── files_
│   └── demo_testdata.xlsx
│
├── generic_utilities
│   ├── excel_utility.py
│   └── __init__.py
│
├── object_repository
│   ├── cartpage_locators.py
│   ├── desktoppage_locators.py
│   ├── homepage_locators.py
│   ├── loginpage_locators.py
│   ├── simpcomp_page_locators.py
│   └── __init__.py
│
├── POM
│   ├── cartpage.py
│   ├── desktop_page.py
│   ├── homepage.py
│   ├── loginpage.py
│   ├── simp_comp_page.py
│   └── __init__.py
│
└── scripts
    ├── conftest.py
    ├── test_demowebshop.py
    └── __init__.py
```
---

# Folder Description

## files_
Contains external test data used by the automation framework.

- **demo_testdata.xlsx**  
  Stores test inputs such as login credentials and other data required during execution.

---

## generic_utilities
Contains reusable helper modules.

- **excel_utility.py**  
  Utility functions for reading data from Excel files.

---

## object_repository
Stores **all web element locators** used across the application.

Each file corresponds to a specific page and contains only locator definitions.

Examples:

- `homepage_locators.py`
- `loginpage_locators.py`
- `desktoppage_locators.py`
- `simpcomp_page_locators.py`
- `cartpage_locators.py`

Separating locators ensures that UI changes can be handled easily without modifying test scripts.

---

## POM (Page Object Model)

Contains page classes implementing **actions and behaviors of each web page**.

Each page file:

- Imports locators from `object_repository`
- Implements methods representing user interactions

Examples:

- **homepage.py** – navigation from the homepage
- **loginpage.py** – login related actions
- **desktop_page.py** – navigation within desktop category
- **simp_comp_page.py** – simple computer product page actions
- **cartpage.py** – cart and checkout interactions

This layer abstracts UI interactions from test logic.

---

## scripts

Contains test execution logic.

### conftest.py
Defines **pytest fixtures** such as:

- WebDriver initialization
- Browser setup
- Test environment configuration

### test_demowebshop.py
Contains the automated test case performing the full workflow:

1. Login to the website
2. Navigate to products
3. Add product to cart
4. Proceed to checkout
5. Validate checkout page

---

# Technologies Used

- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Excel for test data management

---

# Test Execution

Run the test suite using:

```bash
pytest test_demowebshop.py -vs
