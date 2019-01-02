import sys
sys.path.append('/Users/tangxiao/文件/practice/New_API')
from util.operation_config import OperationConfig
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson

class ExtractExcel():
    def __init__(self):
        self.oper_config = OperationConfig()
        self.oper_excel = OperationExcel()
        self.oper_json = OperationJson()

    #是否执行
    def is_run(self,row):
        col = self.oper_config.get_global_var('run')
        is_run = self.oper_excel.get_cell_value(row,col)
        if is_run.lower() != 'yes':
            return None
        return True

    #获取请求方法
    def get_method(self,row):
        col = self.oper_config.get_global_var('method')
        method = self.oper_excel.get_cell_value(row,col)
        return method

    #获取caseID
    def get_case_id(self,row):
        col = self.oper_config.get_global_var('caseid')
        case_id = self.oper_excel.get_cell_value(row,col)
        return case_id

    #获取请求模块
    def get_module(self,row):
        col = self.oper_config.get_global_var('module')
        module = self.oper_excel.get_cell_value(row,col)
        return module

    #获取用例名称
    def get_case_name(self,row):
        col = self.oper_config.get_global_var('case_name')
        case_name = self.oper_excel.get_cell_value(row,col)
        return case_name

    #获取post执行是否为json格式
    def get_post_form(self,row):
        col = self.oper_config.get_global_var('post_form')
        post_form = self.oper_excel.get_cell_value(row,col)
        if post_form.lower() == 'yes':
            return True
        else:return False

    #获取url
    def get_url(self,row):
        col = self.oper_config.get_global_var('url')
        url = self.oper_excel.get_cell_value(row,col)
        return url

    #获取请求
    def get_request_data(self,row):
        col = self.oper_config.get_global_var('request_data')
        request_data = self.oper_excel.get_cell_value(row,col)
        return request_data

    #获取excel中的请求数据
    def get_data_for_json(self,row):
        keyword = self.get_request_data(row)
        data_for_json = self.oper_json.read_data(keyword)
        if data_for_json:
            return data_for_json
        else:return False

    #获取Cookie
    def get_Cookie(self,row):
        col = self.oper_config.get_global_var('Cookie')
        Cookie = self.oper_excel.get_cell_value(row,col)
        if Cookie:
            return Cookie
        else:return False

    #获取依赖caseID
    def get_depend_id(self,row):
        col = self.oper_config.get_global_var('depend_id')
        depend_id = self.oper_excel.get_cell_value(row,col)
        if depend_id:
            return depend_id
        else:return False

    #获取依赖接口上条接口的返回数据
    def get_depend_data(self,row):
        col = self.oper_config.get_global_var('depend_data')
        depend_data = self.oper_excel.get_cell_value(row,col)
        return depend_data

    #获取依赖接口的请求数据
    def get_depend_request(self,row):
        col = self.oper_config.get_global_var('depend_request')
        depend_request = self.oper_excel.get_cell_value(row,col)
        return depend_request

    #获取是否依赖数据库
    def get_depend_db(self,row):
        col = self.oper_config.get_global_var('depend_db')
        depend_db = self.oper_excel.get_cell_value(row,col)
        if depend_db.lower() == 'yes':
            return True
        elif depend_db.lower() == 'no':
            return False

    #获取是否依赖的sql语句
    def get_sql(self,row):
        col = self.oper_config.get_global_var('sql')
        sql = self.oper_excel.get_cell_value(row,col)
        return sql

    #获取json中的sql请求数据
    def get_sql_for_json(self,row):
        keyword = self.get_sql(row)
        title,data_for_json = self.oper_json.read_db_data(keyword)
        return title,data_for_json

    #获取期望值
    def get_expect(self,row):
        col = self.oper_config.get_global_var('expect')
        expect = self.oper_excel.get_cell_value(row,col)
        return expect

    #获取实际结果
    def get_reality(self,row):
        col = self.oper_config.get_global_var('reality')
        reality = self.oper_excel.get_cell_value(row,col)
        return reality

    #将实际结果写入excel表中
    def write_result(self,row,value):
        col = self.oper_config.get_global_var('reality')
        self.oper_excel.write_cell_value(row,col,value)

if __name__ == '__main__':
    oper = ExtractExcel()
    print(oper.get_data_for_json(1))