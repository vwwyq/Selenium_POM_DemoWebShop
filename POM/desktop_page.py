import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from object_repository.desktoppage_locators import DesktopLocators

loc = DesktopLocators()

class DesktopPage:

    def __init__(self, driver):
        self.driver = driver            ## self.driver --> driver --> webdriver.Chrome()
        self.ac = ActionChains(driver)

    def select_sortby(self, text):
        # sort = self.driver.find_element('xpath', '//select[@id="products-orderby"]')
        sort = self.driver.find_element(*loc.sort_drpdwn)
        sort_select = Select(sort)
        sort_select.select_by_visible_text(text)
        time.sleep(1)

    def select_viewas(self, text):
        # view = self.driver.find_element('xpath', '//select[@id="products-viewmode"]')
        view = self.driver.find_element(*loc.viewas_drpdwn)
        view_select = Select(view)
        view_select.select_by_visible_text(text)
        time.sleep(1)

    def scroll_pagedown(self):
        self.ac.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

    def click_on_simp_com(self):
        # self.driver.find_element('xpath', '(//a[text()="Simple Computer"])[2]').click()
        self.driver.find_element(*loc.simp_comp).click()
        time.sleep(1)

















