import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger


class LoginPage(BasePage):

    logger = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator
    _login_link = 'Login'
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = 'commit'

    # def get_login_link(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def get_email_field(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def get_login_button(self):
    #     return self.driver.find_element(By.NAME, self._login_link)

    def click_login_link(self):
        self.element_click(self._login_link, locator_type='link')

    def enter_email(self, email):
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type='name')

    def login(self, email='', password=''):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        result = self.is_element_present('//*[@id="navbar"]/div/div/div/ul/li[4]/a/span',
                                         locator_type='xpath')
        return result

    def verify_login_fail(self):
        return self.is_element_present('/html/body/div/div/div/div/div/div/div[1]/div/div',
                                       locator_type='xpath')

    def verify_login_title(self):
        return self.verify_page_title('Google')

