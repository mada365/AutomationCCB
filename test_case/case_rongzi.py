#!/usr/bin/env
# coding:utf-8
from typing import List

from appium import webdriver
import unittest, time, re, datetime
import Base
from selenium.webdriver.support.wait import WebDriverWait
from Base import *
class rongzi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n融资查询测试开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=setting())
        cls.driver.find_element_by_id(id+'/edit_companyname').click()
        cls.driver.find_element_by_id(id+'/edit_companyname').send_keys('盛世集团成员二')
        cls.driver.find_element_by_id(id+'/edit_phonenumber').click()
        cls.driver.find_element_by_id(id+'/edit_phonenumber').send_keys('18910248213')
        cls.driver.find_element_by_id(id+'/edit_password').click()
        cls.driver.find_element_by_id(id+'/edit_password').send_keys('a1111111')
        time.sleep(1)
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/button_login').click()
       # time.sleep(5)  # 登陆首页
        WebDriverWait(cls.driver, 50).until(lambda driver: cls.driver.find_elements_by_android_uiautomator('text(\"融资查询\")'))
        cls.driver.find_element_by_android_uiautomator('text(\"融资查询\")').click()
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        contexts = cls.driver.contexts
        for cotext in contexts:
            print(u'获取视图:',cotext)
        time.sleep(2)
        print('\n融资查询测试结束')
    def test_rongzi0(self):
        '''融资首页主要元素检查'''
        # 签发页标题：签发查询
        a = self.driver.find_element_by_id(id+'/tv_title_content')
        self.assertEqual(a.text,'融资查询')
        #返回按钮检查
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back')
        #查询按钮检查
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_search')
        #tab检查
        l= ['融资中','已融资']
        b = self.driver.find_elements_by_id(id+'/tv_indicator_title')
        for i in range(len(b)):
            self.assertEqual(b[i].text,l[i],'标题可能有错误')
    def test_rongzi1(self):
        '''融资中'''
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            #操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
            for i in a:
                print (i.text)
    def test_rongzi2(self):
        '''已融资'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[1].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            #操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
            for i in a:
                print (i.text)

if __name__ == "__main__":
    unittest.main()