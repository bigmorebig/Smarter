import xlrd,os
import requests,json
import unittest

dir_book = os.path.join(os.getcwd(),'test.xlsx')
readbook = xlrd.open_workbook(dir_book)
sheet = readbook.sheet_by_index(0)
nrows = sheet.nrows
list_url = []
list_param = []
while nrows >= 2:
    n = 2
    for n in range(1,nrows):
        url = sheet.cell_value(n,2)
        param = sheet.cell_value(n,1)
        nrows = nrows - 1
        list_param.append(param)
        list_url.append(url)
        r = requests.get(list_url[n-2],data = list_param[n-2])
        print(r.text)
        assert r.status_code == 200 ,'出错啦'