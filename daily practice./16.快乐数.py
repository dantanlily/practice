#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:27:55 2022

@author: dantan
"""
# 编写一个算法来判断一个数 n 是不是快乐数。

# 「快乐数」 定义为：

# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

#  

# 示例 1：

# 输入：n = 19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/happy-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def func(n):
    tmp=[n] #数组存放已经拆解过的数字
    while n!=1:
        l=list((str(n)))
        # list=[]
        # for item in strN: # list=[item for item in strN]
        # list.append(item)
        res=0
        for c in l:
            res+=int(c)*int(c)
        if res in tmp:
            return False
        tmp.append(res)
        n=res
    return True

print(func(91))
            