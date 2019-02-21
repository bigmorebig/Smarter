from selenium import webdriver

def browser():
    # browser = webdriver.Firefox()
    # return webdriver.Chrome()
    # browser = webdriver.Edge()
    return webdriver.PhantomJS()


if __name__ == '__main__':
    browser()