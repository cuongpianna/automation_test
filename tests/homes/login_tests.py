import unittest
import pytest
from ddt import ddt, data, unpack

from pages.home.login_pages import LoginPage
from utilities.teststatus import TestStatus
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login_page = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    @data(*get_csv_data('C:\\Users\\admin\\Desktop\\lam\\autotest\\letskodeit\\testdata.csv'))
    @unpack
    def test_valid_login(self, email, password):
        self.login_page.login(email, password)

        result1 = self.login_page.verify_login_title()
        self.ts.mark(result1, 'Title is incorrect')

        result2 = self.login_page.verify_login_successful()
        self.ts.mark_final('test_validLogin', result2, 'Login was not successful')

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.login_page.login()
        result = self.login_page.verify_login_fail()
        assert result == True
