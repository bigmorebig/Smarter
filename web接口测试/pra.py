import requests
import json

s = requests.Session()
base_url = 'http://restapi-test1.fishsaying.com'
header = {'X-DevTools-Emulate-Network-Conditions-Client-Id':'48CB8CE5A3F23E99B637AACE37339C35',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
          'Accept-Language':'zh-CN,zh;q=0.9',
          'Accept-Encoding':'gzip, deflate'}
param_data = {'account':'test_ff7','password':'123456','isRemember':'true','service':'100','client':'201'}
r = s.post(base_url + '/sso/login/normal',data = param_data,headers = header,timeout = 1)
print(r.text)
print(r.cookies.values())