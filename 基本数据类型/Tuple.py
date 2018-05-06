#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-06 15:19:05
# @Author  : money (money89757757@163.com)


import os

tuple = ('abcd',789,2.23,'runoob',70.2)
tinytuple = (123,'runoob')

print (tuple)              #输出完整元组
print (tuple[0])           #输出元组的第一个元素
print (tuple[1:3])         #数据出从第二个元素开始到第三个元素
print (tuple[2:])          #数据出从第二个元素开始元素
print (tinytuple * 2)      #输出两次元组
print (tuple + tinytuple)  #连接元组

#虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。

# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含0或1个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接。