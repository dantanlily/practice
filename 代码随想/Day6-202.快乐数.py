#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:05:48 2023

@author: dantan
"""

'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

示例 1：

输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
示例 2：

输入：n = 2
输出：false
'''

# 题目中说了会 无限循环，那么也就是说求和的过程中，sum会重复出现，这对解题很重要！
# 当我们遇到了要快速判断一个元素是否出现集合里的时候，就要考虑哈希法了。
# 整数变str str(n) 再变整数 int(n)
# 不断拆分循环的是n

n=19
n=2
def isHappy(n):
    seen=[]
    while n!=1:
        for i in str(n):
            n=sum(int(i)**2 for i in str(n))
        if n in seen:
            return False
        seen.append(n)
    return True

isHappy(n)

# In[]
class Solution:
   def isHappy(self, n: int) -> bool:
       seen = set()
       while n != 1:
           n = sum(int(i) ** 2 for i in str(n))
           if n in seen:
               return False
           seen.add(n)
       return True
# In[]
class Solution:
   def isHappy(self, n: int) -> bool:
       seen = []
       while n != 1:
           n = sum(int(i) ** 2 for i in str(n))
           if n in seen:
               return False
           seen.append(n)
       return True

# In[]
class Solution:
    def isHappy(self, n: int) -> bool:        
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self,n: int) -> int: 
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num

# In[]
n=101
new_num = 0  # 用于存放计算结果的变量
while n:
    n, r = divmod(n, 10)  # 将 n 拆解为商和余数
    new_num += r ** 2  # 计算余数的平芳  
    print(n,r,new_num)

 






















    






























