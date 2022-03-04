'''
Author: HaoTian Qi
Date: 2022-02-21 17:34:53
Description: 
LastEditors: HaoTian Qi
LastEditTime: 2022-03-04 11:25:05
'''
import requests


# for i in range(1):
#     requests.put('http://127.0.0.1:12380/my-key',data=f'value {i}')

print(requests.get('http://127.0.0.1:12380/my-key').text)