from pymysql import connect
import yaml

class DB():
    def __init__(self):
        '''连接数据库'''
        print('connect database!')
        self.conn = connect(host = '127.0.0.1',user = 'root',password = '123456',db = 'django_restful')

    def clear(self,table_name):
        '''清除表中数据'''
        print('clear db...')
        clear_sql = 'truncate' + table_name + ';'
        with self.conn.cursor() as cursor:
            #清除外键约束
            cursor.execute('set foreign_key_checks = 0;')
            cursor.execute(clear_sql)
        self.conn.commit()

    def insert(self,table_name,table_data):
        '''插入数据'''
        print('insert data...')

        #遍历数据
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())

        print(key)
        print(value)
        insert_sql = 'insert into ' + table_name + '(' + key + ')' + 'values' + '(' + value + ')'
        print(insert_sql)

        with self.conn.cursor() as cursor:
            cursor.execute(insert_sql)
        self.conn.commit()

    def close(self):
        '''关闭数据库连接'''
        print('close database...')
        self.conn.close()

    # def init_data(self,datas):
    #     '''初始化数据'''
    #     print('init database...')
    #     for table,data in datas.items():
    #         self.clear(table)
    #         for d in data:
    #             self.insert(table,d)
    #     self.close()

if __name__ == '__main__':
    db = DB()
    #调试各个方法
    db.clear('api_user')
    db.clear('api_group')
    user_data = {'id':1,'username':'test1','email':'tangxiao@downjoy.com'}
    db.insert('api_user',user_data)
    group_data = {'id':1,'name':'first group'}
    db.insert('api_group',group_data)
    db.close()

    # #初始化数据
    # f = open('data.yaml','r')
    # datas = yaml.load(f)
    # db.init_data(datas)