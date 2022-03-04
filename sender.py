'''
Author: HaoTian Qi
Date: 2022-02-21 17:34:53
Description: 
LastEditors: HaoTian Qi
LastEditTime: 2022-02-21 17:36:09
'''
import requests


for i in range(50):
    requests.put('http://127.0.0.1:12380/my-key',data=f'value {i}')