import BSTestRunner
import time
import unittest

from manage_data.Run_Request import Run_Request
from mock_test import mock_test


class TestUnittest(unittest.TestCase):
    def test_001(self):
        url = ''
        data = {'account': 'test_ff7', 'password': 123456}
        res = mock_test(data,url,'post',data)
        print(res)
        self.assertEquals(res['password'],123456,'测试失败')

    def test_002(self):
        url = ''
        data = {'account': 'test_ff7', 'password': 123456}
        run = Run_Request()
        res = run.run_method(url,'post',data)
        self.assertEquals(res['code'],200,'测试失败')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestUnittest('test_001'))
    suite.addTest(TestUnittest('test_002'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/result.html'
    with open(filename,'wb') as fp:
        runner = BSTestRunner.BSTestRunner(stream=fp,title='TEST REPORT',description='用例执行情况')
        runner.run(suite)
