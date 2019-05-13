from core.caseTemplate import Base
import os
import pytest
import allure

"""
class Test_Baidu(object):
    def test_a(self,pytestconfig):
        # print(pytestconfig.getoption('browse'))
        assert 1
    def test_b(self):
        print('-----',__name__,'------')
"""


@pytest.mark.timeout(20)
class Testbaidu(Base):

    def test_k(self):
        try:
            self.get('https://www.baidu.com/')
            self.click('css=>#su')
        except Exception as e:
            print('测试失败 %s'% e)
            self.report_add_attach_png(self.__class__.__name__)
            raise e

    data = [
        "./toolong.jpg"]

    @pytest.mark.parametrize('aa', data, indirect=True)
    def ttest_k3(self, aa):
        assert 1

@pytest.mark.red
@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 1


@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('critical')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('normal')
def ttest_case_03():
    """
    用例描述：Test case 03
    """
    assert 1


@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('minor')
def ttest_case_04():
    """
    用例描述：Test case 04
    """
    assert 0 == 0

