#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-08 13:43:24
# @Author  : money (money89757757@163.com@)

import os


#No.1 break
for letter in 'hTTP':
	if letter == 'T':
		break;
	print("当前字母为：",letter)

var = 10
while var > 0:
	print('当前变量值为：',var)
	var = var - 1
	if var == 5:
		break

print('end')


#No.2 continue
for letter in 'Google':
	if letter == 'l':
		continue
	print('当前字母：',letter)

var = 10
while var > 0:
	var = var - 1
	if var == 5:
		continue
	print('当前变量值：',var)
print('end')


#No.3 if/else 中的break

for n in range(2,10):
	for x in range(2,n):
		if n % x == 0:
			print(n,'等于',x,'*',n//x)
			break

		else:

			print(n,'是质数')

#No.4 pass语句
	#pass是空语句,是为了保持程序结构的完整性。
	#pass不做任何事情,一般用做占位语句

for letter in 'Google':
	if letter == 'g':
		pass
		print('执行pass块')

	print('当前字母：',letter)

print("end")