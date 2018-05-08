#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-07 09:28:29
# @Author  : money (money89757757@163.com@)


import os

# 斐波那契数列
# 两个元素的总和确定了下一个数

a,b = 0,1

while b < 10:
	print(b)
	a,b = b, a+b
'''
while b < 1000:
	print(b, end = ',')
	a,b = b,a+b
end关键字可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
'''