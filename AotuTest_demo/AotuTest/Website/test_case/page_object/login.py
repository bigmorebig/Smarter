from BasePage import *
from selenium import webdriver

class LoginPage(Page):
    url = '/login'
    username_loc = (By.ID,'userName')
    password_loc = (By.ID,'password')
    submit_loc = (By.CSS_SELECTOR,'#root > div > div.cacloud-loginNew-content > div.cacloud-loginNew-right > div > div.ant-tabs.ant-tabs-top.ant-tabs-line > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > form > div:nth-child(3) > div > div > span > div.loginNew-btn-box > button')

    def type_username(self,username):
        self.find_pre_loc_element(*self.username_loc).clear()
        self.find_pre_loc_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_pre_loc_element(*self.password_loc).clear()
        self.find_pre_loc_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element_click(*self.submit_loc).click()

    def test_login(self,username,password):
        try:
            self.open()
            self.type_username(username)
            self.type_password(password)
            self.type_submit()
        except Exception as e:
            print('error:',e)

if __name__ == '__main__':
    browser = webdriver.Chrome()
    login = LoginPage(browser)
    login.test_login('test_ff7',123456)