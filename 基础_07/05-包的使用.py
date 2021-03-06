# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 9:34
# @Author  : sunzhen
# @File    : 05-包的使用.py
# @Software: PyCharm

"""
1.包是一个包含__init__.py文件的文件夹
2.为何要有包
    init 存在的价值,在导文件的时候有一个文件可以代替运行
    包的本质是模块中的一种形式,包是被用来当作模块导入


"""
import mmm
# 导入mmm发生三件事
# 1.产生一个模块的名称空间
# 2.运行模块文件(__init__.py文件)将运行过程中产生的名字都丢到模块的名称空间中
# 3.在当前名称空间拿到一个名字,该名字与模块名称空间的某一个内存地址相同
# from mmm import x

mmm.f1()
mmm.f2()


# 强调：
# 1.关于包相关的导入语句分为import和from...import...
# 导入时必须遵循的一个原则：
# 凡是在导入的时候带点的，在点的左边必须是一个包，否则非法
# 可以有一连串的点，如import 顶级包.子包.子模块
# 例如：
# from a.b.c.d.e.f import xxxxx
# import a.b.c.d.e.f
# 其中 a.b.c.d.e 都必须是包

# 2.包A和包B下有相同的名字也不会冲突(命名空间不一样)
# 3.import导入文件是，产生的名称空间的名字来源于文件，import包的话，名称空间来源于__init__











