'''
Date: 2021-08-14 10:34:24
LastEditors: Liuliang
LastEditTime: 2021-08-14 11:55:32
Description: 
'''
# 原始版本
def _bs(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 左边第一个
def _bs(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            if mid == 0 or nums[mid-1] != target: 
                return mid
            else: 
                high = mid - 1
    return -1


# 右边最后一个
def _bs(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid+1] != target: 
                return mid
            else: 
                low = mid + 1
    return -1

# 第一个大于等于给定元素
def _bs(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            if mid == 0 or nums[mid-1] < target:
                return mid
            else:
                high = mid - 1


    return -1
# 查找最后⼀个⼩于等于给定值的元素
def _bs(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        else:
            if mid == len(nums) - 1 or nums[mid + 1] > target:
                return mid 
            else:
                low = mid + 1

    
list = [1,2,3,5,5,5,6,7]

print(_bs(list,5))