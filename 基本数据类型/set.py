#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-06 15:32:53
# @Author  : money (money89757757@163.com)

import os

#集合（set）是一个无序不重复元素的序列。

#基本功能是进行成员关系测试和删除重复元素。

#可以使用大括号 { } 或者 set() 函数创建集合，
#注意：创建一个空集合必须用 set() 而不是 { }，因为 { } #是用来创建一个空字典。

student = {'Tom','jim','mary','tom','jim'}

print(student)

#成员测试

if('Rose'in student) :
	print('Rose 在集合中')

else :
	print('Rose 不在在集合中')

#set可以进行集合运算
a=set("abcdefg")
b=set("alacazam")

print(a)

print(a - b)  #a和b的差集

print(a | b)  #a和b

print(a & b)

print(a ^ b) 