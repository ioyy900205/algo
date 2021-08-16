'''
Date: 2021-08-14 14:28:12
LastEditors: Liuliang
LastEditTime: 2021-08-14 14:45:38
Description: 
'''
import random

def random_level():
    p = 0.5
    level = 1
    create = random.random()
    while create < p and level < 8:
        level += 1
    return level

def _random_level(p: float = 0.5) -> int:
    level = 1
    while random.random() < p and level < 16:
        level += 1
    return level

c = random_level()

print(c)