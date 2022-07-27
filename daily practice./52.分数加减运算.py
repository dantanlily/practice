#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:55:43 2022

@author: dantan
"""

# 592. 分数加减运算
# 给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 

# 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。

 

# 示例 1:

# 输入: expression = "-1/2+1/2"
# 输出: "0/1"
#  示例 2:

# 输入: expression = "-1/2+1/2+1/3"
# 输出: "1/3"
# 示例 3:

# 输入: expression = "1/3-1/2"
# 输出: "-1/6"
 

# 提示:

# 输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。 
# 输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
# 输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
# 输入的分数个数范围是 [1,10]。
# 最终结果的分子与分母保证是 32 位整数范围内的有效整数。

import math

expression = "-1/2+1/2+1/3"
expression = "-5/2+10/3+7/9"


class Solution:
    def fractionAddition(self, expression: str) -> str:
        # x1/y1 + x2/y2= (x1*y2 + x2*y1)/(y1*y2)  x1 nominator;y1 denominator; x2 nominator1;y2 denominator1
        nominator,denominator=0,1
        i,n=0,len(expression)
        while i<n:
            sign,nominator1,denominator1=1,0,0
            if expression[i]=='-' or expression[i]=='+':
                if expression[i]=='-':
                    sign=-1
                i+=1
            while i<n and expression[i].isdigit():
                nominator1=int(expression[i])+nominator1*10
                i+=1
            nominator1=sign*nominator1
            i+=1

            while i<n and expression[i].isdigit():
                denominator1=int(expression[i])+denominator1 * 10
                i+=1
            
            nominator=nominator*denominator1 + denominator * nominator1
            denominator*=denominator1
            # sign is with nominator, make sure it's positive
        g=math.gcd(abs(nominator),denominator)
        return f"{nominator//g}/{denominator//g}"





# 12//4 = 3
# 12/4 = 3.0


#number=expression.split('+')

denominator, numerator = 0, 1  # 分子，分母
i, n = 0, len(expression)
while i < n:
    # 读取分子
    denominator1, sign = 0, 1
    if expression[i] == '-' or expression[i] == '+':
        if expression[i] == '-':
            sign = -1
        i += 1 # move to next number 
    while i < n and expression[i].isdigit():
        denominator1 = denominator1 *10 + int(expression[i])
        i += 1  # move to next
    denominator1 = sign * denominator1
    i += 1 #  #move to next drop '/'

    # 读取分母 考虑两位数的可能 读取到直到下一个符号
    # 输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
#输入的分数个数范围是 [1,10]。
    numerator1 = 0
    while i < n and expression[i].isdigit():
        numerator1 = numerator1 * 10+ int(expression[i])
        i += 1
    print(sign,denominator1,numerator1)
    
    denominator = denominator * numerator1 + denominator1 * numerator
    numerator *= numerator1
    print(denominator,numerator)

g = math.gcd(abs(denominator), numerator)

print(f"{denominator//g}/{numerator//g}")

 
# 12//4 = 3
# 12/4 = 3.0



