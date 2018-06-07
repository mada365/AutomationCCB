#!/usr/bin/env
# coding:utf-8
from typing import List

from appium import webdriver
import unittest, time, re, datetime
import Base
from selenium.webdriver.support.wait import WebDriverWait
from Base import *
class qianfa2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n签发查询测试开始\n')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=setting())
        cls.driver.find_element_by_id(id+'/edit_companyname').click()
        cls.driver.find_element_by_id(id+'/edit_companyname').send_keys('全流程测试企业零一')
        cls.driver.find_element_by_id(id+'/edit_phonenumber').click()
        cls.driver.find_element_by_id(id+'/edit_phonenumber').send_keys('13683347984')
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

    def test_qianfa1(self):
        '''签发申请中'''
        time.sleep(5)
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[0].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无签发中数据')
        except:
            a = Base.huadong(self)
            print (a)
            b = port(self,'https://dev4.ccbscf.com/mobile/app/biz/issue/list')
            print (b)
            for i in range(len(a)):
                self.assertEqual(a[i]['供应商名称:'],b[i]['corpNameAccept'])
                self.assertEqual(a[i]['申请金额:'],b[i]['applyAmount'])
                self.assertEqual(a[i]['申请人:'], b[i]['personNameApply'])
                self.assertEqual(a[i]['申请日期:'], b[i]['applyTimeString'])

        #操作时间
     #   self.assertEqual('2018.04.14 16:06:39',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_operation_time').text)
     #    a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
     #    for i in a:
     #        print (i.text)
    def test_qianfa2(self):
        '''签发签发中'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[1].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无签发中数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = port(self,'https://dev4.ccbscf.com/mobile/app/biz/issue/list?type=ISSUING')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['供应商名称:'],b[i]['corpNameAccept'])
               # self.assertEqual(a[i]['融资金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['交易日期:'], b[i]['tradeTimeString'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])
    def test_qianfa3(self):
        '''签发已签发'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[2].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无已签发数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = port(self,'https://dev4.ccbscf.com/mobile/app/biz/issue/list?type=ISSUED')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['供应商名称:'],b[i]['corpNameAccept'])
                #self.assertEqual(a[i]['融信金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['签发日期:'], b[i]['issueTimeString'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])
    def test_qianfa4(self):
        '''签发付款中'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[3].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无付款中数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = port(self,'https://dev4.ccbscf.com/mobile/app/biz/issue/list?type=REDEEMING')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['供应商名称:'],b[i]['corpNameAccept'])
              #  self.assertEqual(a[i]['待付款金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['剩余天数:'], b[i]['remainDays'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])
    def test_qianfa5(self):
        '''签发已付款'''
        self.driver.find_elements_by_id(id + '/tv_indicator_title')[4].click()
        try:
            time.sleep(2)
            #暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无已付款数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = port(self,'https://dev4.ccbscf.com/mobile/app/biz/issue/list?type=REDEEMED')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['供应商名称:'],b[i]['corpNameAccept'])
                self.assertEqual(a[i]['待付款金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['剩余天数:'], b[i]['redeemTimeString'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])
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