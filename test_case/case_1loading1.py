# coding:utf-8
from appium import webdriver
import unittest, time, re, datetime
import Base
import ddt
from ddt import ddt,data,file_data,unpack
@ddt
class landing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('登陆页测试开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=Base.setting())
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        print('登陆页面测试结束')
        cls.driver.quit()
    @data(['sss','ddd','dddd','输入内容'],
              ['测试企业','','电话密码为空'],
              ['','18600911974','','用户名密码为空'],
              ['测试企业一零','123','a1111111','错误的电话号码'],
              ['ssss','22222','a1111111','错误的企业名']
              )
    @unpack
    def test_ladings(self,name,phone,passwd,ex):
        '''不符合规则的登陆'''
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_companyname').click()
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_companyname').clear()
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_companyname').send_keys(name)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_phonenumber').click()
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_phonenumber').clear()
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_phonenumber').send_keys(phone)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_password').click()
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_password').clear()
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_password').send_keys(passwd)
        self.assertTrue(self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/button_login').is_enabled())
        print (ex)
if __name__ == "__main__":
    unittest.main()
