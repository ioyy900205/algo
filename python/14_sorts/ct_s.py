'''
Date: 2021-08-13 14:41:44
LastEditors: Liuliang
LastEditTime: 2021-08-13 15:06:30
Description: 
'''
from itertools import count
import itertools
from typing import List
a3 = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7, 2, 0, 2, 0 ]

def ct_s(nums:List):
    if len(nums)<=1: return
    
    counts = [0] * (max(nums)+1)
    counts_new = [0] * (max(nums)+1)
    print (f"counts:{counts}")
    for num in nums:
        counts[num] += 1
    print(f"counts:{counts}")
    
    for i in range(len(counts)):
            counts_new[i] = sum(counts[:i+1])
    counts = list(itertools.accumulate(counts))
    print(f"counts:    {counts}")
    print(f"counts_new:{counts_new}")

    sorted_nums = [0] * len(nums)
    print(f"nums:       {nums}")
    print(f"sorted_nums:{sorted_nums}")

    for num in reversed(nums):        
        index = counts_new[num] - 1
        sorted_nums[index] = num
        counts_new[num] -= 1
        # print(f"sorted_nums:{sorted_nums}")
        # print(f"counts_new:{counts_new}")
    nums[:] = sorted_nums

ct_s(a3)
print(f"a3:{a3}")
