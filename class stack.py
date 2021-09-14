#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:14:35 2021

@author: dantan
"""

# Stack()    建立一个空的栈对象
# push()     把一个元素添加到栈的最顶层
# pop()      删除栈最顶层的元素，并返回这个元素
# peek()     返回最顶层的元素，并不删除它
# isEmpty()  判断栈是否为空
# size()     返回栈中元素的个数


class Stack: 
    """模拟栈""" 
    def __init__(self): 
        self.items = [] 

    def isEmpty(self): 
        return len(self.items)==0  

    def push(self, item): 
        self.items.append(item) 

    def pop(self): 
        return self.items.pop()  

    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 

    def size(self): 
        return len(self.items) 

s=Stack() 
print(s.isEmpty()) 
s.push(4) 
s.push('dog') 
print(s.peek()) # dog return the last value; not delete
s.push(True) 
print(s.size()) 
print(s.isEmpty()) 
s.push(8.4) 
print(s.pop()) # 8.4 return the last value; deleted 
print(s.pop()) # True 
print(s.size()) 