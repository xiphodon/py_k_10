#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/30 13:35
# @Author  : GuoChang
# @Site    : 
# @File    : py_k_10.py
# @Software: PyCharm
import requests


def get(url,params):
    r = requests.get(url=url, params=params)
    print("get:" + r.text + "\n")


def post(url,params):
    r = requests.post(url=url, data=params)
    print("post:" + r.text + "\n")


if __name__ == "__main__":
    url = "http://u.ikuaichuan.com:8080/olms/api/account/login"
    params = {"name": "admin", "password": "11111111"}
    get(url,params)
    post(url,params)
