import xlrd,os

class ReadExcel():
    def __init__(self):
        self.dir_excel = os.path.join(os.getcwd(), 'text.xlsx')

    def read_book(self):
        readbook = xlrd.open_workbook(self.dir_excel)
        return readbook

    def read_sheet(self,page):
        sheet = self.read_book().sheet_by_index(page)
        return sheet

    def read_nrow(self):
        nrow = self.read_sheet(0).nrows
        return nrow

    def read_ncols(self):
        ncols = self.read_sheet(0).ncols
        return ncols

    def read_data(self,n,l):
        data = self.read_sheet(0).cell_value(n,l)
        return data
