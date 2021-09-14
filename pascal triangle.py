#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:53:01 2021

@author: dantan
"""
#https://leetcode.com/problems/pascals-triangle/

#Given an integer numRows, return the first numRows of Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

    
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[[1]*i for i in range(1,numRows+1)]
        i=2
        while i< numRows:
            for j in range(1,i):
                triangle[i][j]=triangle[i-1][j]+triangle[i-1][j-1]
            i+=1
        return triangle

#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]