
from appium import webdriver

def drivers():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = '192.168.1.54:5555'
    desired_caps['appPackage'] = 'com. xx'
    #desired_caps['app'] = 'F:// debug.apk'
    desired_caps['appActivity'] = 'com.xx.MainActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait()
    return driver


def testcase_home():
    driver=drivers()
    try:
        driver.find_element_by_id("aa").click()
        driver.find_element_by_id("aa").send_keys("33")


        driver.quit()
        driver.close()

    except Exception as e:
        print(e)



if __name__=='__main__':
    print(1 and 0 or 3)