#coding:utf-8

#import sys
import unittest
import os,time
#sys.path.append('test_case')
#from test_case import *
import HTMLTestRunner
#调用数组文件
#import allcase_list
#获取用例
#alltestnames = allcase_list.caselist()
#创建测试套件
#testunit = unittest.TestSuite()
#循环用例添加到容器
#for test in alltestnames:
#    testunit.addTest(unittest.makeSuite(test))
#添加用例到测试容器
#testunit.addTest(unittest.makeSuite(baidu.Baidu))
#testunit.addTest(unittest.makeSuite(youdao.Youdao))

#执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)
listaa = 'test_case'
def creatsuitel():
    testunit = unittest.TestSuite()
    #discover方法定义
    discover = unittest.defaultTestLoader.discover(listaa,
                                                   pattern='case_*.py',
                                                   top_level_dir=None)
    #添加到测试套件
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTest(test_case)
            print testunit
    return testunit
alltestnames = creatsuitel()

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename='report'+now+'result.html'
fp = file(filename, 'wb')
runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'热点云测试报告',
    description=u'用例执行：'
     )

    # #运行测试用例
runner.run(alltestnames)
