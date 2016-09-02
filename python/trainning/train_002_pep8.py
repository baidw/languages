#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'baidw'

'''
Python编程规范
1.编码
    所有的 Python 脚本文件都应在文件头标上：
    # -*- coding:utf-8 -*-
    用于设置编辑器,保存格式
2.注释
    业界普遍认同 Python 的注释分为两种：
    1.1.由 # 开头的“真正的”注释；
    1.2.docstrings，例如，用于表明如何使用这个包、模块、类、函数（方法），甚至包括使用示例和单元测试
    坚持适当注释原则。
    对不存在技术难点的代码坚持不注释，对存在技术难点的代码必须注释
3.缩进
    Python依赖缩进来确定代码块的层次，行首空白符主要有两种：tab 和 空格，但严禁两者混用。
    如果使用tab缩进，设定tab为4个空格
    python缩进推荐使用空格
4.空格
    空格在Python代码中是有意义的，因为Python的语法依赖于缩进，在行首的空格称为前导空格
    只讨论非前导空格。非前导空格在Python代码中没有意义，但适当地加入非前导空格可以增进代码的可读性
    1）在二元算术、逻辑运算符前后加空格，如：a = b + c;
    2）在一元前缀运算符后不加空格，如：if !flg: pass;
    3）“:”用在行尾时前后皆不加空格，如分枝、循环、函数和类定义语言；用在非行尾时两端加空格
    如：dict 对象的定义：d = {'key' :  'value'}
    4）括号（含圆括号、方括号和花括号）前后不加空格，如：do_something(arg1, arg2)
    5）不要在逗号、分号、冒号前面加空格，但应该在它们后面加（除了在行尾）
    6） 不要用空格来垂直对齐多行间的标记，因为这会成为维护的负担（适用于:，#，=等）
5.空行
    适当的空行有利于增加代码的可读性，加空行可以参考如下几个准则：
    1） 在类、函数的定义间加空行；
    2） 在 import 不同种类的模块间加空行；
    3） 在函数中的逻辑段落间加空行，即把相关的代码紧凑写在一起，作为一个逻辑段落，段落间以空行分隔；
6.断行
    尽管现在的宽屏显示器已经可以单屏显示超过 256 列字符，
    但本规范仍然坚持行的最大长度不得超过 80 个字符的标准
    1) 为长变量名换一个短名
    2) Python会将圆括号、中括号和花括号中的行隐式的连接起来，你可以利用这个特点
    3) 在长行加入续行符强行断行，断行的位置应在操作符前，且换行后多一个缩进，
    以使维护人员看代码的时候看到代码行首即可判定这里存在换行
7.字符串
    1.避免在循环中用+和+=操作符来累加字符串
    2.为多行字符串使用三重双引号而非三重单引号，不过要注意, 通常用隐式行连接更清晰，
    因为多行字符串与程序其他部分的缩进方式不一致
8.命名
    8.1常量
        常量名所有字母大写，由下划线连接各个单词，如：THIS_IS_A_CONSTANT = 1
    8.2变量
        变量名全部小写，由下划线连接各个单词，如：this_is_a_variable = 1
        私有类成员使用单一下划线前缀标识，多定义公开成员，少定义私有成员
        变量名不应带有类型信息，因为Python是动态类型语言，如iValue、names_list、dict_obj等是不好的命名
    8.3函数
        函数名的命名规则与变量名相同
    8.4类
        对类名使用大写字母开头的单词（如CapWords, 即Pascal风格），不使用下划线连接单词
    8.5模块
        模块名全部小写，对于包内使用的模块，可以加一个下划线前缀
    8.6包
        包的命名规范与模块相同
    8.7缩写
        命名应当尽量使用全拼写的单词，缩写的情况有如下两种
        1）常用的缩写，如 XML、ID等，在命名时也应只大写首字母。如：class XmlParser(object):pass
        2）命名中含有长单词，对某个单词进行缩写
        这时应使用约定成俗的缩写方式，如去除元音、包含辅音的首字符等方式
        如：function 缩写为 fn，text 缩写为 txt，object 缩写为 obj，count 缩写为 cnt，等。
    8.8特定命名方式
        主要是指 __xxx__ 形式的系统保留字命名法。项目中也可以使用这种命名，
        它的意义在于这种形式的变量是只读的，这种形式的类成员函数尽量不要重载
    8.9导入格式
        1.import 的次序，先 import Python 内置模块，再 import 第三方模块，
        最后 import 自己开发的项目中的其它模块；这几种模块用空行分隔开来
        2.每个import应该独占一行
        3.不要使用 from module import *，除非是import常量定义模块或其它你确保不会出现命名空间冲突的模块
9.赋值
    对于赋值语言，主要是不要做无谓的对齐
10.语句
    通常每个语句应该独占一行。不过， 如果测试结果与测试语句在一行放得下， 你也可以将它们放在同一行
    如果是if语句， 只有在没有else时才能这样做
    特别地，绝不要对 try/except 这样做，因为try和except不能放在同一行。
11.
'''

import os

class ThisIsAClass(object):
    """docstring for ThisIsAClass"""
    def __init__(self, arg):
        self.__arg__=arg

def this_is_function():
    """ docstring for this_is_function"""
    return 5
    
if __name__ == '__main__':
    THIS_IS_CONSTANT=1  #这是常量定义
    this_is_variable=1  #这是变量定义
    fn=this_is_function()   #这是函数定义
