#coding:utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import unittest,sys,time,re,datetime
reload(sys)
sys.setdefaultencoding('utf-8') #防乱码

#|`orientation`| (Sim/Emu-only) 在一个设定的方向模式中开始测试|`LANDSCAPE` (横向)  或 `PORTRAIT` (纵向) |
#|`autoWebview`| 直接转换到 WebView 上下文。 默认值 `false`、|`true`, `false`|
#|`fullReset`|(iOS) 删除整个模拟器目录。(Android) 通过卸载——而不是清空数据——来重置应用状态。在 Android 上，这也会在会话结束后自动清除被测应用。默认值 `false`|`true`, `false`|

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = '87deeceb'  # adb devices查到的设备名
desired_caps['app'] = '/Users/mada/Downloads/cbchot_v1.82_xiaomi_506.apk'  # 被测试应用在电脑上的位置
desired_caps['appPackage'] = 'com.cbchot.android'
desired_caps['appActivity'] = 'com.cbchot.android.LoadingActivity'
desired_caps['autoLaunch'] = 'true' #是否需要启动或安装app默认为true
desired_caps['noReset'] = 'true' #会话前是否重置app状态，默认false
desired_caps['newCommandTimeout'] = 20 #设置未接收到新命令的超时时间，默认60s

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(8)
class Video():
    '首页上所有元素'
    def video(self):
        '视频标签'
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_tab_video')
        time.sleep(1)
    def life(self):
        '生活标签'
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_tab_life')
        time.sleep(1)
    def navigation(self):
        '导航标签'
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_tab_navigation')
        time.sleep(1)
    def space(self):
        '我的标签'
        self.driver.find_element_by_id('com.cbchot.android:id/cbchot_main_tab_space')
        time.sleep(1)
    def history(self):
        '历史'
        self.driver.find_element_by_id('com.cbchot.android:id/main_title_button_history')
        time.sleep(1)
    def download(self):
        '下载'
        self.driver.find_element_by_id('com.cbchot.android:id/main_title_button_download')
        time.sleep(1)
    def searce(self):
        '搜索'
        self.driver.find_element_by_id('com.cbchot.android:id/main_title_button_search')
        time.sleep(1)
def viewSwitches():
    contexts = driver.contexts
    for cotext in contexts:
        print cotext
    driver.switch_to.context('WEBVIEW_com.cbchot.android')
    driver.get('http://and.cbchot.cn/android/home?v=1.1.82.1.1')
    time.sleep(3)
def webview():

    '首页上的webview'
    contexts = driver.contexts
    for cotext in contexts:
        print cotext
    driver.switch_to.context('WEBVIEW_com.cbchot.android')
    time.sleep(3)
    driver.current_context #查看当前的context
    driver.get('http://and.cbchot.com/android/home?v=1.1.84.1.1')
    driver.implicitly_wait(5)
    a = driver.find_element_by_xpath("/html/body/div[@class='items']/ul/li[1]")#直播
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/zhibo.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    a = driver.find_element_by_xpath("/html/body/div[@class='items']/ul/li[2]/a")#排行
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/paihang.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    a = driver.find_element_by_xpath("/html/body/div[@class='items']/ul/li[3]/a")#专题
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/zhuanti.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    a = driver.find_element_by_xpath("/html/body/div[@class='mod'][1]/div[@class='mod-title hot']/a")#专题二级页
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/zhuantierji.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    a = driver.find_element_by_xpath("/html/body/div[@class='mod'][1]/div[@class='special-ad']")#进入专题页    time.sleep(5)
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/jinruzhuanti.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    a = driver.find_element_by_xpath("/html/body/div[4]/div/a")#进入短片二级页
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/duanpianerji.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    a = driver.find_element_by_xpath("/html/body/div[4]/ul/li[1]")#短片第一个视频
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/duanpianone.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    a = driver.find_element_by_xpath("/html/body/div[4]/ul/li[6]")#短片第六个视频
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/duanpiansix.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    a = driver.find_element_by_xpath("/html/body/div[7]/div/a")#电视剧更多
    a.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/dianshijumore.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
def newVersionNo():
    '发现新版本提示框'
    driver.implicitly_wait(10)
    a = driver.find_element_by_id("com.cbchot.android:id/dialog_update_layout_btn_2") #否
    a.click()

def newVersionYes():
    driver.find_element_by_id("com.cbchot.android:id/dialog_update_layout_btn_1") #是


def xy():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x,y)
def swipLeft(t):          #屏幕向右滑动
    l=xy()
    x1=l[0]*0.75
    y1=l[1]*0.5
    x2=l[0]*0.05
    driver.swipe(x1,y1,x2,y1,t)
    #   swipLeft(1000)
    #  time.sleep(2)
    #  swipLeft(1000)
    #  time.sleep(2)
    #   swipLeft(1000)
if __name__ == '__main__':
    time.sleep(2)


    # def click_shoot_windows():
    #
    #      try:
    #
    #         els = driver.find_elements_by_class_name('android.widget.Button')
    #         print els
    #         for el in els:
    #             if el.text == u'允许':
    #                 driver.find_element_by_android_uiautomator('new UiSelector().text("允许")').click()
    #             elif el.text == u'始终允许':
    #                 driver.find_element_by_android_uiautomator('new UiSelector().text("始终允许")').click()
    #             elif el.text == u'确定':
    #                 driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
    #      except:
    #
    #          pass
    # click_shoot_windows()
    contexts = driver.contexts
    for cotext in contexts:
        print cotext
    driver.switch_to.context('WEBVIEW_com.cbchot.android')
    time.sleep(3)
    driver.current_context  # 查看当前的context
    driver.get('http://and.cbchot.cn/android/home?v=1.1.82.1.1')
    time.sleep(3)
    div = driver.find_element_by_xpath("/html/body/div[@class='items']/ul/li[1]/a")  # 直播
    div.click()
    driver.find_element_by_xpath("/html/body/div[@class='items']/ul/li[1]/a").click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/zhibo.png")
    driver.keyevent(4)
    driver.implicitly_wait(5)
    driver.switch_to.context("WEBVIEW_com.cbchot.android")
    abc = driver.find_element_by_xpath("/html/body/div[@class='items']/ul/li[2]/a")  # 排行
    abc.click()
    time.sleep(5)
    driver.switch_to.context('NATIVE_APP')
    driver.get_screenshot_as_file("/test/paihang.png")
    driver.close_app()
    driver.quit()

