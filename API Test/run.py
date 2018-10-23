import unittest
from HTMLTestRunner import HTMLTestRunner
import time

test_dir = "./"
discover = unittest.defaultTestLoader.discover(test_dir,"unittest_case.py")

if __name__ == '__main__':
    report_dir = './report'
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + 'test_report.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f,title='API TEST REPORT',description='FIRST API TEST')
        runner.run(discover)
    f.close()