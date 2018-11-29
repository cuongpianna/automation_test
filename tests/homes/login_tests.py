import unittest
import pytest

from pages.home.login_pages import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login_page = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_page.login('test@gmail.com', 'abcabc')

        result1 = self.login_page.verify_login_title()
        self.ts.mark(result1, 'Title is incorrect')

        result2 = self.login_page.verify_login_successful()
        self.ts.mark_final('test_validLogin', result2, 'Login was not successful')

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.login_page.login()
        result = self.login_page.verify_login_fail()
        assert result == True
