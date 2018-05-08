#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-07 09:35:09
# @Author  : money (money89757757@163.com@)


import os
'''
var = 100
if var:
	print("ture")
	print(var)

var2 = 0
if var2:
	print("var2 ture")
	print(var2)

print("滚")
'''

num = int(input("input number"))
if num%2==0:
	if num%3==0:
		print("输入的数字可以整除2和3")
	else:
		print("输入的数字不能被2和3整除")

else:
	if num%3==0:
		print("你输入的数字可以整除3,但不能整除2")
	else:
		print("你输入的数字不能整除2和3")