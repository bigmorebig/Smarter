import sys
sys.path.append('/Users/tangxiao/文件/practice/New_API')
import requests
from util.operation_json import OperationJson
import json
from util.operation_config import OperationConfig

class Run_Request():
    def __init__(self):
        self.s = requests.Session()
        self.base_url = OperationConfig().get_base_url('base_url')
        self.request_res_addr = OperationConfig().get_request_res_Addr('Addr')
        self.request_data_addr = OperationConfig().get_jsonfile_addr('Addr')

    def get_request(self,url,data = None,cookie = None,auth = None):
        if data == None:
            r = self.s.get(self.base_url+url,cookies = cookie,auth = auth)
        else:
            r = self.s.get(self.base_url+url,params=data,cookies = cookie,auth = auth)
        return r.json()

    def post_request(self,url,data,cookie = None,data_form = None,auth = None):
        if data_form == True:
            r = self.s.post(self.base_url + url, data=json.dumps(data), cookies=cookie,auth = auth)
        else:
            r = self.s.post(self.base_url+url,data = data,cookies = cookie,auth = auth)
        return r.json()

    def run_method(self,url,method,data = None,cookie = None,data_form = None,auth = None):
        res = None
        if method.lower() == 'get':
            res = self.get_request(url,data,cookie,auth)
        elif method.lower() == 'post':
            res = self.post_request(url,data,cookie,data_form,auth)
        return res

    def write_res(self,mudle,key,url,method,data = None,cookie = None,data_form = None):
        res = self.run_method(url,method,data,cookie,data_form)
        with open(self.request_res_addr,'w',encoding='utf-8') as f:
            # print(mudle[key])
            mudle[key] = res
            json.dump(mudle,f)
        return res

if __name__ == '__main__':
    url = '/sso/login/normal'
    data = OperationJson().read_data('login')
    print(data)
    cookie = {'fs_login_auth': 'f43748815c884efcbbdc2fc7f2741c12'}
    run = Run_Request()
    print(run.run_method('/cultural-cloud/user/clouds','get',cookie))