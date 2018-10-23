# from random import randint,sample
# #先生成随机的字典s1,s2,s3，
# #sample从给定的字符串中选取后面给定的数个，组成列表
# #sample("ABCFD",3)
# #['A','C']
# s1 = {k:randint(3,6) for k in sample("ABCDEF",randint(1,5))}
# s2 = {k:randint(3,6) for k in sample("ABCDEF",randint(1,5))}
# s3 = {k:randint(3,6) for k in sample("ABCDEF",randint(1,5))}
# print(s1)
# print(s2)
# print(s3)
# print([s1,s2,s3])
# #方法一：
# print("-------------------方法一-----------------")
#
# coment = []
# for i in s1:
#     if i in s2 and i in s3:
#         coment.append(i)
# print(coment)
# print("-------------------方法二-----------------")
# #方法二: 将字典转化为集合（python2 dict.viewkeys(),3中 dict.key()），然后取并集
# k1 = s1.keys()
# k2 = s2.keys()
# k3 = s3.keys()
# coment = k1&k2&k3
# print(coment)
# print("-------------------方法三-----------------")
# #当N个时
# from functools import reduce
# # x = map(lambda s:s.keys(),[s1,s2,s3])
# #reduce 用法，必须接受俩参数进行操作，之后将前面两个参数和从后面的列表中一个一个取出进行之前相同的操作
# coment = reduce(lambda x, y : x & y, map(dict.keys,[s1,s2,s3]))
# print(coment)