运行入口：run.py
"""
主函数执行入口，命令行执行：
1.python3 run.py demo
  python3 run.py demo/test_baidu.py
  执行demo文件夹下的所有测试用例，不指定时默认为根目录下./

2.pytest的运行参数在pytest.ini里配置

3.在相应的目录里生成report,打开report/html中index.html,为实际报告展示
"""

1、做UI自动化时有两种方式，一种集成Base类，一种创建Base的对象base

一种集成Base：
class Testbaidu(Base):

    def test_k(self):
        try:
            self.get('https://www.baidu.com/')
            self.click('css=>#ssu')
        except Exception as e:
            print('测试失败 %s'% e)
            self.report_add_attach_png(self.__class__.__name__)
            raise e


二种对象base：
def test_b1():
    """
    不继承Base类，通过创建对象执行UI自动化测试
    :return:
    """
    base.browse()
    base.get('https://www.baidu.com/')
    base.sleep(2)
    base.quite()