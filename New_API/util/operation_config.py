import configparser

class OperationConfig():
    def __init__(self):
        self.path = r'E:\脚本\接口测试脚本\New_API\New_API\storage_data\config.ini'
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path,encoding='utf-8')

    def get_global_var(self,name):
        return int(self.cf.get('Global_Var',name))

    def get_jsonfile_addr(self,name):
        return self.cf.get('JsonFile_Addr',name)

    def get_casefile_addr(self,name):
        return self.cf.get('CaseFile_Addr', name)

    def get_base_url(self,name):
        return self.cf.get('BaseUrl',name)

    def get_database(self,name):
        return self.cf.get('DATABASE',name)

    def get_db_json(self,name):
        return self.cf.get('DB_JSON',name)

    def get_request_res_Addr(self,name):
        return self.cf.get('Request_res_Addr',name)

    def get_email(self,name):
        return self.cf.get('Email',name)

if __name__ == '__main__':
    print(OperationConfig().get_email('host'))