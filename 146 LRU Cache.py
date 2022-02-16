#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:04:26 2022

@author: dantan
"""
from typing import List
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        if key not in self.m:
            if len(self.deq) == self.c:
                oldest = self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)

        self.m[key] = value
        self.deq.append(key)


s=LRUCache(3)
s.put(1,1000)
s.put(2,2000)
s.put(3,3000)

#[1,2,3] # 

print(s.get(1))

#[2,3,1] 1 move in first of the cache
s.put(4,4000)
#least<=[3,1,4]<=most
print(s.get(3))
#[1,4,3]










