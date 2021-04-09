#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:39:44 2021

@author: dantan
"""


import time
import matplotlib.pyplot as plt
import random
import math 
import numpy as np
#The random() method returns a random floating number between 0 and 1.
#random.random()  0.7332522614492373 

#
#random_lists[0][0] 
#l=100000
#n=1
#random_lists[n-1][n*l-1]

# array random numebr lenth is 10+20=30
#array=[]
#for n in range(1,3):
#    for i in range(10*n):
#        array.append(int(1000*random.random()))


#Generate integars from 0 to 1000, index length is 20(from 0 to 19), 
#number of random numbers in each index is l*n
def random_list(l):
    return [[int(1000*random.random()) for i in range(l * n)] for n in range(1, 20)]


#O(1)-Constant

def square(x):
    return x*x

square(3)

def first(x):
    start=time.time()
    r=x[0]
    t=time.time()-start
    return r,len(x),t

def middle(x):
    start=time.time()
    r=x[len(x)//2]
    t=time.time()-start
    return r,len(x),t

def last(x):
    start=time.time()
    r=x[-1]
    t=time.time()-start
    return r,len(x),t

random_lists=random_list(100000) # 19 list each list size 100000,200000, ....1900000
rst=[last(l) for l in random_lists] #l there is index n in range (1,20)
len(rst) # lengh is 19, tuple type
rst

#The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
#The * operator can be used in conjunction with zip() to unzip the list.

#a=list(zip(*rst)) # size 3, each rolw has r, len(x) and t

x=list(zip(*rst))[1] # different input size (l*n)
y=list(zip(*rst))[2] # time tuple type, e-07....
y1=np.round(y,3)
plt.plot(x,y1)



#O(lgn)

#https://docs.python.org/3/library/bisect.html#module-bisect

import bisect

# initializing list
li = [1, 3, 4, 4, 4, 6, 7]
  
# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print ("The rightmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect(li, 4))
#The rightmost index to insert, so list remains sorted is  : 5
  
# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print ("The leftmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_left(li, 4))
#The leftmost index to insert, so list remains sorted is  : 2
  
# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print ("The rightmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_right(li, 4, 0, 4))
#The rightmost index to insert, so list remains sorted is  : 4

#Bisect examples
#1、bisect，return location, same like bisect_right
data = [4,5,6,7,8]
bisect.bisect(data,9)
#5

#2、bisect_left，return location
data = [4,5,6,7,8]
bisect.bisect_left(data,5)
#1

#3、bisect_right，return location
data = [4,5,6,7,8]
bisect.bisect_right(data,5)
#2

#4、insort number, without changing location
data = [4,5,6,7,8]
bisect.insort(data,9)
data
#[4,5,6,7,8,9]

#5、insort_left
data = [4,5,6,7,8] 
bisect.insort_left(data,5)
data
#[4,5,5,6,7,8]

#6、insort_right
data = [4,5,6,7,8]
bisect.insort_right(data,5)
data
#[4,5,5,6,7,8]
 
## 
#def bs(nums,target):
#    sorted(nums)
#    start=time.time()
#    i=bisect.bisect_left(nums,target)
#    if i!=len(nums) and nums[i]==target:
#        t=time.time()-start
#        return i,len(nums),t
#    t=time.time()-start
#    return -1,len(nums),t

#O(lgn)

import bisect
  
def bs(nums,target):
    sorted_nums=sorted(nums)
    start=time.time()
    i=bisect.bisect_left(sorted_nums,target)
    if i!=len(sorted_nums) and sorted_nums[i]==target: 
        t=time.time()-start
        return i,len(sorted_nums),sorted_nums[i],target,t
    t=time.time()-start
    return False, len(nums),t


random_lists=random_list(10000)
rst=[bs(l,100) for l in random_lists]
len(rst)
rst

x=list(zip(*rst))[1]
y=list(zip(*rst))[4]
y1=np.round(y,3)
plt.plot(x,y)
plt.plot(x,y1)


#O(n)
def find_max(l):
    start= time.time()
    if l == None:
        return None
    mx=l[0]
    for n in l:
        if n>mx:
            mx=n
    t=time.time()-start
    return mx, len(l), t

random_lists=random_list(20000)
rst=[find_max(l) for l in random_lists]
len(rst)
rst

x=list(zip(*rst))[1]
y=list(zip(*rst))[2]
plt.plot(x,y)

#O(nlogn)
def mysort(l):
    start=time.time()
    l.sort(reverse=False)# False from low to high
    t=time.time()-start
    return l[0],len(l),t
random_lists=random_list(10000)
rst=[mysort(l) for l in random_lists]
len(rst)
rst
x=list(zip(*rst))[1]
y=list(zip(*rst))[2]

plt.plot(x,y)

# O(n^2)
def has_duplicate(l):
    start=time.time()
    rst=False
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
                rst=True
    t=time.time()-start
    return rst, len(l),t

random_lists=random_list(100)
rst=[has_duplicate(l) for l in random_lists]

x=list(zip(*rst))[1]
y=list(zip(*rst))[2]

plt.plot(x,y)


#######
from pylab import *

n = arange(1,100)
f1 = 1
f2 = n
f3 = n* (log(n))
f4 = n**2

fig = figure()
ax = fig.add_subplot(111)

ax.plot(f1)
ax.plot(f2)
ax.plot(f3)
ax.plot(f4)

legend(["1", "n", "nlgn", "n^2"], loc=2, fontsize="small")

title('Algorithm Matters') 

xlabel('Size of array (n)')
ylabel('Number of interations')

show()

###
from pylab import *

n = arange(1,15)
f1 = 1
f2 = n
f3 = n* (log(n))
f4 = n**2
f5 = n**3
f6 = 2**n

fig = figure()
ax = fig.add_subplot(111)

ax.plot(f1)
ax.plot(f2)
ax.plot(f3)
ax.plot(f4)
ax.plot(f5)
ax.plot(f6)

legend(["1", "n", "nlgn", "n^2", "n^3", "2^n"], loc=2, fontsize="small")

title('Algorithm Matters') 

xlabel('Size of array (n)')
ylabel('Number of interations')

show()
