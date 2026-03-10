import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from object_repository.homepage_locators import HomePageLocators

loc = HomePageLocators()

class HomePage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver --> webdriver.Chrome()
        self.wait = WebDriverWait(driver, 10)
        self.ac = ActionChains(driver)

    def click_on_login_link(self):
        # self.driver.find_element('xpath', '//a[text()="Log in"]').click()
        self.driver.find_element(*loc.login_link).click()
        time.sleep(1)

    def verify_logout_btn(self):
        # self.wait.until(EC.visibility_of_element_located(('xpath', '//a[text()="Log out"]')))
        self.wait.until(EC.visibility_of_element_located(loc.logout_link))
        time.sleep(2)

    def hover_to_computers(self):
        # comp = self.driver.find_element('xpath', '(//a[contains(text(), "Computers")])[1]')
        comp = self.driver.find_element(*loc.computers)
        self.ac.move_to_element(comp).perform()
        time.sleep(1)

    def click_on_desktops(self):
        # self.driver.find_element('xpath', '(//a[contains(text(), "Desktops")])[1]').click()
        self.driver.find_element(*loc.desktops).click()
        time.sleep(1)



















































































