'''
Author: HaoTian Qi
Date: 2022-03-15 16:01:36
Description: 
LastEditors: HaoTian Qi
LastEditTime: 2022-03-15 16:01:36
'''
import requests

print(requests.get('http://127.0.0.1:12380/my-key').text)
