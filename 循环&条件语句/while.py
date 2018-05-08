#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-07 09:45:43
# @Author  : money (money89757757@163.com@)


import os
'''
#NO.1
n = 100
sum = 0
counter = 1

while counter <= n:
	sum = sum + counter
	counter += 1

print("1 到 %d 之间和为：%d" %(n,sum))
'''

'''
#NO.2无限循环
var = 1
while var == 1:
	num = int(input("输入一个数字："))
	print("输入的数字为：", num)

print("bye!")

可以用CTRL + C来退出当前的无限循环
'''

'''
#NO.3ewhile 循环使用else语句
count = 0
while count < 5:
	print(count,"小于5")
	count = count + 1
else:
	print(count,"大于或等于5")
'''

#NO.4 flag
flag = 0
while(flag):
	print(1)
print("out")