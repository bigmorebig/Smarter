from read_excel import ReadExcel

class API():
    def get_case_num(self):
        l = 0
        case_num = []
        while ReadExcel.read_data(0, l) == 'CASE_NUM' and l < ReadExcel.read_ncols():
            for nrows in range(0, ReadExcel.read_nrow()):
               data = ReadExcel.read_data(nrows,l)
               case_num.append(data)
        return case_num

    def get_mod(self):
        l = 0
        mod = []
        while ReadExcel.read_data(0, l) == 'System_mod' and l < ReadExcel.read_ncols():
            for nrows in range(0, ReadExcel.read_nrow()):
                data = ReadExcel.read_data(nrows, l)
                mod.append(data)
        return mod

    def get_name(self):
        l = 0
        name = []
        while ReadExcel.read_data(0, l) == 'Api_Name' and l < ReadExcel.read_ncols():
            for nrows in range(0, ReadExcel.read_nrow()):
                data = ReadExcel.read_data(nrows, l)
                name.append(data)
        return name

    def get_api_num(self):
        l = 0
        api_num = []
        while ReadExcel.read_data(0, l) == 'Api_Num' and l < ReadExcel.read_ncols():
            for nrows in range(0, ReadExcel.read_nrow()):
               data = ReadExcel.read_data(nrows,l)
               api_num.append(data)
        return api_num

    def get_support(self):
        l = 0
        support = []
        while ReadExcel.read_data(0, l) == 'Test_purpose' and l < ReadExcel.read_ncols():
            for nrows in range(0, ReadExcel.read_nrow()):
               data = ReadExcel.read_data(nrows,l)
               support.append(data)
        return support
    def get_url(self):
        l = 0
        url = []
        while ReadExcel.read_data(0, l) == 'Api_Url' and l < ReadExcel.read_ncols():
            for nrows in range(0, ReadExcel.read_nrow()):
               data = ReadExcel.read_data(nrows,l)
               url.append(data)
        return url

    def get_method(self):
        l = 0
        method = []
        while ReadExcel.read_data(0, l) == 'Method' and l < ReadExcel.read_ncols():
            for nrows in range(0, ReadExcel.read_nrow()):
               data = ReadExcel.read_data(nrows,l)
               method.append(data)
        return method

    def get_param(self):
        l = 0
        param = []
        while ReadExcel.read_data(0, l) == 'Parameters' and l < ReadExcel.read_ncols():
            for nrows in range(0, ReadExcel.read_nrow()):
               data = ReadExcel.read_data(nrows,l)
               param.append(data)
        return param