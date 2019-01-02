class Common():
    def compar_str(self,str_one,str_two):
        '''判断一个字符串是否包含另一个字符串
        多次断言用逗号分隔
        str_one：被包含字符串
        str_two：包含字符串
        '''
        if isinstance(str_one,str):
            splite_str_one = str_one.split(',')
            for i in splite_str_one:
                if i in str_two:
                    return True
                else:return False
        else:return False
if __name__ == '__main__':
    print(Common().compar_str('aa','aaa'))