#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 18:49:52 2022

@author: dantan
"""
# 给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。

# 丑数是可以被 a 或 b 或 c 整除的 正整数 。

#  

# 示例 1：

# 输入：n = 3, a = 2, b = 3, c = 5
# 输出：4
# 解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
# 示例 2：

# 输入：n = 4, a = 2, b = 3, c = 4
# 输出：6
# 解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ugly-number-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


#最小公倍数
def common(a,b):
    n=a*b
    while b>0:
        temp =a%b  
        a=b
        b=temp
    return int(n/a)

# print(common(2,3))
# print(common(2,4))
# print(common(4,2))

# print(common(10,12))

def search(mi,ma,a,b,c,n):
    if mi>=ma:
        return mi
    mid = int((mi+ma)/2)
    
    ab=common(a,b)
    ac=common(a,c)
    bc=common(b,c)
    abc=common(a,bc)
    
    #count 多少个丑数 
    count=int(mid/a)+int(mid/b)+int(mid/c)-int(mid/ab)-int(mid/ac)-int(mid/bc)+int(mid/abc)
    if count==n:
        return mid
    if count<n:
        return search(mid+1,ma,a,b,c,n)
    else:
        return search(mi,mid-1,a,b,c,n)

def func(a,b,c,n):
    mi=min(a,b,c) #最小边界
    ma=mi*n #最大边界
    res=search(mi,ma,a,b,c,n)# return的是mid
    la=res%a
    lb=res%b
    lc=res%c
    return res-min(la,lb,lc) #res-余数
 

print(func(2,3,5,3)) # 4
print(func(2,3,5,5)) # 6


a,b,c,n=2,3,5,3

# clean 

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        mi=min(a,b,c) #最小边界
        ma=mi*n #最大边界
        res=self.search(mi,ma,a,b,c,n)# return的是mid
        la=res%a
        lb=res%b
        lc=res%c
        return res-min(la,lb,lc) #res-余数
    
    
    def common(self,a,b):
        n=a*b
        while b>0:
            temp =a%b  
            a=b
            b=temp
        return int(n/a)

    def search(self,mi,ma,a,b,c,n):
        if mi>=ma:
            return mi
        mid = int((mi+ma)/2)
        
        ab=self.common(a,b)
        ac=self.common(a,c)
        bc=self.common(b,c)
        abc=self.common(a,bc)
        
        #count 多少个丑数 
        count=int(mid/a)+int(mid/b)+int(mid/c)-int(mid/ab)-int(mid/ac)-int(mid/bc)+int(mid/abc)
        if count==n:
            return mid
        if count<n:
            return self.search(mid+1,ma,a,b,c,n)
        else:
            return self.search(mi,mid-1,a,b,c,n)



   


