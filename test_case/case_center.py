# coding:utf-8
from appium import webdriver
import unittest, time, re, datetime
import Base
from selenium.webdriver.support.ui import WebDriverWait
class center(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n我的页面测试开始')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=Base.setting())
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_companyname').click()
        # self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_companyname').clear()
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_companyname').send_keys('盛世集团成员二')
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_phonenumber').click()
        # self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_phonenumber').clear()
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_phonenumber').send_keys('18910248213')
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_password').click()
        # self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_password').clear()
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/edit_password').send_keys('a1111111')
        time.sleep(1)
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/button_login').click()
        WebDriverWait(cls.driver, 10, 2).until(
            lambda driver: cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center'))
        #进入我的TAB
        cls.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center').click()
        time.sleep(1)
        contexts = cls.driver.contexts
        for cotext in contexts:
            print(u'获取视图:', cotext)
        # self.verificationErrors=[]#错误信息会被打印在这个列表中

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        print('\n我的页面测试结束')
        # self.assertEqual([],self.verificationErrors)

    def test_center0(self):
        '''我的角色检查'''
        #头像控件
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_user_avatar')
        #角色名称
        self.assertEqual('测试企业一零主管',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_user_name').text)
        #企业名展示
        self.assertEqual('测试企业一零',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_company_name').text)
        #认证状态
        self.assertEqual('已认证',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_auth_status').text)
        #用户岗位查询
        self.assertEqual('主管岗',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_user_role').text)
    def test_center1(self):
        '''我的管理项检查'''
        #用户管理
        self.assertEqual(self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_user_manage').text,'用户管理')
        #账号管理
        self.assertEqual('账号管理',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_account_manage').text)
        #密码设置
        self.assertEqual('密码设置',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_password_setting').text)
        #平台介绍
        self.assertEqual('平台介绍',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_platform_introduction').text)
        #邀请企业加入
        self.assertEqual('邀请企业加入',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_invite_to_join').text)
        #平台版本
        self.assertEqual('1.0.0',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_version_code').text)
        #联系客服
        self.assertEqual('联系客服',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_contact_customer_service').text)
        #我的标签为选中，其他两个为未选中
        self.assertEqual('false',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_person_center').get_attribute('enabled'))
        self.assertEqual('true',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_home').get_attribute('enabled'))
        self.assertEqual('true',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_message').get_attribute('enabled'))
    def test_center2(self):
        '''个人信息页元素检查'''
        #进入个人信息管理页面
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_user_name').click()
        time.sleep(3)
        a=self.driver.find_elements_by_class_name('android.widget.TextView')
        for i in a:
            print (i.text)
        #返回按钮
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back')
        #个人信息页标题
        self.assertEqual('个人信息',
                         self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rl_title_bar').find_elements_by_class_name('android.widget.TextView')[1].text)
        #头像部分,头像元素
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_user_avatar')
        #用户姓名
        self.assertEqual('测试企业一零主管',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_nickname').text)
        #证件
        self.assertEqual('外国护照',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_id_type_name').text)
        #证件号码
        self.assertEqual('6523215',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_id_code').text)
        #手机号
        self.assertEqual('18910248213',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_phone').text)
        #企业职务
        self.assertEqual('灭霸',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_duty').text)
        #退出登陆按钮
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_logout')
        #返回
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back').click()
    def test_center3(self):
        '''更改头像'''
        #进入个人页
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_user_avatar').click()
        time.sleep(2)
        #进入个人信息页
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/iv_user_avatar').click()
        #拍照按钮
        self.assertEqual('拍照',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_take_photo').text)
        #从相册中选取
        self.assertEqual('从相册中选取',self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_from_gallery').text)
        #取消按钮
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_cancel').click()
        #返回到个人信息管理
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_go_back').click()
    def test_center4(self):
        '''企业职务修改'''







    def test_center9(self):
        '''退出登陆'''
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_user_name').click()
        time.sleep(3)
        #退出登陆按钮
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_logout')


    def test_homepaper3(self):
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_user_manage').click() # 用户管理
        time.sleep(3)
        self.driver.press_keycode(4)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_account_manage').click()  # 账号管理
        time.sleep(1)
        self.driver.press_keycode(4)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_password_setting').click()  # 密码设置
        time.sleep(1)
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_platform_introduction').click()  # 平台介绍
        time.sleep(1)
        self.driver.press_keycode(4)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/rl_platform_version').click()  # 平台版本
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_contact_customer_service').click()#联系客服
        self.driver.press_keycode(4)
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/tv_invite_to_join').click()  # 邀请企业加入
        self.driver.press_keycode(4)
        self.driver.press_keycode(4)
    def test_homepaper4(self):
        self.test_homepape0()
        pass
    def test_homepaper5(self):
        self.driver.find_element_by_android_uiautomator('text(\"剩余可用额度\")').click()  # 剩余可用额度
        time.sleep(1)
        self.driver.press_keycode(4)

    def test_homepaper6(self):
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.ImageView[2]').click()

    def test_homepaper7(self):
        '''我的'''
        self.driver.find_element_by_id('com.ccbscf.mobile.corp:id/fl_person_center').click()


if __name__ == "__main__":
    unittest.main()