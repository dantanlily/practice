#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:06:23 2021

@author: dantan
"""

#deque 是Python标准库 collections 中的一个类，实现了两端都可以操作的队列，相当于双端队列
import collections

d=collections.deque('abcdefg')
print('Deque:',d)

d1=collections.deque()
d1.extend('abcdefg')
print('extend:',d1)

#
#deque 类中实现了单个数据入队，将一个可迭代对象入队，将数据插入指定位置的方法。
#1. 单个数据入队
queue = collections.deque()
queue.append('a') 
queue.append('b')
queue.append('c')
print(queue) #deque(['a', 'b', 'c'])
queue.appendleft('A')
queue.appendleft('B') # deque(['B', 'A', 'a', 'b', 'c'])
print(queue)

#2. 可迭代对象入队
queue.extend(['D', 'E'])
queue.extendleft(['c', 'd']) # first c then d, d is in the left side
print(queue) #deque(['d', 'c', 'B', 'A', 'a', 'b', 'c', 'D', 'E'])

#

queue.insert(3, 'T')
print(queue) #deque(['d', 'c', 'B', 'T', 'A', 'a', 'b', 'c', 'D', 'E'])

#deque 类中实现了队列两端的出队方法。
print(queue.pop()) #E
print(queue.popleft()) # d
print(queue) # print(queue.pop()) deque(['c', 'B', 'T', 'A', 'a', 'b', 'c', 'D'])




















