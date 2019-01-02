import sys
sys.path.append('/Users/tangxiao/文件/practice/New_API')
from util.operation_excel import OperationExcel
from manage_data.exract_excel import ExtractExcel
from manage_data.Run_Request import Run_Request
from jsonpath_rw import jsonpath,parse
from util.operation_config import OperationConfig
import json

class DependData():
    def __init__(self,case_id):
        self.oper_excel = OperationExcel()
        self.case_id = case_id
        self.data = ExtractExcel()
        self.run = Run_Request()
        self.oper_conf = OperationConfig()

    #获取上条接口的返回请求数据
    def depend_response(self):
        row = self.oper_excel.get_row_depend_caseid(self.case_id)
        keyword = self.data.get_request_data(row)
        request_data_addr = self.oper_conf.get_request_res_Addr('Addr')
        with open(request_data_addr, 'r', encoding='utf-8') as f:
            mudle = json.load(f)
        return mudle[keyword]

    #获取依赖的请求结果
    def depend_res(self,row):
        depend_data = self.data.get_depend_data(row)
        depend_response = self.depend_response()
        json_exe = parse(depend_data)
        madle = json_exe.find(depend_response)
        if madle:
            return [math.value for math in madle][0]
        else:
            return False

if __name__ == '__main__':
    # data ={'code': 200, 'result': [{'id': '54020b1c87a046ad94893b4b61e797ad', 'name': '文化云04'}, {'id': '80c0f83f55e445fbb1d6ae1c9c0b27a1', 'name': '文化云07'},], 'success': True}
    # depend = 'result[0].id'
    # json_exe = parse(depend)
    # madle = json_exe.find(data)
    # print([math.value for math in madle][0])
    print(DependData('002').depend_res(3))