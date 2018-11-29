import pytest
from pages.home.login_pages import LoginPage
from base.webdriverfactory import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login('test@gmail.com', 'abcabc')

    # if browser == 'firefox':
    #     base_url = 'https://learn.letskodeit.com/'
    #     driver = webdriver.Firefox('C:\\chromedriver_win32\\chromedriver.exe')
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(base_url)
    # else:
    #     print("Running tests on chrome")
    #     base_url = 'https://learn.letskodeit.com/'
    #     driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(base_url)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")