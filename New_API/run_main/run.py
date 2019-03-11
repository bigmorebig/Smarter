import sys
from manage_data.exract_excel import ExtractExcel
from manage_data.Run_Request import Run_Request
from util.operation_excel import OperationExcel
from util.operation_database import OperationDatabase
from util.operation_config import OperationConfig
from util.operation_json import OperationJson
from util.common import Common
import zipfile
from manage_data.depend_data import DependData
import json
sys.path.append('')


class Run:
    def __init__(self):
        self.data = ExtractExcel()
        self.request = Run_Request()
        self.oper_excel = OperationExcel()
        self.oper_config = OperationConfig()
        self.oper_json = OperationJson()
        self.comm = Common()
        host = self.oper_config.get_database('host')
        port = self.oper_config.get_database('port')
        user = self.oper_config.get_database('user')
        password = self.oper_config.get_database('password')
        db = self.oper_config.get_database('db')
        self.oper_db = OperationDatabase(host,port,user,password,db)

    def run_main(self):
        nrows = self.oper_excel.get_nrows()
        request_data_addr = self.oper_config.get_jsonfile_addr('Addr')
        with open(request_data_addr,'r',encoding='utf-8') as f:
            mudle = json.load(f)
        for i in range(1,nrows):
            is_run = self.data.is_run(i)
            if is_run == True:
                url = self.data.get_url(i)
                method = self.data.get_method(i)
                cookie = self.data.get_Cookie(i)
                keyword = self.data.get_request_data(i)
                if self.data.get_depend_db(i) == True:
                    title,sql = self.data.get_sql_for_json(i)
                    key = self.data.get_sql(i)
                    value = self.oper_db.get_db_data(sql)
                    self.oper_json.write_data(key,title,value)
                    data = self.data.get_data_for_json(i)
                    data_form = self.data.get_post_form(i)
                else:
                    data = self.data.get_data_for_json(i)
                    data_form = self.data.get_post_form(i)
                if self.data.get_depend_id(i):
                    depend = DependData(self.data.get_depend_id(i))
                    depend_res = depend.depend_res(i)
                    if depend_res != False:
                        depend_request = self.data.get_depend_request(i)
                        data[depend_request] = depend_res
                    else:
                        self.data.write_result(i, '该条用例被跳过')
                        print('第%d条测试用例被跳过，未执行' % i)
                        continue
                r = self.request.write_res(mudle,keyword,url,method,data,cookie,data_form)
                #断言
                if self.comm.compar_str(self.data.get_expect(i), str(r)):
                    self.data.write_result(i, 'pass')
                    print('第%d条测试用例成功' % i)
                else:
                    self.data.write_result(i, str(r))
                    print('第%d条测试用例失败' % i)
        # azip = zipfile.ZipFile('测试数据.zip', 'w')
        # for current_path, subfolders, filesname in os.walk(r'E:\脚本\接口测试脚本\New_API\storage_data'):
        #     for file in filesname:
        #         filename = os.path.join(current_path, file)
        #         azip.write(filename)
        # azip.close()


if __name__ == '__main__':
    Run().run_main()
