from pymysql import connect
from ReadExcel import Readexcel
import logging.config
import pymysql.cursors

excel = Readexcel()
class mysql():
    def __init__(self):
        # print('connect database...')
        self.conn = connect(host='rdsbuezp0btf932d168jo.mysql.rds.aliyuncs.com',port=3306,user='fsadmin',password='ChUvuxebrumatRA4UtRA',db='db_content',cursorclass=pymysql.cursors.DictCursor)

    def get_new_data(self):
        try:
            result = []
            for i in range(0,excel.get_nrows()-1):
                if excel.db_select()[i] == 'H':
                    sql = excel.get_db()[i]
                    with self.conn.cursor() as cursor:
                        cursor.execute(sql)
                        result.append(cursor.fetchall())
                        # print('查询到的数据库值为:\n%s' % result)

                # elif excel.db_select()[i] != 'H':
                #     print('%s组数据不需要查询数据库' % excel.get_casenum()[i])
                #     result.append( '%s组数据不需要查询数据库' % excel.get_casenum()[i])
            self.conn.commit()
            self.conn.close()
            return result
        except pymysql.err.InternalError as error:
            # logging.info('%s' % error)
            return ('%s' % error)
        except pymysql.err.ProgrammingError as error:
            # logging.info('%s' % error)
            return ('%s' % error)

def excute_db():
    data = mysql().get_new_data()
    new_list = []
    for l in range(len(data)):
        if type(data[l]) == list:
            for a in range(len(data[l])):
                new_list.append(data[l][a])
    return new_list

if __name__ == '__main__':
    # db = mysql()
    r = mysql().get_new_data()
    print(r)
    # print(type(r[2]))