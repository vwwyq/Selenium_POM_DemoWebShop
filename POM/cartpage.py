import time

from selenium.webdriver.support.select import Select
from object_repository.cartpage_locators import CartPageLocators

loc = CartPageLocators()

class CartPage:

    def __init__(self, driver):
        self.driver = driver            ## self.driver --> driver --> webdriver.Chrome()

    def select_country(self, country):
        # country_id = self.driver.find_element('xpath', '//select[@id="CountryId"]')
        country_id = self.driver.find_element(*loc.country_data)
        country_select = Select(country_id)
        country_select.select_by_visible_text(country)
        time.sleep(1)

    def clear_pincode_textbox(self):
        # self.driver.find_element('xpath', '//input[@id="ZipPostalCode"]').clear()
        self.driver.find_element(*loc.postalcode).clear()
        time.sleep(1)

    def enter_pincode(self, pincode):
        # self.driver.find_element('xpath', '//input[@id="ZipPostalCode"]').send_keys(int(pincode))
        self.driver.find_element(*loc.postalcode).send_keys(int(pincode))
        time.sleep(1)

    def click_on_terms_service(self):
        # self.driver.find_element('xpath', '//input[@id="termsofservice"]').click()
        self.driver.find_element(*loc.terms_service).click()
        time.sleep(1)

    def click_on_checkout(self):
        # self.driver.find_element('xpath', '//button[@id="checkout"]').click()
        self.driver.find_element(*loc.checkout_btn).click()