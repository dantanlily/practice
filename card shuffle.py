#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 20:52:04 2021

@author: dantan
"""

#Each element after shuffled randomly appears in each position with the same probability
import random

#The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
#mylist = ["apple", "banana", "cherry"]
#random.shuffle(mylist)
#print(mylist)

#1.General same probability approach using random
def shuffle_system(cards):
    random.shuffle(cards)
    return cards
    
A=[i for i in range(0,10)]
A
shuffle_system(A)

#random.randint(a, b)
#Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

# random i from 0 to 100; both 0 and 100 are included
#for i in range(1000):
#    i=random.randint(0,100)
#    if i==100:
#        print(i)

# i from 0 to 9
#for i in range(10):
#    print (i)

#2.Another approach which generate same proabilities (1/n, n-1/n * 1/(n-1),(n-1)/n* (n-2)/(n-1)* 1/(n-2) ....) = 1/n
def shuffle_approach(cards):
    for i in range(len(cards)):
        random_i=i+random.randint(0,(len(cards)-i-1))
        cards[i],cards[random_i]=cards[random_i],cards[i]
        

#3.A'Wrong' approach1, probabilities in diagonal postion is bigger than the others'. 

def shuffle_1st(cards):
    for k in range(len(cards)):
        i=random.randint(0,len(cards)-1)
        j=random.randint(0,len(cards)-1)
        cards[i],cards[j]=cards[j],cards[i]


def shuffle_2nd(cards):
     # k from 0 to len(cards)-1, but has len(cards) numbers to be generated
    for k in range(len(cards)): 
        i= random.randint(0,len(cards)-1)
        cards[i],cards[k]=cards[k],cards[i]        


#Test
A=[i for i in range(0,10)]
A

shuffle_system(A)

#a=[0 for i in range(10)] #list size 10; value =0 from index 0 to 9
#b=[a for j in range (10)]

def test_shuffle(f):
    result=[[0 for i in range(10)] for j in range(10)] # create 10*10 zero
    
    for i in range(1000):
        A=[i for i in range(0,10)]# cards from 0 to 10 as a input to shuffle function
        f(A)# shuffle function to generate random cards
        for j in range(len(A)):
            result[A[j]][j]+=1
    #return result
            
    print('\n'.join([''.join(['{:6}'.format(item) for item in row])
                    for row in result]))


m=test_shuffle(shuffle_system)
type(m)
import numpy as np
a=np.asarray(m)
type(a)

#a.sum()#10000

#a.sum(axis=1)# add each row; array([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])
#a.sum(axis=1,dtype='float')
#a.sum(axis=0)

#print(f"Hello\nWorld!")
#vowels = ["a", "e", "i", "o", "u"]
#vowelsCSV = ",".join(vowels)
#print("Vowels are = ", vowelsCSV)

test_shuffle(shuffle_approach)
test_shuffle(shuffle_1st)# bigger probabilities in diagonal (k-2)/k + 2/k*(k-1)
test_shuffle(shuffle_2nd)#biggler probabilities below diagonal
















