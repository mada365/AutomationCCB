#coding:utf-8
import unittest
import os,time
#sys.path.append('test_case')
#from test_case import *
import HTMLTestRunner

#执行测试套件
# runner = unittest.TextTestRunner()
# runner.run(testunit)
listaa = 'test_case'
def creatsuitel():
    testunit = unittest.TestSuite()
    # discover方法定义

    discover = unittest.defaultTestLoader.discover(listaa,
                                                   pattern='case_*.py',
                                                   top_level_dir=None)
    # 添加到测试套件
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTest(test_case)
            print (testunit)
    return testunit
alltestnames = creatsuitel()

now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename='Report/'+'report'+now+'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'建信融通APP',
    description=u'用例执行：'
     )
# 运行测试用例
runner.run(alltestnames)
