#!/usr/bin/env
# coding:utf-8
from typing import List
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import unittest, time, re, datetime
import Base
from selenium.webdriver.support.wait import WebDriverWait
import login

class liuzhuan(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('\n流转查询测试开始\n')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=Base.setting())
        login.login()
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
        cls.driver.quit()
        print('\n流转查询测试结束')
    def test_liuzhuan1(self):
        '''流转签收中'''
        self.driver.find_element_by_android_uiautomator('text(\"签收中\")').click()
        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = Base.port(self,'https://dev4.ccbscf.com/mobile/app/biz/exchange/list?type=ACCEPTING')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['采购商名称:'],b[i]['corpNameTransfer'])
                #self.assertEqual(a[i]['融信金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['交易日期:'], b[i]['tradeTimeString'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])

    def test_liuzhuan2(self):
        '''流转已签收'''
        self.driver.find_element_by_android_uiautomator('text(\"已签收\")').click()
        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = Base.port(self,'https://dev4.ccbscf.com/mobile/app/biz/exchange/list?type=ACCEPTED')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['采购商名称:'],b[i]['corpNameTransfer'])
                #self.assertEqual(a[i]['融信金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['签收日期:'], b[i]['acceptTimeString'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])
    def test_liuzhuan3(self):
        '''流转转让中'''
        self.driver.find_element_by_android_uiautomator('text(\"转让中\")').click()

        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = Base.port(self,'https://dev4.ccbscf.com/mobile/app/biz/exchange/list?type=TRANSFERING')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['供应商名称:'],b[i]['corpNameAccept'])
                #self.assertEqual(a[i]['融信金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['交易日期:'], b[i]['tradeTimeString'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])

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
            a = Base.huadong(self)
            print(a)
            b = Base.port(self,'https://dev4.ccbscf.com/mobile/app/biz/exchange/list?type=TRANSFERED')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['供应商名称:'],b[i]['corpNameAccept'])
                #self.assertEqual(a[i]['融信金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['转让日期:'], b[i]['transferTimeString'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])

    def test_liuzhuan5(self):
        '''流转收款中'''
        self.driver.find_element_by_android_uiautomator('text(\"收款中\")').click()
        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = Base.port(self,'https://dev4.ccbscf.com/mobile/app/biz/exchange/list?type=COLLECTING')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['采购商名称:'],b[i]['corpNameTransfer'])
                #self.assertEqual(a[i]['本次收款金额:'],b[i]['collect'])
                self.assertEqual(a[i]['承诺付款日期:'], b[i]['maturityDateString'])
                self.assertEqual(a[i]['剩余回款天数:'], b[i]['remainDays'])
                self.assertEqual(a[i]['融信状态：'],b[i]['creditStateMain'])

    def test_liuzhuan6(self):
        '''流转已收款'''
        self.driver.find_element_by_android_uiautomator('text(\"已收款\")').click()
        try:
            time.sleep(2)
            # 暂无数据的图片
            self.driver.find_element_by_id(id + '/status_empty').find_element_by_class_name('android.widget.ImageView')
            print('暂无数据')
        except:
            a = Base.huadong(self)
            print(a)
            b = Base.port(self,'https://dev4.ccbscf.com/mobile/app/biz/exchange/list?type=COLLECTED')
            print(b)
            for i in range(len(a)):
                self.assertEqual(a[i]['采购商名称:'],b[i]['corpNameTransfer'])
                #self.assertEqual(a[i]['融信金额:'],b[i]['maturityAmount'])
                self.assertEqual(a[i]['收款日期:'], b[i]['redeemTimeString'])
                self.assertEqual(a[i]['融信状态:'], b[i]['creditStateMain'])

if __name__ == "__main__":
    unittest.main()