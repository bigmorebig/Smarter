import unittest
from ReadExcel import Readexcel
import requests
import warnings
import logging.config
from extract_data import extract,get_params
import json

CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()
class testcase(unittest.TestCase):
    def setUp(self):
        print('===========================测试开始!=====================================')
        warnings.filterwarnings("ignore")
        self.excel = Readexcel()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
        self.base_url = 'http://restapi-test1.fishsaying.com'
        self.data = extract().deal_list()

    def test(self):
        params = get_params()
        url = self.excel.get_url()
        method = self.excel.get_method()
        nrows = self.excel.get_nrows()
        name = self.excel.get_Api_Name()
        s = requests.Session()
        for i in range(1, nrows):
            if method[i-1] == 'GET':
                if params[i-1] == '':
                    r = s.get(self.base_url + url[i - 1],headers = self.headers)
                    result = r.json()
                else:
                    r = s.get(self.base_url + url[i - 1], params=eval(params[i - 1]),headers = self.headers)
                    result = r.json()
                try:
                    self.assertEqual(result['code'], 200)
                    print(name[i-1])
                    print(result['result'][0]['id'])
                except AssertionError as error:
                    print('%s断言失败!\t msg:%s' % (name[i-1],error))
                except Exception as e:
                    print(e)
            elif method[i - 1] == 'POST':
                if self.excel.get_json()[i-1] == 'H':
                    r = s.post(self.base_url + url[i - 1], data=json.dumps(eval(params[i - 1])),headers = self.headers)
                    result = r.json()
                else:
                    r = s.post(self.base_url + url[i - 1], data=eval(params[i - 1]), headers=self.headers)
                    result = r.json()
                try:
                    self.assertEqual(result['code'], 200)
                    print(name[i-1])
                except AssertionError as error:
                    print('%s断言失败!\t msg:%s' % (name[i-1],error))
            else:
                print('%s请求方式错误，请重新检查!' % name[i-1])

    def tearDown(self):
        print('===========================测试完成!=====================================')

if __name__ == '__main__':
    unittest.main()