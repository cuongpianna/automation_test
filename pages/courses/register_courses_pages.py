import logging
from base.basepage import BasePage
from utilities.custom_logger import custom_logger


class RegisterCoursesPage(BasePage):

    log = custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ###############
    ## Locators ###
    ###############

    _search_box = "search-courses"
    _all_courses_link = '//*[@id="navbar"]/div/div/div/ul/li[2]/a'
    _course = "/html/body/div/div/div/div[2]/div[4]"
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = '//*[@id="root"]/form/span[2]/label/input[@name="cardnumber"]'
    _cc_exp = "cc-exp"
    _cc_cvv = "//*[@id='root']/form/span[2]/label/input"
    _submit_enroll = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text()," \
                            "'The card number is not a valid credit card number.')]"

    ############################
    ### Element Interactions ###
    ############################

    def click_all_courses_link(self):
        self.element_click(self._all_courses_link, locator_type='xpath')

    def enter_course_name(self, name):
        self.send_keys(name, locator=self._search_box)

    def select_course_to_enroll(self, full_course_name):
        self.element_click(locator=self._course.format(full_course_name), locator_type="xpath")

    def click_on_enroll_button(self):
        self.element_click(locator=self._enroll_button)

    def enter_card_num(self, num):
        self.send_keys(num, locator=self._cc_num, locator_type='xpath')

    def enter_card_exp(self, exp):
        self.send_keys(exp, locator=self._cc_exp)

    def enter_card_cvv(self, cvv):
        self.send_keys(cvv, locator=self._cc_cvv, locator_type='xpath')

    def click_enroll_submit_button(self):
        self.send_keys(self._submit_enroll, locator="xpath")

    def enter_credit_card_information(self, num, exp, cvv):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)

    def enroll_course(self, num="", exp="", cvv=""):
        self.click_on_enroll_button()
        self.web_scroll(direction="down")
        self.enter_credit_card_information(num, exp, cvv)
        self.click_enroll_submit_button()

    def verify_enroll_failed(self):
        message_element = self.wait_for_element(self._enroll_error_message, locator_type="xpath")
        result = self.is_element_displayed(element=message_element)
        return result
