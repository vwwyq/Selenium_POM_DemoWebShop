import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from object_repository.simpcomp_page_locators import SimpCompPageLocators


loc = SimpCompPageLocators()

class SimpleComputerPage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver ---> driver --> webdriver.Chrome()
        self.ac = ActionChains(driver)

    def select_processor(self):
        # self.driver.find_element('xpath', '//input[@id="product_attribute_75_5_31_96"]').click()
        self.driver.find_element(*loc.processor).click()
        time.sleep(1)

    def click_on_addtocart(self):
        # self.driver.find_element('xpath', '//input[@id="add-to-cart-button-75"]').click()
        self.driver.find_element(*loc.addtocart_btn).click()
        time.sleep(1)

    def scroll_to_home(self):
        self.ac.send_keys(Keys.HOME).perform()
        time.sleep(1)

    def click_on_shoppingcart(self):
        # self.driver.find_element('xpath', '//span[text()="Shopping cart"]').click()
        self.driver.find_element(*loc.shopping_cart).click()
        time.sleep(1)
