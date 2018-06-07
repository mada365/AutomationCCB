
def login():
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'GWY0217413001449'  # adb devices查到的设备名
        # desired_caps['app'] = '/Users/mada/Downloads/cbchot_v1.82_xiaomi_506.apk'  # 被测试应用在电脑上的位置
        desired_caps['appPackage'] = 'com.ccbscf.mobile.corp'
        desired_caps['appActivity'] = 'com.ccbscf.mobile.corp.ui.activity.MainActivity'
        desired_caps['autoLaunch'] = 'true'  # 是否需要启动或安装app默认为true
        desired_caps['noReset'] = 'false'  # 会话前是否重置app状态，true为不需要,默认false
        desired_caps['newCommandTimeout'] = 20  # 设置未接收到新命令的超时时间，默认60s

