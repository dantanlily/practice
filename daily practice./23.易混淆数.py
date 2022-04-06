#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:32:48 2022

@author: dantan
"""
# 给定一个数字 N，当它满足以下条件的时候返回 true：

# 原数字旋转 180° 以后可以得到新的数字。

# 如 0, 1, 6, 8, 9 旋转 180° 以后，得到了新的数字 0, 1, 9, 8, 6 。

# 2, 3, 4, 5, 7 旋转 180° 后，得到的不是数字。

# 易混淆数 (confusing number) 在旋转180°以后，可以得到和原来不同的数，且新数字的每一位都是有效的。

#  

# 示例 1：



# 输入：6
# 输出：true
# 解释： 
# 把 6 旋转 180° 以后得到 9，9 是有效数字且 9!=6 。
# 示例 2：



# 输入：89
# 输出：true
# 解释: 
# 把 89 旋转 180° 以后得到 68，86 是有效数字且 86!=89 。
# 示例 3：



# 输入：11
# 输出：false
# 解释：
# 把 11 旋转 180° 以后得到 11，11 是有效数字但是值保持不变，所以 11 不是易混淆数字。 
# 示例 4：



# 输入：25
# 输出：false
# 解释：
# 把 25 旋转 180° 以后得到的不是数字。


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/confusing-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def func(n):
    dic={"0":"0","1":"1","6":"9","8":"8","9":"6"}
    listNum=list(str(n))
    l=[]
    for i in listNum:
        if i not in dic:
            return False
        l.insert(0,dic[i])
    return l!=listNum

print(func(8910))

list(str(89)) # ['8', '9']