#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:35:51 2023

@author: dantan
"""

# In[] python deque 性质
from collections import deque

# 创建一个空的deque
d = deque()

# 在右侧添加元素
d.append(1)
d.append(2)
d.append(3)

# 在左侧添加元素
d.appendleft(0)

print(d)  # 输出: deque([0, 1, 2, 3])

# 弹出右侧元素
right_element = d.pop()
print(right_element)  # 输出: 3

# 弹出左侧元素
left_element = d.popleft()
print(left_element)  # 输出: 0

# 限制队列长度为2
d = deque(maxlen=2)
d.append(1)
d.append(2)
d.append(3)  # 第一个元素1将被自动弹出
print(d)  # 输出: deque([2, 3])

# 旋转队列
d.rotate(1)
print(d)  # 输出: deque([3, 2])

# 迭代和切片操作
for element in d:
    print(element)  # 输出: 3 2


print(d[2])  # 输出: deque([2])

# In[] 用队列实现栈 先进后出  后入先出

# 想图形 [1,2,3] [2,3,1] [3,1,2] que.popleft() 3
class MyStack:

    def __init__(self):
        self.que=deque()


    def push(self, x: int) -> None:
        self.que.append(x)


    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
            print('que.popleft',self.que)
        return self.que.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.que[-1]


    def empty(self) -> bool:
        return not self.que



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()

param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

# obj.pop()
# que.popleft deque([2, 3, 1])
# que.popleft deque([3, 1, 2])
# Out[169]: 3








































