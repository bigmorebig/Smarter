import pymysql

class OperationDatabase():
    def __init__(self,host,port,user,password,db):
        self.conn = pymysql.connect(host = host,port = int(port),user = user,password = password,db = db,cursorclass = pymysql.cursors.DictCursor)

    def get_db_data(self,sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
        self.conn.close()
        return list(result.values())[0]

if __name__ == '__main__':
    host = 'localhost'
    port = '3306'
    user = 'root'
    password = '123456'
    db = 'bank'
    sql = 'select * from account where open_date="2000-01-15"'
    value = OperationDatabase(host,port,user,password,db).get_db_data(sql)
    print(value)