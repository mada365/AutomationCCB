import requests
import json
import re

login = "https://dev4.ccbscf.com/uaa/app/login"
# 缴费账单
product = 'https://dev4.ccbscf.com/mobile/app/biz/common/bills?page=1&pageSize=20&billType=&isPaid='
values = {}
values['name'] = '马到成功'
values['password'] = "a1111111"
values['appId'] = '865296036668109F0%3AC8%3A50%3AAF%3AD9%3A3B'
values['appType'] = 'android'
values['mobile'] = "18910248213"
ret = requests.post(url=login, data=values, verify=False)
data = ret.json()
# token值
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
print  (data)

