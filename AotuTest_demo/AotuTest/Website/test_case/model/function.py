from selenium import webdriver
import os

def insert_img(driver,filename):
    path = os.path.dirname(__file__)
    base_path = os.path.dirname(path)
    base_path = base_path.replace('\\','/')
    base = os.path.dirname(base_path)
    img_path = ''.join([base,'/test_report/screen_shot/'+filename])
    print(img_path)
    driver.get_screenshot_as_file(img_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    insert_img(driver,'baidu.png')