#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 21:38:41 2021

@author: dantan
"""


for i in range(5):# for i in range(0,5)
    print(i)

# 0 1 2 3 4 


a=[[i*5+j for j in range(5)] for i in range(5)]

for i in range(0,5):
        print([i*5+j for j in range(5)])

#
#[0, 1, 2, 3, 4]
#[5, 6, 7, 8, 9]
#[10, 11, 12, 13, 14]
#[15, 16, 17, 18, 19]
#[20, 21, 22, 23, 24]

import array
import binascii

s = 'sample' 
a = array.array('u', s)

print('As string:', s)
print('As array :', a)

? array.array

len(a)


a = list(range(0, 9))
print(a)
b = a[3:7]
print(b)

b[0] = -1
print(a)
print(b)


import numpy as np

a = np.arange(10)
print(a)
b = a[3:7]
print(b)

b[0] = -1
print(a)
print(b)

b = a[3:7].copy()
print(b)
b[1] = -2
print(a)
print(b)

a = [0] * 8
a[2] = 1
a

a = [[0] * 8] * 8
a[0][0] = 9
a

a = [0] * 8
a[2] = 1
a

m, n = 3, 2
data = [ [0] * n for j in range(m) ]
data

a = array.array('i', range(5))
print('Initial :', a)

a.extend(range(5))
print('Extended:', a)

print('Slice   :', a[3:6])

print('Iterator:', list(enumerate(a)))

print(type(a))
print(len(a))

a = array.array("B", range(16)) # unsigned char
b = array.array("h", range(-8,9)) # signed short

print(a)
print(repr(a.tostring()))

print(b)
print(repr(b.tostring()))

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.index('banana')

fruits.index('banana', 4) #fruits.index('banana', 5)

fruits.reverse()
fruits

fruits.append('grape')
fruits

fruits.sort()
fruits

squares = []
for x in range(10):
    squares.append(x**2)
squares

squares = [x**2 for x in range(10)]
squares

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]

matrix = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]


for row in matrix:
    print(row)

#[1, 2, 3, 4]
#[5, 6, 7, 8]
#[9, 10, 11, 12]


































