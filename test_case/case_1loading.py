# coding:utf-8
from appium import webdriver
import unittest, time, re, datetime
import Base
import ddt
from ddt import ddt,data,file_data,unpack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class landing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('登陆页测试开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=Base.setting())
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        print('登陆页面测试结束')
    def test_landing(self):
        '''引导页'''
        time.sleep(3)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/splash1alpha')
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.75, y * 0.5, x * 0.05, y * 0.5, 1000)
        self.driver.swipe(x * 0.75, y * 0.5, x * 0.05, y * 0.5, 1000)
        self.driver.find_element_by_id("com.ccbscf.mobile.corp:id/btn_login").click()
    def test_landing1(self):
        '''进入首页权限提示'''
        # 判断是否有权限弹窗
        for i in range(5):
            loc = ("xpath", "//*[@text='始终允许']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass
        for i in range(5):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(self.driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass
    def test_landing2(self):
        '''登陆页元素检查'''
        time.sleep(1)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_icpeople')
        #企业名称元素及提示文字
        self.assertEqual('企业全称',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_companyname').text)
        #手机号码元素及提示文字
        self.assertEqual('手机号码',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_phonenumber').text)
        #登陆密码元素及提升文字
        self.assertEqual('登录密码',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_password').text)
        #logo提示文字
        self.assertEqual('Copyright © 2018 \nccbscf.com',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_loginlogo').text)
        #记住账号默认为选中状态
        self.assertTrue(self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/checkBox_remember').get_attribute('checked'))
        #忘记密码按钮
        self.assertEqual('忘记密码？',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_forgetpassword').text)

if __name__ == "__main__":
    unittest.main()
