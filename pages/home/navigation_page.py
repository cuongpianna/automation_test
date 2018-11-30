import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "All Courses"
    _all_courses = "My Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"

    def navigate_to_all_courses(self):
        self.element_click(locator=self._all_courses, locator_type='link')

    def navigate_to_my_courses(self):
        self.element_click(locator=self._my_courses, locator_type="link")

    def navigate_to_practice(self):
        self.element_click(locator=self._practice, locator_type="link")

    def navigate_to_user_settings(self):
        user_settings_element = self.wait_for_element(locator=self._user_settings_icon,
                                                      locator_type="xpath", poll_frequency=1)
        # self.elementClick(element=user_settings_element)
        self.element_click(locator=self._user_settings_icon,
                           locator_type="xpath")
