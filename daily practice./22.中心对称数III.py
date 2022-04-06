#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:11:14 2022

@author: dantan
"""
# 给定两个字符串 low 和 high 表示两个整数 low 和 high ，其中 low <= high ，返回 范围 [low, high] 内的 「中心对称数」总数  。

# 中心对称数 是一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

#  

# 示例 1:

# 输入: low = "50", high = "100"
# 输出: 3 
# 示例 2:

# 输入: low = "0", high = "0"
# 输出: 1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/strobogrammatic-number-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 给定一个整数 n ，返回所有长度为 n 的 中心对称数 。你可以以 任何顺序 返回答案。

# 中心对称数 是一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

#  

# 示例 1:

# 输入：n = 2
# 输出：["11","69","88","96"]
# 示例 2:

# 输入：n = 1
# 输出：["0","1","8"]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/strobogrammatic-number-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#thoughts
# 中心对称数如果是奇数位的，那么最中间的数一定是0，1，8这三个数字中的一个，因为只有这三个数字旋转180度后依然与自身相等。并且从中心开始向两边扩展，两边的数字一定是成对出现的，即00，11，88，69和96这五对数字。
# 如果是偶数位的，则从左向右与从右向左依次取到的数字一定是成对的。 

S=["0","1","8"] #单位数可以出现在中间的
D=["00","11","88","69","96"]#双位数可以向中心扩展的
d=["11","88","69","96"]#双位数不能向两边扩展的

def func(l,n):
    res=[]
    if n>1:
        for c in D:
            for item in l:
                tmp=list(item)
                tmp.insert(len(tmp)//2,c)
                res.append("".join(tmp))
            if res==[]: 
                res=d
        return func(res,n-2)
    if n==1:
        for c in S:
            for item in l:
                tmp=list(item)
                tmp.insert(len(tmp)//2,c)
                res.append("".join(tmp)) #['6','9'] to '69'
            if res==[]:
                res=S
        return res
    return l

print(func([],1)) # ['0', '1', '8']
print(func([],2)) # ['11', '88', '69', '96']
print(func([],3)) 
#['101', '808', '609', '906', '111', '818', '619', 
#'916', '181', '888', '689', '986']
print(func([],4))
#
# ['1001', '8008', '6009', '9006', '1111', '8118', '6119', '9116', '1881', 
#  '8888', '6889', '9886', '1691', '8698', '6699', '9696', '1961', '8968', 
#  '6969', '9966']
print(func([],5))

# '10001', '80008', '60009', '90006', '11011', '81018', '61019', '91016', '18081', 
# '88088', '68089', '98086', '16091', '86098', '66099', '96096', '19061', '89068', 
# '69069', '99066', '10101', '80108', '60109', '90106', '11111', '81118', '61119', 
# '91116', '18181', '88188', '68189', '98186', '16191', '86198', '66199', '96196', 
# '19161', '89168', '69169', '99166', '10801', '80808', '60809', '90806', '11811', 
# '81818', '61819', '91816', '18881', '88888', '68889', '98886', '16891', '86898', 
# '66899', '96896', '19861', '89868', '69869', '99866']


def test(low,high):
    mi=len(low)
    ma=len(high)
    count=0
    while mi<=ma:
        res=func([],mi)
        count+=len(res)
        if mi==len(low) or mi==len(high):
            for item in res:
                if int(item)<int(low) or int(item)>int(high):
                    count-=1
        mi+=1
    return count

print(func([],3))
print(func([],4))


#
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        mi=len(low)
        ma=len(high)
        count=0
        while mi<=ma:
            res=self.func([],mi)
            count+=len(res)
            if mi==len(low) or mi==len(high):
                for item in res:
                    if int(item)<int(low) or int(item)>int(high):
                        count-=1
            mi+=1
        return count


    def func(self,l,n):
        S=["0","1","8"] #单位数可以出现在中间的
        D=["00","11","88","69","96"]#双位数可以向中心扩展的
        d=["11","88","69","96"]#双位数不能向两边扩展的
        res=[]
        if n>1:
            for c in D:
                for item in l:
                    tmp=list(item)
                    tmp.insert(len(tmp)//2,c)
                    res.append("".join(tmp))
                if res==[]: 
                    res=d
            return self.func(res,n-2)
        if n==1:
            for c in S:
                for item in l:
                    tmp=list(item)
                    tmp.insert(len(tmp)//2,c)
                    res.append("".join(tmp)) #['6','9'] to '69'
                if res==[]:
                    res=S
            return res
        return l






    














