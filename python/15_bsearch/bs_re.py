'''
Date: 2021-08-14 09:42:37
LastEditors: Liuliang
LastEditTime: 2021-08-14 10:33:15
Description: 
'''
def _bs(nums, target, low ,high):
    
    if low > high:
        return 
    mid = low + (high - low) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return _bs(nums, target, low, mid)
    elif nums[mid] < target:
        return _bs(nums,target, mid+1 , high)
        

list = [1,2,3,5,5,5,6,7]

print(_bs(list,4,0,7))
