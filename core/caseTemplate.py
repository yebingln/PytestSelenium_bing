# from .drivers import Drivers
from .webdriver_api import WebDriver
import pytest
import allure
from .allure_attach import report_attach


# class BaseCase(WebDriver):
#     def __init__(self, driver='chrome', timeout=10):
#         self.driver = Drivers(driver)
#         self.timeout = timeout

@allure.feature('UI自动化测试集')
@allure.story('基于Base(webdriver)类的cases')
class Base(WebDriver):

    @pytest.fixture(scope="module", autouse=True)
    def browser_setup_and_teardown(self, pytestconfig):
        """
        自定义 UI自动化的 setup and teardown
        :param pytestconfig: read conftest.py
        :return:

        """
        browse = pytestconfig.getoption('browse')  # 获取命令行浏览器参数--browse
        timeout = float(pytestconfig.getoption('eleto'))  # 获取命令行元素超时参数--eleto
        self.browser = WebDriver.browse(browse, timeout) if browse or timeout else WebDriver.browse()
        yield
        self.browser.close()
        self.browser.quit()

    def report_add_attach_png(self, filename='error'):
        """
        add allure report 截图，如：查找元素失败，截图并添加到report
        :param filename: 文件名，默认为error
        :return:
        """
        base64 = self.get_screenshot_allure()
        allure.attach(filename, base64, allure.attach_type.PNG)



base=Base()

"""
    @pytest.fixture()
    def aa(self, request):
        print(request.function)

        # file = open(request.param,'rb')
        #
        # filename = file.name
        #
        # allure.attach(filename.rsplit("/")[-1],file.read(),getattr(allure.attach_type,filename.rsplit('.')[1].upper(),"OTHER"))
        return True
        
        # 使用
        data = [
            "./toolong.jpg"]

        @pytest.mark.parametrize('aa', data, indirect=True)
        def ttest_k3(self, aa):
            assert 1

"""
