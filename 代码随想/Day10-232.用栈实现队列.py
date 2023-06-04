#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:17:54 2023

@author: dantan
"""

'''
232. 用栈实现队列
简单
919
相关企业
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：

你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

示例 1：

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue) 模拟队列 1先进1就先出
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2] 
myQueue.empty(); // return false
 

提示：
1 <= x <= 9
最多调用 100 次 push、pop、peek 和 empty
'''

'''
同样地，if self.stack_out 也可以用于判断栈是否为空。
在Python中，非空的可迭代对象（如列表）会被视为True，空的可迭代对象会被视为False。
因此，如果self.stack_out不为空，即至少有一个元素，条件判断会为True，可以执行出栈操作。
'''

class MyQueue:
    
    def __init__(self):
        #in主要负责push，out主要负责pop
        self.stack_in=[]
        self.stack_out=[]


    def push(self, x: int) -> None:
        self.stack_in.append(x)
        print('stack_in',self.stack_in)


    def pop(self) -> int:
        if self.empty():
            return None
        #已经有数了 就直接出
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        
    def peek(self) -> int:
        #get the front
        #仅仅是用自定义的function pop看一眼 
        ans=self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek() #返回队列开头的元素 就是看一眼 
param_4 = obj.empty()


# In[]
class MyQueue:

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]


    def push(self, x: int) -> None:
        self.stack_in.append(x)


    def pop(self) -> int:
        if self.empty():
            return False
        if len(self.stack_out)>0:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        ans=self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return (len(self.stack_in)==0 and len(self.stack_out)==0)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''
同样地，if self.stack_out 也可以用于判断栈是否为空。
在Python中，非空的可迭代对象（如列表）会被视为True，空的可迭代对象会被视为False。
因此，如果self.stack_out不为空，即至少有一个元素，条件判断会为True，可以执行出栈操作。
'''








