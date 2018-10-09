from pymysql import connect
from read_excel import ReadExcel

class DB():
    def __init__(self):
        print('connect database...')
        self.conn = connect(host = '',user = '',password = '',db = '')

    def execute_db(self):
        l = 0
        while ReadExcel.read_data(0,l) == 'sql' and l < ReadExcel.read_ncols():
            for nrows in range(0,ReadExcel.read_nrow()):
                sql = ReadExcel.read_data(nrows,l)
                if sql == None:
                    with self.conn.cursor() as cursor:
                        cursor.execute(sql)
                else:
                    pass
            l += 1
        self.conn.commit()

    def get_all(self):
        value = self.conn.cursor().fetchall()
        return value

    def get_one(self):
        value = self.conn.cursor().fetchone()
        return value

    def close_db(self):
        self.conn.close()
        print('close database!')