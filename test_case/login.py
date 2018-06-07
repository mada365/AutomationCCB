from appium import webdriver
import Base
from Base import *
import unittest
name = '马到成功'
phone = '18910248213'
password = 'a1111111'
def login(self):
    driver = self.driver
    driver.find_element_by_id(id + '/edit_companyname').click()
    driver.find_element_by_id(id + '/edit_companyname').send_keys(name)
    driver.find_element_by_id(id + '/edit_phonenumber').click()
    driver.find_element_by_id(id + '/edit_phonenumber').send_keys(phone)
    driver.find_element_by_id(id + '/edit_password').click()
    driver.find_element_by_id(id + '/edit_password').send_keys(password)
    driver.find_element_by_id('com.ccbscf.mobile.corp:id/button_login').click()
def port_login():
    #登陆
    login = "https://dev4.ccbscf.com/uaa/app/login"
    values = {}
    values['name'] = name
    values['password'] = password
    values['appId'] = '865296036668109F0%3AC8%3A50%3AAF%3AD9%3A3B'
    values['appType'] = 'android'
    values['mobile'] = phone
    ret = requests.post(url=login, data=values, verify=False)
    data = ret.json()
    #企业开通产品
    products = data['data']['products']
    #企业类型
    userType = data['data']['user']
    return {**userType,**products}
#登陆以后
def port_index():
    #登陆
    login = "https://dev4.ccbscf.com/uaa/app/login"
    #首页接口
    index = 'https://dev4.ccbscf.com/mobile/app/index'
    #首页消息
    message = 'https://dev4.ccbscf.com/mobile/app/corp/message/index?random=poll'
    values = {}
    values['name'] = name
    values['password'] = password
    values['appId'] = '865296036668109F0%3AC8%3A50%3AAF%3AD9%3A3B'
    values['appType'] = 'android'
    values['mobile'] = phone
    ret = requests.post(url=login, data=values, verify=False)
    data = ret.json()
    #token值
    accesstoken = data['data']['accessToken']
    refreshtoken = data['data']['refreshToken']
    header = {}
    header['User-Agent'] = 'okhttp/3.3.0'
    header['page'] = '1'
    header['pageSize'] = '15'
    header['refreshToken'] = refreshtoken
    ret = requests.get(url=index, headers=header, verify=False)
    json = ret.json()
    data = json['data']
    return data
#消息
def port_message():
    #登陆
    login = "https://dev4.ccbscf.com/uaa/app/login"
    #首页接口
    index = 'https://dev4.ccbscf.com/mobile/app/index'
    #首页消息
    message = 'https://dev4.ccbscf.com/mobile/app/corp/message/index?random=poll'
    values = {}
    values['name'] = name
    values['password'] = password
    values['appId'] = '865296036668109F0%3AC8%3A50%3AAF%3AD9%3A3B'
    values['appType'] = 'android'
    values['mobile'] = phone
    ret = requests.post(url=login, data=values, verify=False)
    data = ret.json()
    #token值
    accesstoken = data['data']['accessToken']
    refreshtoken = data['data']['refreshToken']
    header = {}
    header['User-Agent'] = 'okhttp/3.3.0'
    header['page'] = '1'
    header['pageSize'] = '15'
    header['refreshToken'] = refreshtoken
    ret = requests.get(url=message, headers=header, verify=False)
    json = ret.json()
    data = json['data']
    return data
#产品信息融信
def port_productCredit():
    #登陆
    login = "https://dev4.ccbscf.com/uaa/app/login"
    #产品信息
    product = 'https://dev4.ccbscf.com/mobile/app/biz/common/product/states?product=CREDIT'
    values = {}
    values['name'] = name
    values['password'] = password
    values['appId'] = '865296036668109F0%3AC8%3A50%3AAF%3AD9%3A3B'
    values['appType'] = 'android'
    values['mobile'] = phone
    ret = requests.post(url=login, data=values, verify=False)
    data = ret.json()
    #token值
    accesstoken = data['data']['accessToken']
    refreshtoken = data['data']['refreshToken']
    header = {}
    header['User-Agent'] = 'okhttp/3.3.0'
    header['page'] = '1'
    header['pageSize'] = '15'
    header['refreshToken'] = refreshtoken
    ret = requests.get(url=product, headers=header, verify=False)
    json = ret.json()
    data = json['data']
    return data
#产品信息账款
def port_productReceivable():
    #登陆
    login = "https://dev4.ccbscf.com/uaa/app/login"
    #产品信息
    product = 'https://dev4.ccbscf.com/mobile/app/biz/common/product/states?product=RECEIVABLE'
    values = {}
    values['name'] = name
    values['password'] = password
    values['appId'] = '865296036668109F0%3AC8%3A50%3AAF%3AD9%3A3B'
    values['appType'] = 'android'
    values['mobile'] = phone
    ret = requests.post(url=login, data=values, verify=False)
    data = ret.json()
    #token值
    accesstoken = data['data']['accessToken']
    refreshtoken = data['data']['refreshToken']
    header = {}
    header['User-Agent'] = 'okhttp/3.3.0'
    header['page'] = '1'
    header['pageSize'] = '15'
    header['refreshToken'] = refreshtoken
    ret = requests.get(url=product, headers=header, verify=False)
    json = ret.json()
    data = json['data']
    return data
#缴费账单
def port_bills():
    #登陆
    login = "https://dev4.ccbscf.com/uaa/app/login"
    #缴费账单
    product = 'https://dev4.ccbscf.com/mobile/app/biz/common/bills?page=1&pageSize=20&billType=&isPaid='
    values = {}
    values['name'] = name
    values['password'] = password
    values['appId'] = '865296036668109F0%3AC8%3A50%3AAF%3AD9%3A3B'
    values['appType'] = 'android'
    values['mobile'] = phone
    ret = requests.post(url=login, data=values, verify=False)
    data = ret.json()
    #token值
    accesstoken = data['data']['accessToken']
    refreshtoken = data['data']['refreshToken']
    header = {}
    header['User-Agent'] = 'okhttp/3.3.0'
    header['page'] = '1'
    header['pageSize'] = '15'
    header['refreshToken'] = refreshtoken
    ret = requests.get(url=product, headers=header, verify=False)
    json = ret.json()
    data = json['data']
    return data