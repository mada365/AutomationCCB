#coding:utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest,sys,time,re,datetime
reload(sys)
sys.setdefaultencoding('utf-8') #防乱码
from selenium.webdriver.support.ui import WebDriverWait

#|`orientation`| (Sim/Emu-only) 在一个设定的方向模式中开始测试|`LANDSCAPE` (横向)  或 `PORTRAIT` (纵向) |
#|`autoWebview`| 直接转换到 WebView 上下文。 默认值 `false`、|`true`, `false`|
#|`fullReset`|(iOS) 删除整个模拟器目录。(Android) 通过卸载——而不是清空数据——来重置应用状态。在 Android 上，这也会在会话结束后自动清除被测应用。默认值 `false`|`true`, `false`|

# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '4.4.4'
# desired_caps['deviceName'] = '87deeceb'  # adb devices查到的设备名
# desired_caps['app'] = '/Users/mada/Downloads/cbchot_v1.82_xiaomi_506.apk'  # 被测试应用在电脑上的位置
# desired_caps['appPackage'] = 'com.cbchot.android'
# desired_caps['appActivity'] = 'com.cbchot.android.LoadingActivity'
# desired_caps['autoLaunch'] = 'true' #是否需要启动或安装app默认为true
# desired_caps['noReset'] = 'true' #会话前是否重置app状态，默认false
# desired_caps['newCommandTimeout'] = 20 #设置未接收到新命令的超时时间，默认60s
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# time.sleep(8)
class Cbchot1(unittest.TestCase):

    # def setUp(self):
    #     self.driver = webdriver.Remote(
    #         command_executor='http://localhost:4723/wd/hub',
    #         desired_capabilities={
    #             'platformName':'Android',
    #             'platformVersion' : '4.4.4',
    #             'deviceName' : '87deeceb',
    #             'app':'/Users/mada/Downloads/cbchot_v1.82_xiaomi_506.apk',
    #             'appPackage':'com.cbchot.android',
    #             'appActivity':'com.cbchot.android.LoadingActivity',
    #             'newCommandTimeout':'newCommandTimeout'
    #         })
    #     self.driver.implicitly_wait(30)
    #     self.verifficationErrors=[]
    #     self.accept_next_alert = True
    @classmethod
    def setUpClass(cls):
        print('start setup')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'd5ce9db'  # adb devices查到的设备名
        desired_caps['app'] = '/Users/mada/Downloads/cbchot_v1.82_xiaomi_506.apk'  # 被测试应用在电脑上的位置
        desired_caps['appPackage'] = 'com.cbchot.android'
        desired_caps['appActivity'] = 'com.cbchot.android.LoadingActivity'
        desired_caps['autoLaunch'] = 'true' #是否需要启动或安装app默认为true
        desired_caps['noReset'] = 'false' #会话前是否重置app状态，true为不需要,默认false
        desired_caps['newCommandTimeout'] = 20 #设置未接收到新命令的超时时间，默认60s
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print ('tearDown')


    def test_1open(self):
        '''允许访问数据小米'''
        WebDriverWait(self.driver,15,0.5,ignored_exceptions= '异常').until(lambda driver:self.driver.find_element_by_id('com.lbe.security.miui:id/accept'))

    #    self.driver.find_element_by_id('com.lbe.security.miui:id/accept').click()

    def test_2star(self):
        """起始页面"""
        time.sleep(2)
        self.driver.find_element_by_id('com.cbchot.android:id/indicator')
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.75,y*0.5,x*0.05,y*0.5,1000)
        self.driver.swipe(x * 0.75, y * 0.5, x * 0.05, y * 0.5, 1000)
        self.driver.swipe(x * 0.75, y * 0.5, x * 0.05, y * 0.5, 1000)

    def test_3newversion(self):
        '''新版本提示框点击否'''
       # WebDriverWait(self.driver, 100, 10)
        time.sleep(5)
      #  WebDriverWait(self.driver,10,0.5).until(lambda driver:self.driver.find_element_by_id('com.cbchot.android:id/dialog_update_layout_btn_2').click())
        self.driver.find_element_by_id('com.cbchot.android:id/dialog_update_layout_btn_2').click()



if __name__=="__main__":
    unittest.main()











# #搜索测试yongli
#     def test_baidu_search(self):
#         u"""百度搜索"""
#         driver = self.driver
#         driver.get(self.base_url+'/')
#         driver.find_element_by_id("kw").send_keys("selenium webdriver")
#         driver.find_element_by_id("su").click()
#         time.sleep(2)
#         driver.close()
# #百度设置用例
#     def test_baidu_set(self):
#         u"""百度设置"""
#         driver = self.driver
#
#         driver.get(self.base_url+"/gaoji/preferences.html")
#
#         m = driver.find_element_by_xpath('//*[@id="sh_2"]').click()
#         time.sleep(2)
#
#         driver.find_element_by_xpath('//*[@id="save"]').click()
#         time.sleep(2)
#         driver.switch_to_alert().accept()
    #
    # def tearDown(self):
    #
    #     self.driver.quit()
    #     self.assertEqual([], self.verifficationErrors)

