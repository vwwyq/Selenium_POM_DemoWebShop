import time

from object_repository.loginpage_locators import LoginPageLocators

loc = LoginPageLocators()

class LoginPage:

    def __init__(self, driver):
        self.driver = driver        ## self.driver --> driver --> webdriver.Chrome()

    def enter_email(self, email_id):
        # self.driver.find_element('id', 'Email').send_keys(email_id)
        self.driver.find_element(*loc.email).send_keys(email_id)

    def enter_pwd(self, pwd):
        # self.driver.find_element('id', 'Password').send_keys(pwd)
        self.driver.find_element(*loc.password).send_keys(pwd)

    def click_on_login_btn(self):
        # self.driver.find_element('xpath', '//input[@value="Log in"]').click()
        self.driver.find_element(*loc.login_btn).click()
        time.sleep(4)