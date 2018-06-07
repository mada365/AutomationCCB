# coding:utf-8
from appium import webdriver
import unittest, time, re, datetime
import Base
import login
from selenium.webdriver.support.ui import WebDriverWait
class bill(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print('\n缴费账单页测试开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=Base.setting())
        login.login(cls)
        try:
            WebDriverWait(cls.driver, 5, 2).until(
                lambda driver: cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rx_account_button'))
            cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rx_account_button').click()
        except:
            cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rxandzk_account_button').click()
        # WebDriverWait(cls.driver,10,2).until(
        #     lambda driver: cls.driver.find_elements_by_class_name('android.widget.ImageView')[0])
        # cls.driver.find_elements_by_class_name('android.widget.ImageView')[0].click()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()
        print('\n缴费账单页测试结束')
    def test_bill0(self):
        '''主要元素检查'''
        #缴费账单标题
        self.assertEqual('缴费账单',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/account_detail_name').text)
        #账单类型TAB
        self.assertEqual('账单类型',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_billtype').text)
        #缴费状态TAB
        self.assertEqual('缴费状态',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_ispaid').text)
        #返回按钮
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back')
    def test_bill1(self):
        '''账单类型、缴费状态下拉单内容检查'''
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_billtype').click()
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_ispaid').click()
    def test_bill2(self):
        '''账单列表检查'''
        try:
            # 账单列表
            list=self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/llitem')[0]
            a=list.find_element_by_id('com.ccbscf.mobile.corp:id/tv_billtypestring').text          #账单类型
            b=list.find_element_by_id('com.ccbscf.mobile.corp:id/tv_ispaidstring').text            #缴费状态
            c=list.find_element_by_id('com.ccbscf.mobile.corp:id/tv_totalamount').text         #金额
            print ('\n对账：',a,b,c)
        except:
            print ('账单列表检查无数据')
    def test_bill3(self):
        '''账单详情数据检查'''

        list = self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/llitem')[0]
        list.find_element_by_id('com.ccbscf.mobile.corp:id/tv_totalamount').click()
        time.sleep(5)
        #账单详细页账单详情
        self.assertEqual('账单详情',self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_title')[0].text)
            #各项名称
        a = self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_title')
            #各项数值
        b = self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_content')
        for i in range(1,len(a)):         #账单编号
            print('\n',a[i].text,b[i-1].text)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back').click()

    def test_bill4(self):
        '''账单明细数据检查'''
        list = self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/llitem')[0]
        list.find_element_by_id('com.ccbscf.mobile.corp:id/tv_totalamount').click()
        #进入账单明细页按钮
        WebDriverWait(self.driver,10,2).until(
            lambda driver: self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_billtypestring'))
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_billtypestring').click()
        #账单明细详情标题
        time.sleep(2)
        self.assertEqual('账单明细',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_title').text)         #账单明细页标题
        a = self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_title')           #账单明细标题
        b = self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_content')         #账单明细数值
        for i in range(1,len(a)):
            print('\n',a[i].text,b[i-1].text)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back').click()
        time.sleep(1)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back').click()


if __name__ == "__main__":
    unittest.main()