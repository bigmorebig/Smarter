import unittest
from driver import *
from selenium.webdriver.support.ui import WebDriverWait

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.browser = browser()
        self.wait =  WebDriverWait(self.browser, 10)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()