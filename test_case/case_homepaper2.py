# coding:utf-8
from appium import webdriver
import unittest, time, re, datetime
import login
import Base
class homepaper(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n首页UI测试开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=Base.setting())
        login.login(cls)
        login.port_login()
        time.sleep(5)  # 登陆首页
    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        print('\n首页UI测试结束')
    def test_homepape0(self):
        '''首页主要元素检查'''
        port_login = login.port_login()
        #核心企业开通融信
        if port_login['userType'] == 'CORE' and \
            port_login['CREDIT']==True and\
            port_login['RECEIVABLE']==False:
            print ('核心企业开通融信')
            #首页按钮为选中状态
            self.assertEqual('false',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_home').get_attribute('enabled'))
            #消息按钮为未选中
            self.assertEqual('true',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_message').get_attribute('enabled'))
            #我的为未选中
            self.assertEqual('true',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center').get_attribute('enabled'))
            self.driver.find_element_by_android_uiautomator('text(\"签发查询\")')           #签发查询
            self.driver.find_element_by_android_uiautomator('text(\"流转查询\")')           #流转查询
            self.driver.find_element_by_android_uiautomator('text(\"融资查询\")')           #融资查询
            self.driver.find_element_by_android_uiautomator('text(\"产品信息\")')           #产品信息
            self.driver.find_element_by_android_uiautomator('text(\"平台账户\")')           #平台账户
            # 左上角账单
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rx_account_button')
        #链条企业开通融信
        elif port_login['userType']=='CORP' and\
                port_login['CREDIT']==True and\
                port_login['RECEIVABLE']==False:
            print('链条企业开通融信')
            #首页按钮为选中状态
            self.assertEqual('false',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_home').get_attribute('enabled'))
            #消息按钮为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_message').get_attribute('enabled'))
            #我的为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center').get_attribute('enabled'))
            self.driver.find_element_by_android_uiautomator('text(\"流转查询\")')           #签发查询
            self.driver.find_element_by_android_uiautomator('text(\"融资查询\")')           #流转查询
            self.driver.find_element_by_android_uiautomator('text(\"产品信息\")')           #融资查询
            self.driver.find_element_by_android_uiautomator('text(\"平台账户\")')           #产品信息
            # 左上角账单
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rx_account_button')
            #融资中的融信
            self.driver.find_element_by_android_uiautomator('text(\"融资中的融信\")')
        #核心企业开通账款融资
        elif port_login['userType']=='CORE' and\
                port_login['CREDIT']==False and\
                port_login['RECEIVABLE']==True:
            print ('核心企业开通账款融资')
            #首页按钮为选中状态
            self.assertEqual('false',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_home').get_attribute('enabled'))
            #消息按钮为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_message').get_attribute('enabled'))
            #我的为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center').get_attribute('enabled'))
            self.driver.find_element_by_android_uiautomator('text(\"应收账款\")')
            self.driver.find_element_by_android_uiautomator('text(\"应付账款\")')
            self.driver.find_element_by_android_uiautomator('text(\"融资查询\")')
            self.driver.find_element_by_android_uiautomator('text(\"产品信息\")')
            self.driver.find_element_by_android_uiautomator('text(\"平台账户\")')
            # 左上角账单
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rx_account_button')
        #链条企业开通账款融资
        elif port_login['userType']=='CORP' and\
                port_login['CREDIT']==False and\
                port_login['RECEIVABLE']==True:
            print ('链条企业开通账款融资')
            #首页按钮为选中状态
            self.assertEqual('false',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_home').get_attribute('enabled'))
            #消息按钮为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_message').get_attribute('enabled'))
            #我的为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center').get_attribute('enabled'))
            self.driver.find_element_by_android_uiautomator('text(\"应收账款\")')
            self.driver.find_element_by_android_uiautomator('text(\"融资查询\")')
            self.driver.find_element_by_android_uiautomator('text(\"报名查询\")')
            self.driver.find_element_by_android_uiautomator('text(\"产品信息\")')
            self.driver.find_element_by_android_uiautomator('text(\"平台账户\")')
            # 左上角账单
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/zk_account_button')
            #融资中的账款
            self.driver.find_element_by_android_uiautomator('text(\"融资中的账款\")')
        #核心企业开通融信和账款融资
        elif port_login['userType']=='CORE' and\
                port_login['CREDIT']==True and\
                port_login['RECEIVABLE']==True:
            print ('核心企业开通融信和账款')
            #首页按钮为选中状态
            self.assertEqual('false',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_home').get_attribute('enabled'))
            #消息按钮为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_message').get_attribute('enabled'))
            #我的为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center').get_attribute('enabled'))
            self.driver.find_element_by_android_uiautomator('text(\"签发查询\")')           #签发查询
            self.driver.find_element_by_android_uiautomator('text(\"流转查询\")')           #流转查询
            self.driver.find_element_by_android_uiautomator('text(\"融资查询\")')           #流转查询
            self.driver.find_element_by_android_uiautomator('text(\"产品信息\")')           #融资查询
            self.driver.find_element_by_android_uiautomator('text(\"平台账户\")')           #产品信息
            # 左上角账单
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rxandzk_account_button')
            #TAB项
            self.driver.find_element_by_android_uiautomator('text(\"融信\")')
            self.driver.find_element_by_android_uiautomator('text(\"账款\")')
        #链条企业开通融信和帐款融资
        elif port_login['userType']=='CORP' and\
                port_login['CREDIT']==True and\
                port_login['RECEIVABLE']==True:
            print ('链条企业开通融信账款融资')
            #首页按钮为选中状态
            self.assertEqual('false',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_home').get_attribute('enabled'))
            #消息按钮为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_message').get_attribute('enabled'))
            #我的为未选中
            self.assertEqual('true',
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center').get_attribute('enabled'))
            self.driver.find_element_by_android_uiautomator('text(\"流转查询\")')           #签发查询
            self.driver.find_element_by_android_uiautomator('text(\"融资查询\")')           #流转查询
            self.driver.find_element_by_android_uiautomator('text(\"产品信息\")')           #融资查询
            self.driver.find_element_by_android_uiautomator('text(\"平台账户\")')           #产品信息
            # 左上角账单
            self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rxandzk_account_button')
            #TAB项
            self.driver.find_element_by_android_uiautomator('text(\"融信\")')
            self.driver.find_element_by_android_uiautomator('text(\"账款\")')
            #融资中的融信
            self.driver.find_element_by_android_uiautomator('text(\"融资中的融信\")')
    def test_homepaper1(self):
        '''剩余可用额度'''
        port_login = login.port_login()
        port_index = login.port_index()
        if port_login['userType'] == 'CORE':
            if port_login['CREDIT']==True:
                self.assertEqual(format(port_index['credit']['limitRemain'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/limitAvailable').text)        #剩余可用额度
            else:
                self.assertEqual(format(port_index['receivable']['limitRemain'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/limitAvailable').text)        #剩余可用额度
        else : print ('链条企业无此项')
            #百分比
         #   self.assertEqual('48',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/percent_limitAvailable').text)
    def test_homepaper2(self):
        '''签发总额度显示'''
        port_login = login.port_login()
        port_index = login.port_index()
        if port_login['userType'] == 'CORE':
            if port_login['CREDIT']==True:
                self.assertEqual(format(port_index['credit']['limitTotal'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_vpfirstrx_money').text)
            else:
                self.assertEqual(format(port_index['receivable']['limitTotal'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_vpfirstzk_money').text)
        else : print ('链条企业无此项')
    def test_homepaper3(self):
        '''搜索框'''
        port_login = login.port_login()
        if port_login['CREDIT']==True and port_login['RECEIVABLE']==True:
            print ('开通双业务搜索框不展示')
        else:
            self.driver.find_element_by_android_uiautomator('text(\"搜索企业名称／融信编号／金额／摘要\")')
    def test_homepaper4(self):
        '''已分配额度'''
        port_login = login.port_login()
        port_index = login.port_index()
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y * 0.75, x * 0.5, y * 0.05, 1000)
        if port_login['userType'] == 'CORE':
            if port_login['CREDIT']==True:
                self.assertEqual(format(port_index['credit']['limitDispatch'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/dispatch').text)        #剩余可用额度
            else:
                self.assertEqual(format(port_index['receivable']['limitDispatch'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/dispatch').text)        #剩余可用额度
        else : print ('链条企业无此项')
        #额度百分比
        #self.assertEqual('30',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/percent_dispatch').text)
    def test_homepaper5(self):
        '''已用额度'''
        port_login = login.port_login()
        port_index = login.port_index()
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 0.5, y * 0.75, x * 0.5, y * 0.05, 1000)
        if port_login['userType'] == 'CORE':
            if port_login['CREDIT']==True:
                self.assertEqual(format(port_index['credit']['limitUsed'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/used').text)        #剩余可用额度
            else:
                self.assertEqual(format(port_index['receivable']['limitUsed'],'0,.2f'),
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/used').text)        #剩余可用额度
        else : print ('链条企业无此项')
        #额度百分比
        #self.assertEqual('22',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/percent_used').text)
    def test_homepaper6(self):
        '''消息数'''
        try:
            port_message = login.port_message()
            self.assertEqual(port_message['allMessageCount'],
                             self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_total_unread_msg_count').text)
        except:
            print("没有新消息")
    def test_homepaper7(self):
        '''链条企业代签收金额'''
        port_login = login.port_login()
        port_index = login.port_index()
        if port_login['userType'] == 'CORP':
            if port_login['CREDIT']==True:
                self.assertEqual(port_index['corpCredit']['acceptAmount'],
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_vpfirstrx_money').text)
            else:
                self.assertEqual(port_index['corpReceivable']['acceptAmount'],
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_vpfirstrx_money').text)
        else: print('核心企业无此项')
    def test_homepaper8(self):
        '''链条企业可融资金额、持有金额'''
        port_login = login.port_login()
        port_index = login.port_index()
        if port_login['userType'] == 'CORP':
            if port_login['CREDIT']==True:
                self.assertEqual(port_index['corpCredit']['financeAmount'],
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_usefulmoney').text)
            else:
                self.assertEqual(port_index['corpReceivable']['financeAmount'],
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_usefulmoney').text)
        else: print('核心企业无此项')
    def test_homepaper9(self):
        '''链条企业15天到期金额'''
        port_login = login.port_login()
        port_index = login.port_index()
        if port_login['userType'] == 'CORP':
            if port_login['CREDIT']==True:
                self.assertEqual(port_index['corpCredit']['collectAmount'],
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_fifteendaymoney').text)
            else:
                self.assertEqual(port_index['corpReceivable']['collectAmount'],
                                 self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_fifteendaymoney').text)
        else: print('核心企业无此项')
if __name__ == "__main__":
    unittest.main()