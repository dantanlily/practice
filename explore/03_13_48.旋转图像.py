#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:39:59 2023

@author: dantan
"""
# clockwise  顺时针旋转90度
from typing import List
matrix=[[1,2,3],[4,5,6],[7,8,9]]
def spiralOrder(matrix: List[List[int]]):
    for i in range(len(matrix)-1):
        for j in range(i+1,len(matrix)):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
            
    def reverseline(line):
        # remember end of index is length -1 
        i=0
        j=len(line)-1
        while i<j:
            temp=line[i]
            line[i]=line[j]
            line[j]=temp
            i+=1 # inside condition for while condition to determine the end of loop
            j-=1
        return line
    
        
    for i in range(len(matrix)):
        matrix[i]=reverseline(matrix[i])# using brackets to call function properly
    
    return matrix


matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
spiralOrder(matrix)      
   
matrix=[[5,1,9,11]]
spiralOrder(matrix)   


# counterclockwise 逆时针旋转90度

#swap(matrix[i][j],matrix[n-j-1][n-i-1])
matrix=[[1,2,3,4],[5,6,7,8],[7,6,5,4],[4,1,2,3]]
n=len(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)-i): # bound is important
        print(i,j)
        temp=matrix[i][j]
        matrix[i][j]=matrix[n-j-1][n-i-1]
        matrix[n-j-1][n-i-1]=temp


  
        
# In[]
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)-1):
            for j in range(i+1,len(matrix)):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
            
  
        
        def reverseline(line):
            # remember end of index is length -1 
            i=0
            j=len(line)-1
            while i<j:
                temp=line[i]
                line[i]=line[j]
                line[j]=temp
                i+=1 # inside condition for while condition to determine the end of loop
                j-=1
            return line
    
        
        for i in range(len(matrix)):
            matrix[i]=reverseline(matrix[i])# using brackets to call function properly
    
        #return matrix

