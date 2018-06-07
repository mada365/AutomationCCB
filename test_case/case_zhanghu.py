#!/usr/bin/env
# coding:utf-8
from typing import List
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import unittest, time, re, datetime
from selenium import webdriver
import Base
from selenium.webdriver.support.wait import WebDriverWait
from Base import *

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

class information(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n产品信息测试开始\n')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=setting())
        cls.driver.find_element_by_id(id + '/edit_companyname').click()
        cls.driver.find_element_by_id(id + '/edit_companyname').send_keys(u'测试企业一零')
        cls.driver.find_element_by_id(id + '/edit_phonenumber').click()
        cls.driver.find_element_by_id(id + '/edit_phonenumber').send_keys('18910248213')
        cls.driver.find_element_by_id(id + '/edit_password').click()
        cls.driver.find_element_by_id(id + '/edit_password').send_keys('a1111111')
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/button_login').click()#登陆按钮

    @classmethod
    def tearDownClass(cls):
        contexts = cls.driver.contexts
        for cotext in contexts:
            print(u'获取视图:', cotext)
        time.sleep(2)
        print('\n产品信息测试结束')
    def test_information0(self):
        '''提示toast'''
        # 定位toast元素
     #   WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
      #  toast_loc = ("xpath", ".//*[contains(@text,'平台账户暂未开放')]")
     #   t = WebDriverWait(self.driver, 10, 0.1).until(self.driver.presence_of_element_located(toast_loc))
        toast_loc = ("xpath", ".//*[contains(@text,'平台账户暂未开放')]")

        t = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_loc))

        print (t)
    # def test_xxxx(self):
    #     '''试验田'''
    #     time.sleep(5)
    #     #self.driver.background_app(2)
    #     self.driver.switch_to.context('NATIVE_APP')
    #     x = self.driver.get_window_size()['width']
    #     y = self.driver.get_window_size()['height']
    #     #self.driver.tap([(x * 0.1, y * 0.1)])
    #     WebDriverWait(self.driver, 50).until(
    #         lambda driver: self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/item_text'))
    #     self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/item_text')[2].click()




if __name__ == "__main__":
    unittest.main()