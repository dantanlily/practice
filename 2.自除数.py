#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:23:47 2022

@author: dantan
"""
#728

# 自除数是指可以被它包含的每一位数除尽的数。也可以理解为，
# 自除数对组成其本身的每一位数字进行取余结果都为0。
# 需要注意，自除数不允许包含 0 。例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。


def test(left,right):
    l=[]
    for num in range(left,right+1):
        numStr=str(num)
        numList=[item for item in numStr]
        res=True
        for item in numList:
            itemNum=int(item)
            if itemNum==0:
                res=False
                break
            if num % itemNum !=0:
                res=False
        if res:
            l.append(num)
    return l

print(test(1,22))
print(test(1,200))

l=[1,2,3,4,5,6,7,8]

l2=[item for item in l if item % 2 ==0]
print(l2)

l2=[item for item in l if item >4]
print(l2)


def test(left,right):
    l=[num for num in range(left,right+1) if ([item for item in list(str(num)) if (int(item)!=0 and num % int(item) ==0)] ==list(str(num)))]
    return l

print(test(1,220))                                       




