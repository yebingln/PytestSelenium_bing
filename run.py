# coding='utf-8'

import pytest, os, sys

"""
主函数执行入口，命令行执行：
1.python3 run.py demo
  python3 run.py demo/test_baidu.py 
  执行demo文件夹下的所有测试用例，不指定时默认为根目录下./
  
2.pytest的运行参数在pytest.ini里配置

3.在相应的目录里生成report,打开report/html中index.html,为实际报告展示
"""

if __name__ == '__main__':
    testdir = (sys.argv[1:] if len(sys.argv) >= 1 else '/')  # 指定测试文件夹
    reportpath = (testdir and not testdir[0].find('.py')) and (testdir[0] + '/report') or (
            testdir and testdir[0].find('.py')) and (testdir[0].rsplit('/', 1)[0] + '/report') or './report'
    testdir.extend(['--alluredir', reportpath])
    pytest.main(testdir)
    os.system('allure generate ' + reportpath + ' -o ' + reportpath + '/html')
