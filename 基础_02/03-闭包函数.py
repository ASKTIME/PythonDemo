# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 15:22
# @Author  : sunzhen
# @File    : 03-闭包函数.py
# @Software: PyCharm

# 1.大前提
# 闭包函数 = 名称空间与作用域+函数嵌套+函数对象
# 核心点：名字的查找关系是以函数定义阶段为准的

# 2.什么是闭包函数
# 闭 指函数定义在一个函数内的函数(内嵌函数)
# 包 指函数对包含在外层的函数的作用域的名字的引用
#       (不包含全局作用域)

# 闭包函数之名称空间的与作用域的应用 + 函数嵌套
# def f1():
#     x = 1
#     def f2():
#         print(x)
#     f2()
# x = 222
# def bar():
#     x = 3344
#     f1()
#
# bar()


# 闭包函数 ：函数对象(以定义阶段为主)
# def f1():
#     x = 1
#     def f2():
#         print('f2的输出',x)
#     f2()
#
#     return f2  # 返回f2的内存地址
#
# f = f1()
#
# x = 444
# f()


# 3.定义闭包函数

# 4.为何要有闭包函数(闭包函数的应用)
# 两种函数传参方式

# 方式一: 直接把函数体需要的参数定义形参
# def f1(x):
#     print(x)
# f1(1)

# 方式二:
# def f1():
#     x = 3
#
#     def f2():
#         print(x)
#
#     # f2(x)
#     return f2
#
#
# # f2()
#
# f = f1()
# f()

def outer(n):
	num = n
	
	def inner():
		return num + 1
	
	return inner


print(outer(3)())  # 4
print(outer(5)())  # 6
