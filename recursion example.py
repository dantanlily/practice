#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:15:11 2022

@author: dantan
"""

# calculation n! factorial
def Factorial(n):
    if n<=1:
        return 1
    return n* Factorial(n-1)

#Fibonacci array 1,1,2,3,5,13,21,34
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

#
def recursion(level, param1, param2, ...):
    
    # recursion terminator
    if level > MAX_LEVEL:
        print_result
        return 
    # process logic in current level
    process_data(level,data)
    
    #drill down
    self.recursion(level+1,p1,...)
    
    # reverse the current level status if needed
    reverse_state(level)

#
def divide_conquer(problem,param1,param2,..):
    
    # recurions terminator
    if problem is None:
        print_result
        return
    #prepare data
    data=prepare_data(problem)
    subproblems=split_problem(problem,data)
    
    #conquer subproblems
    subresults1=self.divide_conquer(subproblems[0],p1,..)
    subresults2=self.divide_conquer(subproblems[1],p1,..)
    subresults3=self.divide_conquer(subproblems[2],p1,..)
    
    ...
    # process and generate the final result
    result=process_result(subresults1,subresults2,subresults3,...)








