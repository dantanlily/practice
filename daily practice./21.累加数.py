#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 23:08:30 2022

@author: dantan
"""
# 累加数 是一个字符串，组成它的数字可以形成累加序列。

# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。

# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。

# 说明：累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。

#  

# 示例 1：

# 输入："112358"
# 输出：true 
# 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 示例 2：

# 输入："199100199"
# 输出：true 
# 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/additive-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

num=[1,5,4,6,7,9]
end1=2 # index
end2=4 # index

print(num[0:end1]) #[1, 5]
print(num[0:end1+1]) #[1, 5, 4]
print(num[end1+1:end2+1])#[6,7]

def func(end1,end2,num):
    res=num[0:end2+1] #'11'
    c1=num[0:end1+1]
    c2=num[end1+1:end2+1]
    if res==num:
        return False
    #累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3
    if (len(c1)>1 and c1[0]=="0") or (len(c2)>1 and c2[0]=="0"):
        return False
    while len(res)<len(num):
        c3=str(int(c1)+int(c2))
        res=res+c3 # res in order to assess while condition, whether len reach the end.
        c1=c2
        c2=c3
    if res==num:
        return True
    return False

# num="112358"
# end1=0
# end2=1

def test(num):
    if len(num)<3:
        return False
    for i in range(0,len(num)-1):
        for j in range(i+1,len(num)):
            if func(i,j,num):
                return True
    return False


print(test("101"))
