from core.caseTemplate import base


def test_b1():
    """
    不继承Base类，通过创建对象执行UI自动化测试
    :return:
    """
    base.browse()
    base.get('https://www.baidu.com/')
    base.sleep(2)
    base.quite()