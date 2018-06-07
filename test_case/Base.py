#!/usr/bin/env
# -*- coding: utf-8 -*-
import unittest, time, re, datetime
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# 使用正则表达式筛选设备 id
import re
import requests

# 使用 os 模块调用命令
import os

# 测试的包的路径和包名
appLocation = "/Users/mada/Downloads/jxrt-release.apk"

# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())

# 正则表达式匹配出 id 信息
deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]

# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]

# 读取 APK 的 package 信息
#appPackageAdb = list(os.popen('aapt dump badging ' + appLocation ).readlines())
#appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]

# 删除以前的安装包
#os.system('adb uninstall ' + appPackage)

def setting():
    desired_caps = {}
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = deviceAndroidVersion
    desired_caps['deviceName'] = deviceId  # adb devices查到的设备名
    desired_caps['app'] = appLocation  # 被测试应用在电脑上的位置
    desired_caps['appPackage'] = 'com.ccbscf.mobile.corp'
    desired_caps['appActivity'] = 'com.ccbscf.mobile.corp.ui.activity.MainActivity'
    desired_caps['autoLaunch'] = 'true'  # 是否需要启动或安装app默认为true
    desired_caps['noReset'] = 'true'  # 会话前是否重置app状态，true为不需要,默认false
    desired_caps['newCommandTimeout'] = 20  # 设置未接收到新命令的超时时间，默认60s
    desired_caps["unicodeKeyboard"] = "True"  # 屏蔽了键盘中文
    desired_caps["resetKeyboard"] = "True"  # 为了输入中文
    desired_caps["autoAcceptAlerts"]="True"
    return (desired_caps)

print (setting())
#各种常量
id = 'com.ccbscf.mobile.corp:id'

#向下滑动列表获得列表内容数据
def huadong(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    z=0
    li=[]
    while True:
        a = self.driver.page_source
        element = self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/cv_info').find_elements_by_class_name('android.widget.TextView')
        dic={}
        for i in range(len(element)-1):
            if i%2==0:
                 dic[element[i].text]=element[i+1].text
        print(dic)
        #向下滑动动作
        #self.driver.drag_and_drop(self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')[1], self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')[0],)
        #self.driver.scroll(self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')[1], self.driver.find_elements_by_id('com.ccbscf.mobile.corp:id/tv_operation_time')[0],)
        #time.sleep(0.5)
        self.driver.swipe(x * 1035 / 1080, y * 1919 / 1920, x * 1035 / 1080, y * 1131 / 1920, 3000)
        time.sleep(0.2)
        b = self.driver.page_source
        z+=1
        li.append(dic)
        if a == b or z==10:
            break
    return (li)
#请求接口数据
def port(self,urs):
    dev4 = 'dev4.ccbscf.com'
    url = "https://dev4.ccbscf.com/uaa/app/login"
#   urs = "https://dev4.ccbscf.com/mobile/app/biz/issue/list"
    gtasks = 'https://dev4.ccbscf.com/mobile/app/corp/gtasks/list'
    values = {}
    values['name'] = '全流程测试企业零三'
    values['password'] = 'a1111111'
    values['appId'] = '865296036668109F0%3AC8%3A50%3AAF%3AD9%3A3B'
    values['appType'] = 'android'
    values['mobile'] = '13552317374'
    ret = requests.post(url=url, data=values, verify=False)
    data = ret.json()
    # print (data)
    accesstoken = data['data']['accessToken']
    refreshtoken = data['data']['refreshToken']
    header = {}
    header['User-Agent'] = 'okhttp/3.3.0'
    header['page'] = '1'
    header['pageSize'] = '15'
    header['refreshToken'] = refreshtoken
    a = requests.get(url=urs, headers=header, verify=False)
    b = a.json()
    print(b)
    lis = b['data']['datalist']
    return lis


#重新封装
def find_elements(self,loc):
    '''封装一组元素定位方法'''
    try:
        if len(self.driver.find_elements(*loc)):
            return self.driver.find_elements(*loc)
    except Exception as e:
        print(u"%s 页面中未能找到 %s 元素" %(self,loc))
        return False
# def find_element(self,loc):
#     '''封装单个元素定位方法'''
#     try:
#         WebDriverWait(self.driver,15.).until(lambdadriver:driver.find_element(*loc).is_displayed())
#         return self.driver.find_element(*loc)
#     except Exception as e:
#         print(u"%s 页面中未能找到 %s 元素" %(self,loc))
#         return False




