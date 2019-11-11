#!/usr/bin/env
# -*- coding: UTF-8 -*-

# 导入模块
import hello_package
# 导入package
import package_runoob.b
from package_runoob.a import runoob1,runoob11

# __init__.py空文件作用
from package_runoob import a
from package_runoob import b

# # 导入TensorFlow和tf.keras
# import tensorflow as tf
# from tensorflow import keras
# print tf.__version__

# 现在可以调用模块里包含的函数了
hello_package.print_func("Runoob")
package_runoob.b.runoob2()
runoob1()
runoob11()

a.runoob1()
b.printme()
print(123) # Python 2.6与Python 2.7部分地支持python3形式的print语法