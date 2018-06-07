#!/usr/bin/env
# coding:utf-8
from typing import List

from appium import webdriver
import unittest, time, re, datetime
import Base
from selenium.webdriver.support.wait import WebDriverWait
from Base import *
class qianfa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n签发查询测试开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=setting())
        cls.driver.find_element_by_id(id+'/edit_companyname').click()
        cls.driver.find_element_by_id(id+'/edit_companyname').send_keys('盛世集团成员二')
        cls.driver.find_element_by_id(id+'/edit_phonenumber').click()
        cls.driver.find_element_by_id(id+'/edit_phonenumber').send_keys('18910248213')
        cls.driver.find_element_by_id(id+'/edit_password').click()
        cls.driver.find_element_by_id(id+'/edit_password').send_keys('a1111111')
        time.sleep(1)
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/button_login').click()
        WebDriverWait(cls.driver, 50).until(lambda driver: cls.driver.find_elements_by_android_uiautomator('text(\"签发查询\")'))
        cls.driver.find_element_by_android_uiautomator('text(\"签发查询\")').click()
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        contexts = cls.driver.contexts
        for cotext in contexts:
            print(u'获取视图:',cotext)
        time.sleep(2)
        print('\n签发查询测试结束')
    def test_qianfa0(self):
        '''签发首页主要元素检查'''
        # 签发页标题：签发查询
        a = self.driver.find_element_by_id(id+'/tv_title_content')
        self.assertEqual(a.text,'签发查询')
        #返回按钮检查
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back')
        #查询按钮检查
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_search')
        #申请中、签发中、已签发、付款中、已付款tab检查
        l= ['申请中','签发中','已签发','付款中','已付款']
        b = self.driver.find_elements_by_id(id+'/tv_indicator_title')
        for i in range(len(b)):
            self.assertEqual(b[i].text,l[i],'标题可能有错误')
    def test_qianfa1(self):
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[0].click()
        '''签发申请中'''
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('签发申请中暂无数据')
        except:
            #操作时间
            self.assertEqual('2018.04.14 16:06:39',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time').text)
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
            for i in a:
                print (i.text)
    def test_qianfa2(self):
        '''签发签发中'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[1].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无签发中数据')
        except:
            #操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
            for i in a:
                print (i.text)
    def test_qianfa3(self):
        '''签发已签发'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[2].click()

        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无已签发数据')
        except:
            #操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
            for i in a:
                print (i.text)
    def test_qianfa4(self):
        '''签发付款中'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[3].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无付款中数据')
        except:
            #操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
            for i in a:
                print (i.text)
    def test_qianfa5(self):
        '''签发已付款'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[4].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无已付款数据')
        except:
            #操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
            for i in a:
                print (i.text)
    # def test_qianfa6(self):
    #     '''签发页搜索元素检查'''
    #     self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_search').click()
    #     time.sleep(2)
    #     #返回按钮
    #     self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_go_back')
    #     #搜索框
    #     a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/textView_searchtext').text
    #     self.assertEqual(a,'搜索企业名称／融信编号／金额／摘要','搜索框显示信息不正确')
    #     self.assertEqual(self.drvier.find_element_by_class_name('android.widget.TextView').text,'搜索历史')
    #     self.driver.press_keycode(4)

if __name__ == "__main__":
    unittest.main()