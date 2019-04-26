def pytest_addoption(parser):

    # 浏览器类型
    parser.addoption('--browse', action='store', default='chrome',
                     help='browse type such as chrome')
    # 查找元素超时时间
    parser.addoption('--eleto', action='store', default=10,
                     help='timeout of find element')
    parser.addoption("--ALL", action="store_true",
                     help="run all combinations")



# from core.caseTemplate import BaseCase
import pytest


# @pytest.fixture(scope='module', autouse=True)
# def creat_driver(pytestconfig):
#     browse = pytestconfig.getoption('browse')
#     driver = BaseCase(browse) if browse else BaseCase()
#     print('驱动加载成功')
#     return driver
