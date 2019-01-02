import json
from util.operation_config import OperationConfig

class OperationJson():
    def __init__(self):
        self.request_path = OperationConfig().get_jsonfile_addr('Addr')
        self.db_path = OperationConfig().get_db_json('Addr')

    #读取请求json文件中的data
    def read_data(self,keyword):
        with open(self.request_path,'r',encoding='utf-8') as f:
            data = json.load(f)
            return data[keyword]

    #将数据库中查询的结果写入请求json文件中
    def write_data(self,read_title,keyword_title,keyword):
        with open(self.request_path,'r',encoding='utf-8') as f:
            datas = json.load(f)
        datas[read_title][keyword_title] = keyword
        with open(self.request_path,'w',encoding='utf-8') as fp:
            json.dump(datas,fp)

    #读取数据库json文件中的数据，返回数据库的title和数据库语句
    def read_db_data(self,keyword):
        with open(self.db_path,'r',encoding='utf-8') as f:
            data = json.load(f)
            return list(data[keyword].keys())[0],list(data[keyword].values())[0]

if __name__ == '__main__':
    print(OperationJson().write_data('login','account','111'))