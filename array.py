#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 01:53:08 2021

@author: dantan
"""
# solve ax^2+bx+c>=0; if b^2-4ac>0, return two results; if b^2-4ac<0, return error
import math
def solve(a,b,c):
    r=pow(b,2)-4*a*c
    if(r<0):
        raise ValueError("No Solution")
    return (-b+math.sqrt(r)/(2*a),(-b-math.sqrt(r))/(2*a))

solve(1,4,1)
#
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
#


#
import time
import matplotlib.pyplot as plt
import random
import math

def random_list(l):
    return [[int(1000*random.random()) for i in range(l * n)] for n in range(1, 20)]

def last(x): 
    start = time.time()
    r = x[-1]
    t = time.time() - start
    return r, len(x), t

random_lists = random_list(100000)
rst = [last(l) for l in random_lists]
len(rst)
rst

#A singer in a singing competition scored, we designed a program 
#to remove a minimum score and a maximum score and then calculate an average score.
#For example, if the score is: [8,9,5,10,9.5,8,7,9,9.5], the lowest score [8,9,5,10,9.5,8,9,9.5] is removed

#Find the min and max
#Remove it from the list

import time
def singing_score(values):
    start=time.time()
    small_pos=0
    for i in range(1,len(values)): # compare start from 1, 0 is already included
        if values[i]<values[small_pos]:
            small_pos=i
            
    high_pos=0
    
    for i in range(1,len(values)):
        if values[i]>values[high_pos]:
            high_pos=i
            
    values.remove(values[small_pos])
    values.remove(values[high_pos])
    rst=sum(values)/len(values)
    t=time.time()-start
    return rst, len(values),t

values=[8,9,5,10,5,8,7,9,9.5]
singing_score(values)

random_lists=random_list(100000)
rst=[singing_score(l) for l in random_lists]
rst

x=list(zip(*rst))[1]
y=list(zip(*rst))[2]

plt.plot(x,y)

def singing_score2(values):
    start=time.time()
    maxx=values[0]
    minn=values[0]
    summ=values[0]
    for i in range(1,len(values)):
        if values[i]<minn:
            minn=values[i]
        if values[i]>minn:
            maxx=values[i]
        summ+=values[i]
    
    rst=summ/(len(values)-2)
    t=time.time()-start
    return rst,len(values),t

values=[8,9,5,10,5,8,7,9,9.5]
singing_score2(values)

sum(values)/(len(values)-2)


#pi/4=1-1/3+1/5-1/7+1/9+...

def pi1(n):
    pi=0
    sign=1
    for i in range(1,n+1,2):
        pi+=sign*(1/i)
        sign*=-1
    return pi*4

pi1(10000)


def pi2():
    pi=0
    sign=1
    pre=999# anynumber absolute value> delta 
    i=1
    delta=0.000001
    
    while(abs(pi-pre)>delta):
        pre=pi
        pi+=sign*(1/i)
        sign*=-1
        i+=2
    return pi*4

pi2()

#Monte Carlo method

from random import random 

def pi3(TRIES):
    hits=0
    for i in range(TRIES):
        # Generate two random numbers between -1 to 1
        r=random()# random number between 0 to 1
        x=-1+2*r
        r=random()
        y=-1+2*r
        # Check whether the point lies in the unit circle r =1
        if x*x+y*y<=1:
            hits=hits+1
        #The ratio hits/tries is approximately the same as the ratio
        # circle area/square area = pi/4
    return 4.0*hits/TRIES
        
pi3(10000000)


for i in range(1,2,2):
    print(i)
    
for i in range(1,3,2):
    print(i)
    
for i in range(1,4,2):
    print(i)


# Multiplication formula table
def mults():
    for i in range(1,10):
        for j in range(1,i+1):
            print(i,"*",j,"=",i*j,end=" ")
    print()
    
mults()

[(i,j,i*j)for i in range(1,10) for j in range(1,i+1)]











