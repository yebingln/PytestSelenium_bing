# from .drivers import Drivers
from .webdriver_api import WebDriver
import pytest
import allure



# class BaseCase(WebDriver):
#     def __init__(self, driver='chrome', timeout=10):
#         self.driver = Drivers(driver)
#         self.timeout = timeout

@allure.feature('UI Testsuite')
@allure.story('base by Base(webdriver)\'s cases')
class Base(WebDriver):

    @pytest.fixture(scope="module", autouse=True)
    def browser_setup_and_teardown(self, pytestconfig):
        """
        Custom UI autotest's setup and teardown
        :param pytestconfig: read conftest.py
        :return:

        """
        browse = pytestconfig.getoption('browse')  # get terminal args--browse
        timeout = float(pytestconfig.getoption('eleto'))  # get terminal args timeout--eleto
        self.browser = WebDriver.browse(browse, timeout) if browse or timeout else WebDriver.browse()
        yield
        self.browser.close()
        self.browser.quit()

    def report_add_attach_png(self, filename='error'):
        """
        add allure report screenshot，such:find element fail,add screenshot to allure-report
        :param filename: filename，default=error
        :return:
        """
        base64 = self.get_screenshot_allure()
        allure.attach(filename, base64, allure.attach_type.PNG)



base=Base()


