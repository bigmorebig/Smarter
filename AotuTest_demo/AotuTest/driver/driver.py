from selenium import webdriver

def browser():
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    # browser = webdriver.Edge()
    browser.get('http://www.baidu.com')
    browser.current_url()

if __name__ == '__main__':
    browser()