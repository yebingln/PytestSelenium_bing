# encoding='utf-8'
import pytest, os, sys



if __name__ == '__main__':
    testdir = (sys.argv[1:] if len(sys.argv) >= 1 else '/')  # give the folder
    reportpath = (testdir and not testdir[0].find('.py')) and (testdir[0] + '/report') or (
            testdir and testdir[0].find('.py')) and (testdir[0].rsplit('/', 1)[0] + '/report') or './report'
    testdir.extend(['--alluredir', reportpath])
    pytest.main(testdir)
    os.system('allure generate ' + reportpath + ' -o ' + reportpath + '/html')
