'''
Date: 2021-08-13 11:38:47
LastEditors: Liuliang
LastEditTime: 2021-08-13 12:31:48
Description: 
'''
from typing import List
import random

def _partition(nums:List, left, right):
    tmp = nums[left]
    while left < right:
        while left < right and nums[right] >= tmp:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= tmp:
            left += 1
        nums[right] = nums[left]
    nums[left] = tmp
    return left


def _qk_s(nums, left, right, k=1):
    
    if left<right:

        mid = _partition(nums,left,right)
        if mid + 1 == k:
            return nums[k]
        elif mid + 1 < k:
            return _qk_s(nums,mid+1,right,k)
        else:
            return _qk_s(nums,left,mid-1,k)


def qk(nums):
    _qk_s(nums,0,len(nums)-1)



a1 = [3, 5, 6, 7, 8]
a2 = [2, 2, 2, 2]
a3 = [4, 3, 2, 1]
a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]

print(_qk_s(a4,0,8,5))
print(a4)