import xlrd
import os
import logging.config
import re

class Readexcel():
    def __init__(self):
        test_dir = os.path.join(os.getcwd(),'test.xlsx')
        if not os.path.exists(test_dir):
            print('测试数据不存在')
        self.test_book = xlrd.open_workbook(test_dir)
        self.sheet = self.test_book.sheet_by_index(0)
        self.nrows = self.sheet.nrows
        self.ncols = self.sheet.ncols

    def get_nrows(self):
        nrows = self.nrows
        return nrows

    def get_ncols(self):
        ncols = self.ncols
        return ncols

    def get_casenum(self):
        casenum = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'Case_Num':
                for i in range(1,self.nrows):
                    if re.match('case_\d+', self.sheet.cell_value(i,l)):
                        casenum.append(self.sheet.cell_value(i,l))
                    else:
                        return 'casenum中存在名称错误，请检查！'
        if casenum != []:
            return casenum
        else:
            print('列表中未填写用例序号')

    def get_System_mod(self):
        mod = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'System_mod':
                for i in range(1,self.nrows):
                    if re.match(r'[\u4E00-\u9FA5]', self.sheet.cell_value(i,l)):
                        mod.append(self.sheet.cell_value(i,l))
                    else:
                        return 'Mod中存在名称错误，请检查！'
        if mod != []:
            return mod
        else:
            print('列表中未填写模块名称')

    def get_Api_Name(self):
        name = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'Api_Name':
                for i in range(1,self.nrows):
                    if re.match(r'[\u4E00-\u9FA5]', self.sheet.cell_value(i,l)):
                        name.append(self.sheet.cell_value(i,l))
                    else:
                        return 'name中存在名称错误，请检查！'
        if name != []:
            return name
        else:
            print('列表中未填写API名称')

    def get_url(self):
        url = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'Api_Url':
                for i in range(1,self.nrows):
                    if re.match('[a-zA-Z\/]+', self.sheet.cell_value(i, l)):
                        url.append(self.sheet.cell_value(i, l))
                    else:
                        return 'url中存在名称错误，请检查！'
        if url != []:
            return url
        else:
            print('列表中未填写url')

    def get_method(self):
        method = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'Method':
                for i in range(1,self.nrows):
                    if self.sheet.cell_value(i,l) == 'GET' or self.sheet.cell_value(i,l) =='POST' or self.sheet.cell_value(i,l) =='DELETE' or self.sheet.cell_value(i,l) =='PUT':
                        method.append(self.sheet.cell_value(i, l))
                    else:
                        return 'method中存在名称错误，请检查！'
        if method != []:
            return method
        else:
            print('列表中未填写请求方法')

    def get_param(self):
        param = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'Parameters':
                for i in range(1,self.nrows):
                    param.append(self.sheet.cell_value(i,l))
        if param != []:
            return param
        else:
            print('列表中未填写参数')

    def get_expect(self):
        expect = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'Expect':
                for i in range(1,self.nrows):
                    expect.append(self.sheet.cell_value(i,l))
        if expect != []:
            return expect
        else:
            print('列表中无期望值')

    def get_db(self):
        db = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'Sql':
                for i in range(1,self.nrows):
                    db.append(self.sheet.cell_value(i,l))
        if db != []:
            return db
        else:
            print('列表中无数据库值')

    def db_select(self):
        select = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'DB':
                for i in range(1,self.nrows):
                    if re.match('\s+', self.sheet.cell_value(i, l)) or self.sheet.cell_value(i, l) == 'H'or self.sheet.cell_value(i, l) == '':
                        select.append(self.sheet.cell_value(i, l))
                    else:
                        return 'select中存在名称错误，请检查！'
        if select != []:
            return select
        else:
            return '列表中无数据库判断'

    def get_json(self):
        updata_json = []
        for l in range(0,self.ncols):
            if self.sheet.cell_value(0,l) == 'Json':
                for i in range(1,self.nrows):
                    updata_json.append(self.sheet.cell_value(i,l))
        if updata_json != []:
            return updata_json
        else:
            print('列表中未填写参数')

if __name__ == '__main__':
    s = Readexcel()
    print(s.get_param())