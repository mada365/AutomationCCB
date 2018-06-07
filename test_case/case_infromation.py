#!/usr/bin/env
# coding:utf-8
from typing import List
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import unittest, time, re, datetime

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

import Base
from selenium.webdriver.support.wait import WebDriverWait

import login

class information(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        print('\n产品信息测试开始\n')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=Base.setting())
        login.login(cls )
        WebDriverWait(cls.driver, 50).until(
            lambda driver: cls.driver.find_elements_by_android_uiautomator('text(\"产品信息\")'))
        cls.driver.find_element_by_android_uiautomator('text(\"产品信息\")').click()
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        contexts = cls.driver.contexts
        for cotext in contexts:
            print(u'获取视图:', cotext)
        cls.driver.quit()
        print('\n产品信息测试结束')
    def test_information0(self):
        '''产品信息首页标题'''
        port_login = login.port_login()
        #开通了融信和账款融资
        if port_login['CREDIT']==True and\
            port_login['RECEIVABLE']==True:
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_rongxin')
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_lianxin')
        else:
            self.assertEqual('产品信息',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_rongxin').text,'标题不正确')
    def test_information1(self):
        '''产品信息字段展示'''
        port_login = login.port_login()
        #核心企业开通了融信
        if port_login['userType'] == 'CORE':
            if port_login['CREDIT']==True:
                # 持有总额
                self.assertEqual('持有总额',
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_amount_of_money_label').text)
                # 累计签发
                self.assertEqual('累计签发', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_1').text)
                # 累计签收
                self.assertEqual('累计签收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_2').text)
                # 累计转让
                self.assertEqual('累计转让', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_3').text)
                # 累计融资
                self.assertEqual('累计融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_4').text)
                # 累计付款
                self.assertEqual('累计付款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_5').text)
                # 累计收款
                self.assertEqual('累计收款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_6').text)
            else:
                self.assertEqual('持有总额',
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_amount_of_money_label').text)
                self.assertEqual('确认应付', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_1').text)
                # 累计签收
                self.assertEqual('确认应收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_2').text)
                # 累计转让
                self.assertEqual('累计融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_3').text)
                # 累计融资
                self.assertEqual('累计付款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_4').text)
                # 累计付款
                self.assertEqual('累计收款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_5').text)
        else:
            if port_login['CREDIT']==True:
                # 持有总额
                self.assertEqual('持有总额',
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_amount_of_money_label').text)
                # 累计签发
                self.assertEqual('累计签收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_1').text)
                # 累计签收
                self.assertEqual('累计转让', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_2').text)
                # 累计转让
                self.assertEqual('累计融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_3').text)
                # 累计融资
                self.assertEqual('累计收款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_4').text)

            else:
                self.assertEqual('持有总额',
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_amount_of_money_label').text)
                self.assertEqual('确认应收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_1').text)
                # 累计签收
                self.assertEqual('累计融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_2').text)
                # 累计转让
                self.assertEqual('累计收款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_label_3').text)

    def test_information2(self):
        '''产品信息页折线图字段展示'''
        port_login = login.port_login()
        # 核心企业开通了融信
        if port_login['userType'] == 'CORE':
            if port_login['CREDIT'] == True:
                self.assertEqual('融信签发',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_type').text)
                self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_change_chart_type').click()
                time.sleep(1)
                self.assertEqual('签发', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_issue').text)
                self.assertEqual('签收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_accept').text)
                self.assertEqual('转让', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_transfer').text)
                self.assertEqual('融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_finance').text)
                self.assertEqual('付款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_redeem').text)
                self.assertEqual('收款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_collect').text)
                #切换到签收
                self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_accept').click()
                self.assertEqual('融信签收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_type').text)
            else :
                self.assertEqual('账款确认应付',
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_type').text)
                self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_change_chart_type').click()
                time.sleep(1)
                self.assertEqual('确认应付', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_issue').text)
                self.assertEqual('确认应收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_accept').text)
                self.assertEqual('融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_finance').text)
                self.assertEqual('付款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_redeem').text)
                self.assertEqual('收款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_collect').text)
                # 切换到确认应收
                self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_accept').click()
                self.assertEqual('账款确认应收',
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_type').text)
        else :
            if port_login['CREDIT'] == True:
                self.assertEqual('融信签收',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_type').text)
                self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_change_chart_type').click()
                time.sleep(1)
                self.assertEqual('签收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_accept').text)
                self.assertEqual('转让', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_transfer').text)
                self.assertEqual('融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_finance').text)
                self.assertEqual('收款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_collect').text)
                #切换到融资
                self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_finance').click()
                self.assertEqual('融信融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_type').text)
            else :
                self.assertEqual('账款确认应收',
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_type').text)
                self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_change_chart_type').click()
                time.sleep(1)
                self.assertEqual('确认应收', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_accept').text)
                self.assertEqual('融资', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_finance').text)
                self.assertEqual('收款', self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_collect').text)

                # 切换到确认收款
                self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_collect').click()
                self.assertEqual('账款收款',
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_type').text)
    def test_information3(self):
        '''产品信息数值展示'''
        port_login = login.port_login()
        # 核心企业开通了融信
        if port_login['userType'] == 'CORE':
            if port_login['CREDIT'] == True:
                port_product = login.port_productCredit()
                # 持有总额
                self.assertEqual(format(port_product['holdAmount'],'0,.2f'),
                                 self.driver.find_element_by_id(
                                     'com.ccbscf.mobile.corp:id/tv_amount_of_money').text)
                # 累计签发
                self.assertEqual(format(port_product['issueAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_1').text)
                # 累计签收
                self.assertEqual(format(port_product['acceptAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_2').text)
                # 累计转让
                self.assertEqual(format(port_product['transferAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_3').text)
                # 累计融资
                self.assertEqual(format(port_product['financeAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_4').text)
                # 累计付款
                self.assertEqual(format(port_product['redeemAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_5').text)
                # 累计收款
                self.assertEqual(format(port_product['collectAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_6').text)
            #核心企业开通账款融资
            else:
                port_product = login.port_productReceivable()
                self.assertEqual(format(port_product['holdAmount'],'0,.2f'),
                                 self.driver.find_element_by_id(
                                     'com.ccbscf.mobile.corp:id/tv_amount_of_money').text)
                self.assertEqual(format(port_product['issueAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_1').text)
                # 累计签收
                self.assertEqual(format(port_product['acceptAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_2').text)
                #累计转让
                self.assertEqual(format(port_product['financeAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_3').text)
                # 累计付款
                self.assertEqual(format(port_product['redeemAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_4').text)
                # 累计收款
                self.assertEqual(format(port_product['collectAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_5').text)
        else:
            if port_login['CREDIT'] == True:
                port_product = login.port_productCredit()
                # 持有总额
                self.assertEqual(format(port_product['holdAmount'],'0,.2f'),
                                 self.driver.find_element_by_id(
                                     'com.ccbscf.mobile.corp:id/tv_amount_of_money').text)
                # 累计签收
                self.assertEqual(format(port_product['acceptAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_1').text)
                # 累计转让
                self.assertEqual(format(port_product['transferAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_2').text)
                # 累计转让
                self.assertEqual(format(port_product['financeAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_3').text)
                # 累计收款
                self.assertEqual(format(port_product['collectAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_4').text)
            else:
                port_product = login.port_productReceivable()
                self.assertEqual(format(port_product['holdAmount'],'0,.2f'),
                                 self.driver.find_element_by_id(
                                     'com.ccbscf.mobile.corp:id/tv_amount_of_money').text)
                #确认应收
                self.assertEqual(format(port_product['issueAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_1').text)
                # 累计融资
                self.assertEqual(format(port_product['financeAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_1').text)
                # 累计收款
                self.assertEqual(format(port_product['collectAmount'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_value_1').text)
    def test_information4(self):
        '''产品信息数值展示'''
        a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/ll_nine_grid_container')
        b = a.find_elements_by_class_name('android.widget.TextView')
        for i in range(len(b)):
            if i%2==1:
                b[i].click()
                time.sleep(2)
                try:
                    self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/status_empty').find_element_by_class_name(
                        'android.widget.ImageView')
                    print('暂无数据')
                    self.driver.keyevent('4')
                except:
                    self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_amount').click()
                    time.sleep(2)
                    a = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/recycle_view').find_elements_by_class_name(
                        "android.widget.TextView")
                    for i in a:
                        print (i.text)
                    self.driver.keyevent('4')
                    self.driver.keyevent('4')
    def test_information5(self):
        '''通用元素'''
        #产品信息页返回按钮
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back')
        #日期
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_month')
        #日历
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_change_date')
        #融信日期段
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_chart_time_range')
        #折线图
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/lc_detail')
    def test_information6(self):
        '''日历拉起功能'''
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_change_date').click()
        time.sleep(1)
        a = self.driver.find_elements_by_class_name('android.widget.TextView')
        for i in a:
            print (i.text)
        self.driver.keyevent('4')
if __name__ == "__main__":
    unittest.main()