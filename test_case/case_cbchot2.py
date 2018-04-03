# coding:utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest, sys, time, re, datetime

reload(sys)
sys.setdefaultencoding('utf-8')  # 防乱码



class Cbchot1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start setup')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '87deeceb'  # adb devices查到的设备名
        desired_caps['app'] = '/Users/mada/Downloads/cbchot_v1.82_xiaomi_506.apk'  # 被测试应用在电脑上的位置
        desired_caps['appPackage'] = 'com.cbchot.android'
        desired_caps['appActivity'] = 'com.cbchot.android.LoadingActivity'
        desired_caps['autoLaunch'] = 'true'  # 是否需要启动或安装app默认为true
        desired_caps['noReset'] = 'true'  # 会话前是否重置app状态，默认false
        desired_caps['newCommandTimeout'] = 20  # 设置未接收到新命令的超时时间，默认60s
        desired_caps["unicodeKeyboard"] = "True"#中文
        desired_caps["resetKeyboard"] = "True"#中文
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_home(self):
        '''视频首页'''
        time.sleep(3)
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_tab_video').click()
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_tab_life')
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_tab_navigation')
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_tab_space')
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="直播 Link"]')
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="排行 Link"]')
        self.driver.find_element_by_xpath('//android.view.View[@content-desc="专题 Link"]')
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_title_iv')
        self.driver.find_element_by_id('com.cbchot.android:id/main_title_button_history')
        self.driver.find_element_by_id('com.cbchot.android:id/main_title_button_download')
        self.driver.find_element_by_id('com.cbchot.android:id/main_title_button_search')

    def test_search(self):
        '''搜索页'''
        self.driver.find_element_by_id('com.cbchot.android:id/main_title_button_search').click()
        name = self.driver.find_element_by_id('com.cbchot.android:id/sub_title_tv').text
        print name
        self.driver.find_element_by_id('com.cbchot.android:id/sub_title_button_right')
        self.driver.find_element_by_accessibility_id("大家都在看 Heading")
        self.driver.find_element_by_accessibility_id("超体12:31:38 Link")

    def test_searchcase1(self):
        '''搜索不存在内容'''
        self.driver.switch_to.context('WEBVIEW_com.cbchot.android')
        self.driver.get('http://and.cbchot.com/android/search?v=1.1.82.1.1')
        self.driver.find_element_by_xpath('//*[@id="search"]').send_keys("maxin")
        self.driver.find_element_by_xpath('/html/body/div[1]/form/button').click()
        content=self.driver.find_element_by_xpath('/html/body/div[1]/div').text
        print content
        time.sleep(5)
    def test_searchcase2(self):
        '''搜索'''
        self.driver.find_element_by_xpath('//*[@id="btn-clear"]').click()
        self.driver.find_element_by_xpath('//*[@id="search"]').send_keys(u"超体")
        self.driver.find_element_by_xpath('/html/body/div[1]/form/button').click()
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.find_element_by_accessibility_id("超体12:31:38 Link")

        time.sleep(5)












if __name__ == "__main__":
    unittest.main()
