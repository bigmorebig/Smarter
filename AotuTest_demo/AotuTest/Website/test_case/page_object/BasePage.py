from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page():
    def __init__(self,browser):
        self.browser = browser
        self.base_url = 'http://test-1.yushuoyun.com'
        self.wait = WebDriverWait(self.browser,10)

    def _open(self,url):
        self.url = url
        url_ = self.base_url + self.url
        self.browser.maximize_window()
        self.browser.get(url_)
        assert self.browser.current_url == url_,'Did not land on %s' % url_

    def open(self):
        self._open(self.url)

    #等待是否可定位
    def find_pre_loc_element(self,*loc):
        return self.wait.until(EC.presence_of_element_located((loc)))

    #等待是否可点击
    def find_element_click(self,*loc):
        return self.wait.until(EC.element_to_be_clickable((loc)))

    #等待是否包含预期的字符串
    def find_text_pre_element(self,*loc,text):
        return self.wait.until(EC.text_to_be_present_in_element(loc,text))