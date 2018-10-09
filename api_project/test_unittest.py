import requests
import unittest
from read_api import API
from mysql_action import DB
from read_excel import ReadExcel

class TestApi(unittest.TestCase):
    def setUp(self):
        self.base_url = ''
        self.auth = ''
        self.db = DB()
        self.api = API()
        self.excel = ReadExcel

    def run_test(self):
        s = requests.Session()
        for nrows in range(1,self.excel.read_nrow()):
            if self.api.get_method() == 'GET':
                r = s.get(self.base_url + self.api.get_url(),params = self.api.get_param(),auth = self.auth)
                resulte = r.json()
                self.assertEquals(resulte['status_code'],200)
