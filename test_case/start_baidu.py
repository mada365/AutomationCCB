#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import  NoSuchElementException
import unittest,time,re
import HTMLTestRunner

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = '/test/geckodriver')
        self.driver.implicitly_wait(30)
        self.base_url="http://www.baidu.com"
        self.verifficationErrors=[]
        self.accept_next_alert = True
#搜索测试yongli
    def test_baidu_search(self):
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
#百度设置用例
    def test_baidu_set(self):
        u"""百度设置"""
        driver = self.driver

        driver.get(self.base_url+"/gaoji/preferences.html")

        m = driver.find_element_by_xpath('//*[@id="sh_2"]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="save"]').click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):

        self.driver.quit()
        self.assertEqual([], self.verifficationErrors)
if __name__=="__main__":
    unittest.main()

    #定义测试容器
    # testunit=unittest.TestSuite()
    # #测试用例加入容器
    # testunit.addTest(Baidu("test_baidu_search"))
    # testunit.addTest(Baidu("test_baidu_set"))
    # #定义报告地址
    # filename='/Users/mada/result.html'
    # fp = file(filename, 'wb')
    # #定义测试报告
    # runner=HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'百度搜索测试报告',
    #     description=u'用例执行：'
    # )
    #
    # #运行测试用例
    # runner.run(testunit)