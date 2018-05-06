#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-06 15:56:29
# @Author  : money (money89757757@163.com)


import os

dict = {}
dict['one'] = "frist"
dict['two'] = "second"

tinydict = {'name': 'bob','wm':"m",'age':1}

print(dict['one'])       # 输出键为'one'的值
print(dict['two'])       # 输出键为'two'的值
print(tinydict)          #输出完整的字典
print(tinydict.keys())   #输出所用的键
print(tinydict.values()) #输出所有的值



#字典（dictionary）是Python中另一个非常有用的内置数据类型。

#列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

#字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

#键(key)必须使用不可变类型。

#在同一个字典中，键(key)必须是唯一的。

print(======)


#字典类型也有一些内置的函数，例如clear()、keys()、values()等。

#注意：

#1、字典是一种映射类型，它的元素是键值对。
#2、字典的关键字必须为不可变类型，且不能重复。
#3、创建空字典使用 { }。