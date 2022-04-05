#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:43:51 2022

@author: dantan
"""
# 如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。

# 例如，321 是一个步进数，而 421 不是。

# 给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。

#  

# 示例：

# 输入：low = 0, high = 21
# 输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/stepping-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#
low,high=10,15


def func(low,high):
    #all from0 to 9
    l=[0]#步进数列表
    res=[]#范围内步进数筛选
    p=0#指针 到什么位置
    if low<=0:
        res.append(0)
    while l[-1]<9:
        l.append(l[-1]+1)
        if l[-1]>=low and l[-1]<=high:
            res.append(l[-1])
    # above create 0-9
    while l[-1]<high:
        current=l[p]
        if current==0:
            p+=1
            continue
        if str(current)[-1]=="0": # 10 to 101
            nex=current*10+int(str(current)[-1]) +1
            l.append(nex)
            if nex>=low and nex<=high:
                res.append(nex)
        elif str(current)[-1]=="9": # 9- 98 change current number to string
            nex=current*10+int(str(current)[-1])-1
            l.append(nex)
            if nex>=low and nex<=high:
                res.append(nex)
        # 1 to 8 has two adjacent numbers
        else: 
            nexL=current*10+int(str(current)[-1])-1
            nexR=current*10+int(str(current)[-1])+1
            l.append(nexL)
            l.append(nexR)
            if nexL>=low and nexL<=high:
                res.append(nexL)
            if nexR >=low and nexR<=high:
                res.append(nexR)
        p+=1
    return res
          
print(func(10,15))
            
            
            
            
            
            
        
            
            
            

        
            
    