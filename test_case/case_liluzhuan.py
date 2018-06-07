#!/usr/bin/env
# coding:utf-8
from typing import List
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import unittest, time, re, datetime
import Base
from selenium.webdriver.support.wait import WebDriverWait
from Base import *


class liuzhuan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n流转查询测试开始\n')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=setting())
        cls.driver.find_element_by_id(id + '/edit_companyname').click()
        cls.driver.find_element_by_id(id + '/edit_companyname').send_keys('盛世集团成员二')
        cls.driver.find_element_by_id(id + '/edit_phonenumber').click()
        cls.driver.find_element_by_id(id + '/edit_phonenumber').send_keys('18910248213')
        cls.driver.find_element_by_id(id + '/edit_password').click()
        cls.driver.find_element_by_id(id + '/edit_password').send_keys('a1111111')
        time.sleep(1)
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/button_login').click()
        # time.sleep(5)  # 登陆首页
        WebDriverWait(cls.driver, 50).until(
            lambda driver: cls.driver.find_elements_by_android_uiautomator('text(\"流转查询\")'))
        cls.driver.find_element_by_android_uiautomator('text(\"流转查询\")').click()
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        contexts = cls.driver.contexts
        for cotext in contexts:
            print(u'获取视图:', cotext)
        time.sleep(2)
        print('\n流转查询测试结束')
    def test_liuzhuan0(self):
        '''流转查询首页元素检查'''
        # 流转页标题：流转查询
        self.assertEqual(self.driver.find_element_by_id(id + '/tv_title_content').text,'流转查询')
        # 返回按钮检查
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back')
        # 查询按钮检查
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_search')
        # 申请中、签发中、已签发、付款中、已付款、已收款tab检查
        l = ['签收中', '已签收', '转让中', '已转让', '收款中','已收款']
        b = self.driver.find_element_by_id(id+'/title_container').find_elements_by_class_name('android.widget.TextView')
        for i in range(len(b)):
            self.assertEqual(b[i].text, l[i], '标题可能有错误')
        self.driver.drag_and_drop(b[-1],b[0])
        self.assertEqual((b[-1].text),l[-1],'标题可能有误')
        self.driver.drag_and_drop(b[0],b[-1])
    def test_liuzhuan1(self):
        '''流转签收中'''
        self.driver.find_element_by_android_uiautomator('text(\"签收中\")').click()

        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            # 操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name(
                'android.widget.TextView')
            for i in a:
                print(i.text)

    def test_liuzhuan2(self):
        '''流转已签收'''
        self.driver.find_element_by_android_uiautomator('text(\"已签收\")').click()
        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            # 操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name(
                'android.widget.TextView')
            for i in a:
                print(i.text)

    def test_liuzhuan3(self):
        '''流转转让中'''
        self.driver.find_element_by_android_uiautomator('text(\"转让中\")').click()

        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            # 操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name(
                'android.widget.TextView')
            for i in a:
                print(i.text)

    def test_liuzhuan4(self):
        '''流转已转让'''
        self.driver.find_element_by_android_uiautomator('text(\"已转让\")').click()
        # self.driver.find_element_by_id(id + '/title_container').find_elements_by_class_name('android.widget.TextView')[3].click()
        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            # 操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name(
                'android.widget.TextView')
            for i in a:
                print(i.text)

    def test_liuzhuan5(self):
        '''流转收款中'''
        self.driver.find_element_by_android_uiautomator('text(\"收款中\")').click()
        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            # 操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name(
                'android.widget.TextView')
            for i in a:
                print(i.text)

    def test_liuzhuan6(self):
        '''流转已收款'''
        self.driver.find_element_by_android_uiautomator('text(\"已收款\")').click()
        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            # 操作时间
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')
            a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name(
                'android.widget.TextView')
            for i in a:
                print(i.text)

if __name__ == "__main__":
    unittest.main()