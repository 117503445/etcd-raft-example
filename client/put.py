'''
Author: HaoTian Qi
Date: 2022-02-21 17:34:53
Description: 
LastEditors: HaoTian Qi
LastEditTime: 2022-03-28 18:49:41
'''
import requests
from datetime import datetime


a = 0


def req(n):
    global a
    for _ in range(n):
        a += 1
        print(a)
        requests.put(f'http://127.0.0.1:12380/my-key', data=f'{a}')


req(16)

# 4 add config entry
# 16 normal entry


input()
req(15)
