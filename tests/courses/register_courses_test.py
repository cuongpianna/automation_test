import unittest
import pytest

from pages.courses.register_courses_pages import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    # def setUp(self):
    #     self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)
    def test_invalid_enrolment(self):
        self.courses.click_all_courses_link()
        self.courses.enter_course_name('javascript')
        self.courses.select_course_to_enroll('Javascript for beginners')
        self.courses.enroll_course(num='10', exp='1220', cvv='10')
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final('test_invalid_enrollment', result,
                           'Enrollment Failed Verification')