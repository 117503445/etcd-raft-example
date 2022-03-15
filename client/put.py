'''
Author: HaoTian Qi
Date: 2022-02-21 17:34:53
Description: 
LastEditors: HaoTian Qi
LastEditTime: 2022-03-15 16:03:38
'''
import requests
from datetime import datetime



for i in range(1):
    requests.put('http://127.0.0.1:12380/my-key',data=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
