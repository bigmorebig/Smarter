import unittest
from model import function,myunit
from page_object import BasePage,login
from time import sleep
from AotuTest.driver import driver


class LoginTest(myunit.StartEnd):
    def test_login_nomal(self):
        print('test_login_nomal test starts..')
        browser = driver.browser()
        nomal_login = login.LoginPage(browser)
        nomal_login.test_login('test_ff7',123456)
        self.assertEqual(nomal_login.assert_login(),'http://test-1.yushuoyun.com/login/success')
        function.insert_img(browser,'test_login_nomal.png')

    def test_login_no_passwd(self):
        print('test_login_no_passwd test starts..')
        browser = driver.browser()
        nomal_login = login.LoginPage(browser)
        nomal_login.test_login('test_ff7','')
        self.assertEqual(nomal_login.assert_no_passwd_msg(), '请输入密码')
        function.insert_img(browser, 'test_login_no_passwd.png')

    def test_login_no_account(self):
        print('test_login_no_account test starts..')
        browser = driver.browser()
        nomal_login = login.LoginPage(browser)
        nomal_login.test_login('','12345')
        self.assertEqual(nomal_login.assert_no_account_msg(), '请输入用户名')
        function.insert_img(browser, 'test_login_no_account.png')

    def test_login_no_account_passwd(self):
        print('test_login_no_account_passwd test starts..')
        browser = driver.browser()
        nomal_login = login.LoginPage(browser)
        nomal_login.test_login('','')
        self.assertEqual(nomal_login.assert_no_account_msg(), '请输入用户名')
        self.assertEqual(nomal_login.assert_no_passwd_msg(), '请输入密码')
        function.insert_img(browser, 'test_login_no_account_passwd.png')

    def test_login_wrong_passwd(self):
        print('test_login_wrong_passwd test starts..')
        browser = driver.browser()
        nomal_login = login.LoginPage(browser)
        nomal_login.test_login('test_ff7','')
        # self.assertEqual(nomal_login.assert_wrong_msg(), '请输入密码')
        function.insert_img(browser, 'test_login_wrong_passwd.png')

if __name__ == '__main__':
    LoginTest()

