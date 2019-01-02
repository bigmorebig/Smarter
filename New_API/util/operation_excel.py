import sys
sys.path.append('/Users/tangxiao/文件/practice/New_API')
import xlrd
from util.operation_config import OperationConfig
from xlutils.copy import copy


class OperationExcel():
    def __init__(self,page = None):
        self.filepath = OperationConfig().get_casefile_addr('Addr')
        self.page = page
        if page == None:
            self.page = 0
        self.data = self.get_sheets()

    def get_sheets(self):
        filename = xlrd.open_workbook(self.filepath)
        return filename.sheets()[self.page]

    #获取行数
    def get_nrows(self):
        return self.data.nrows

    #获取单元格值
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    #修改单元格值
    def write_cell_value(self,row,col,value):
        rb = xlrd.open_workbook(self.filepath)
        wb = copy(rb)
        ws = wb.get_sheet(0)
        ws.write(row,col,value)
        wb.save(self.filepath)

    #获取一行的数据
    def get_row_data(self,row):
        row_data = self.data.row_values(row)
        return row_data

    #获取一列的数据，默认为第一列的数据
    def get_col_data(self,col = None):
        if col != None:
            cols_data = self.data.col_values(col)
        else:
            cols_data = self.data.col_values(0)
        return cols_data

    #通过caseID获取一行数据
    def depend_data(self,case_id):
        cols_data = self.get_col_data()
        for num,col_data in enumerate(cols_data):
            if col_data == case_id:
                return self.get_row_data(num)
            num +=1

    #根据case_id获取case_id行号
    def get_row_depend_caseid(self,case_id):
        cols_data = self.get_col_data()
        for num,col_data in enumerate(cols_data):
            if col_data == case_id:
                return num
            num +=1

    # #根据依赖的caseid获取caseid的行号
    def get_depend_caseid_for_row(self,case_id):
        row = self.get_row_depend_caseid(case_id)


if __name__ == '__main__':
    print(OperationExcel().get_row_depend_caseid('002'))