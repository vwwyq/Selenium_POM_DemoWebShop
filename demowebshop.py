import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait = WebDriverWait(driver, 10)
ac = ActionChains(driver)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath', '//a[text()="Log in"]').click()
time.sleep(1)
driver.find_element('id', 'Email').send_keys('steve.jobs123@gmail.com')
driver.find_element('id', 'Password').send_keys('stevejobs')
driver.find_element('xpath', '//input[@value="Log in"]').click()
time.sleep(4)

wait.until(EC.visibility_of_element_located(('xpath', '//a[text()="Log out"]')))
time.sleep(2)

comp = driver.find_element('xpath', '(//a[contains(text(), "Computers")])[1]')
ac.move_to_element(comp).perform()
time.sleep(1)

driver.find_element('xpath', '(//a[contains(text(), "Desktops")])[1]').click()
time.sleep(1)

sort = driver.find_element('xpath', '//select[@id="products-orderby"]')
sort_select = Select(sort)
sort_select.select_by_visible_text("Price: Low to High")
time.sleep(1)

view = driver.find_element('xpath', '//select[@id="products-viewmode"]')
view_select = Select(view)
view_select.select_by_visible_text("List")
time.sleep(1)

ac.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)

driver.find_element('xpath', '(//a[text()="Simple Computer"])[2]').click()
time.sleep(1)

driver.find_element('xpath', '//input[@id="product_attribute_75_5_31_96"]').click()
time.sleep(1)

driver.find_element('xpath', '//input[@id="add-to-cart-button-75"]').click()
time.sleep(1)

ac.send_keys(Keys.HOME).perform()
time.sleep(1)

driver.find_element('xpath', '//span[text()="Shopping cart"]').click()
time.sleep(1)

country = driver.find_element('xpath', '//select[@id="CountryId"]')
country_select = Select(country)
country_select.select_by_visible_text("India")
time.sleep(1)

driver.find_element('xpath', '//input[@id="ZipPostalCode"]').clear()
time.sleep(1)
driver.find_element('xpath', '//input[@id="ZipPostalCode"]').send_keys('5632014')
time.sleep(1)

driver.find_element('xpath', '//input[@id="termsofservice"]').click()
time.sleep(1)

driver.find_element('xpath', '//button[@id="checkout"]').click()















































