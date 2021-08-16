'''
Date: 2021-08-13 10:22:16
LastEditors: Liuliang
LastEditTime: 2021-08-13 10:24:12
Description: 
'''
import random
dic = {}
list = [random.randint(0,10) for i in range(10)]
for i in range(len(list)):
    dic[list[i]] += 1
print (dic)