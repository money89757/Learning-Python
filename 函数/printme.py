#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-18 10:00:40
# @Author  : money (money89757757@163.com@)


import os
'''
No.1 函数调用
def printme(str):
	"打印任何传入的字符串"
	print(str)
	return


printme("调用函数")
printme("再次调用")

'''
'''
No.2
在python中，string,tuples,numbers是不可更改的对象，
而list,dict等则是可以修改的对象
	· 不可变类型：变量赋值a=5再赋值a=10,这里实际是新生产一个int值对象10，再
	  让a指向它，而5被丢弃，不是a的值,相当于新生成了a

	· 可变类型：变量赋值la = [1,2,3,4]后再赋la[2] = 5则是将list la的第三个元素值更改，
	  本身la并没有动,只是其内部的一部分值被改变

python 函数的参数传递：
	· 不可变类型：类似C++的值传递,如整数、字符串、元祖。如fun(a),传递的只是
	  a的值，没有影响a对象本身。比如fun(a)内部修改了a的值，只是修改另一个复制的对象吗

    · 可变类型：类似C++的引用传递，如 列表、字典。如fun(la),则是将真正的传过去
      修改后fun外部的la也会受影响

python 中一切都是对象,严格不能说值传递还是引用传递，我们应该说传
不可变对象和传可变对象
'''
'''
No3.传不可变对象
def ChangeInt(a):
	a = 10

b = 2

ChangeInt(b)
print(b)
'''

def changeme(mylist):
	"修改参数列表"
	mylist.append([1,2,3,4])
	print("函数内取值：",mylist)
	return


mylist = [10,20,30]
changeme(mylist)
print("函数外取值：",mylist)
