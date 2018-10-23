from mysql_action import excute_db
from ReadExcel import Readexcel
from functools import reduce

class extract():
    def __init__(self):
        self.r = excute_db()
        self.length = len(self.r)
        self.excel = Readexcel()

    def deal_list(self):
        data = []
        key = []
        value = []
        for p in range(len(self.excel.get_param())):
            param = eval(self.excel.get_param()[p])
            if self.excel.db_select()[p] == 'H':
                for key_p,value_p in param.items():
                    key.append(key_p)
                    if param[key_p] == '$':
                        for i in range(0, self.length):
                            sql = self.r[i]
                            for key_r, value_r in sql.items():
                                value.append(value_r)
                    else:
                        pass

            elif self.excel.db_select()[p] == '':
                pass
            else:
                data.append('%s输入类型错误，请重新检查！' % self.excel.get_casenum()[p])
        for i in range(len(key)):
                data.append('{"' + key[i] + '":"' + str(value[i]) + '"}')
        # print(data[0])
        return data

#提取数据库查询的数据
def get_params():
    info = []
    a = 0
    excel = Readexcel()
    data = extract().deal_list()
    for i in range(len(excel.get_param())):
        if excel.db_select()[i] == 'H':
            if a <= len(data):
                info.append(data[a])
                a = a + 1
        else:
            info.append(excel.get_param()[i])
    return info

#需要跑多条数据库查询的数据
def multi_data():
    orig_data = []
    for i in range(len(get_params())):
        orig_data.append(eval(get_params()[i]))
    print(orig_data)
    coment = reduce(lambda x, y : x & y, map(dict.keys,orig_data))      #字典中的公共key
    print(coment)

#获取需要从上一条接口返回值获取数据的key值
def get_key():
    excel = Readexcel()
    for i in range(len(excel.get_param())):
        data = eval(excel.get_param()[i])
        for key,value in data.items():
            if data[key] == '#':
                a = data.keys()
                return a
            else:
                pass

#获取需要从上一条接口返回值获取数据的value
def get_dict():
    excel = Readexcel()
    a = []
    for i in range(len(excel.get_param())):
        data = eval(excel.get_param()[i])
        for key, value in data.items():
            if data[key] == '#':
                a.append('{"'+key+'":"'+str(value)+'"}')
                return a
            else:
                pass

def get_spc_param():
    spe_param = []

if __name__ == '__main__':
   r = get_params()
   print(r)