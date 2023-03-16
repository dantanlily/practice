#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:29 2023

@author: dantan
"""

# =====字符串转义
# print 'what is wrong'  # 如何输入what's wrong
# print 'what\'s wrong\t'  # 使用\对特殊字符进行转义。转义也可以用于表达不可见字符，例如tab符号：\t。
# print '\\'  # 如果要表达\本身，也需要转义，写为\。
# print r'what\'s wrong'  # 在字符串的开始加r（Raw String），使得字符串中不发生转义。

# =====unicode字符串
# print '中国', type('中国')
# print u'中国', type(u'中国')
# print '中国' == u'中国'

# =====字符串常见操作：字符串相加，相乘
# stock_code1 = 'sh600000'
# stock_code2 = 'sh600001'
# print stock_code1 + ', ' + stock_code2  # 字符串可以直接相加
# print stock_code1 * 3  # 字符串可以乘以整数
# print '*' * 30


# =====字符串常见操作：startswith、endswith、
# stock_code = 'sh600000'
# print stock_code.startswith('sh')  # 判断字符串是否是以'sh'开头
# print stock_code.startswith('s')
# print stock_code.startswith('sz')


# =====字符串常见操作：判断
# stock_code = 'sh600000'
# print 'sh' in stock_code  # 判断字符串中是否包含'sh'
# print 'sz' in stock_code


# =====字符串常见操作：替换
# stock_code = 'sh600000'
# print stock_code.replace('sh', 'sz')  # 将字符串中的'sh'替换成'sz'
# print 'sh600000来自sh'.replace('sh', 'sz')  # 会替换所有的sh


# stock_code = 'sh600000, sh600001, sh600002, sh600003'
# print(stock_code.split(', '))

# 逆操作
# stock_code_list = ['sh600000', 'sh600001', 'sh600002', 'sh600003']
# print (', '.join(stock_code_list))

# =====字符串常见操作：strip
# stock_code = '  sh600000  '
# print stock_code
# print stock_code.strip()  # 去除两边的空格

# =====异常处理
# 语法
"""
try:
    执行相关语句1
except:
    执行相关语句2
else:
    执行相关语句3
"""

# 说明
"""
1. 先尝试执行相关语句1
2. 若在执行语句1的过程中报错，那么执行相关语句2
3. 若在执行语句1的过程中没有报错，那么执行相关语句3
"""


# =====异常处理的一个例子
import time  # 导入系统库time，可以使用一些系统级别的函数


def buy_one_stock(stock_name='sh600000'):  # 参数为股票名
    """
    此程序用于下单买入某个股票，但是买入过程中，程序有50%的概率报错。
    """
    import random
    random = random.random()
    if random >= 0.5:
        return
    else:
        raise ValueError('程序报错！')
# buy_one_stock()

max_try_num = 5
tyr_num = 0
while True:
    try:  # 尝试做以下事情
        buy_one_stock()
    except:  # 如果因为各种原因报错
        print '警告！下单出错，停止1秒再尝试'
        tyr_num += 1
        time.sleep(1)
        if tyr_num > max_try_num:
            print '超过最大尝试次数，下单失败'
            # 此处需要执行相关程序，通知某些人
            break
    else:  # 如果没有报错
        print '下单成功了'
        break
    
# In[]