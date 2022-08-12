#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 21:14:35 2022

@author: dantan
"""


import numpy as np
matrix=np.array([[1,1,1,0,1,0],[0,0,0,0,0,1],[0,1,1,1,0,1],[0,0,0,1,0,1],[0,1,1,1,0,1],[0,0,0,0,0,1]])

# import numpy as np
# a = np.arange(12).reshape([3, 4])
# b = np.arange(12).reshape([4, 3])

# In[]
# Recursive method without optimisation
# O(n^4) time | 0 (n^3) space

def squareOfZeroes(matrix):
    lastIdx=len(matrix)-1
    return hasSquareOfZeroes(matrix,0,0,lastIdx,lastIdx,{})

def hasSquareOfZeroes(matrix,r1,c1,r2,c2,cache):
    if r1>=r2 or c1>=c2:
        return False
    
    key=str(r1)+"-"+str(c1)+"-"+str(r2)+"-"+str(c2)
    if key in cache:
        return cache[key]
    
    # imagine
    cache[key]=(
            isSquareOfZeroes(matrix,r1,c1,r2,c2)
            or hasSquareOfZeroes(matrix,r1+1,c1+1,r2-1,c2-1,cache) # inner 
            or hasSquareOfZeroes(matrix,r1,c1+1,r2-1,c2,cache) # bottom left 
            or hasSquareOfZeroes(matrix,r1+1,c1,r2,c2-1,cache) # top right
            or hasSquareOfZeroes(matrix,r1+1,c1+1,r2,c2,cache) # top left
            or hasSquareOfZeroes(matrix,r1,c1,r2-1,c2-1,cache) # bottom right
            )
    return cache[key]

def isSquareOfZeroes(matrix,r1,c1,r2,c2):
    for row in range(r1,r2+1):
        if matrix[row][c1]!=0 or matrix[row][c2]!=0:  # check vertical 0s for each of the rows
            return False
        
    for col in range(c1,c2+1):
        if matrix[r1][col]!=0 or matrix[r2][col]!=0:
            return False
    return True

squareOfZeroes(matrix)
# In[]
# Recursive method with optimisation; improve on isSquareOfZeroes function
# O(n^3) time | 0 (n^3) space

def squareOfZeroes(matrix):
    infoMatrix=preComputeNumOfZeroes(matrix) #as there're duplicate squares
    lastIdx=len(matrix)-1
    return hasSquareOfZeroes(infoMatrix,0,0,lastIdx,lastIdx,{})

def hasSquareOfZeroes(infoMatrix,r1,c1,r2,c2,cache):
    if r1>=r2 or c1>=c2:
        return False
    
    key=str(r1)+"-"+str(c1)+"-"+str(r2)+"-"+str(c2)
    if key in cache:
        return cache[key]
    
    # imagine
    cache[key]=(
            isSquareOfZeroes(infoMatrix,r1,c1,r2,c2)
            or hasSquareOfZeroes(infoMatrix,r1+1,c1+1,r2-1,c2-1,cache) # inner 
            or hasSquareOfZeroes(infoMatrix,r1,c1+1,r2-1,c2,cache) # bottom left 
            or hasSquareOfZeroes(infoMatrix,r1+1,c1,r2,c2-1,cache) # top right
            or hasSquareOfZeroes(infoMatrix,r1+1,c1+1,r2,c2,cache) # top left
            or hasSquareOfZeroes(infoMatrix,r1,c1,r2-1,c2-1,cache) # bottom right
            )
    return cache[key]

def isSquareOfZeroes(infoMatrix,r1,c1,r2,c2):
    squareLength=c2-c1+1
    hasTopBoarder=infoMatrix[r1][c1]["numZeroesRight"]>=squareLength
    hasLeftBoarder=infoMatrix[r1][c1]["numZeroesBelow"]>=squareLength
    hasBottomBorder=infoMatrix[r2][c1]["numZeroesRight"]>=squareLength
    hasRightBorder=infoMatrix[r1][c2]["numZeroesBelow"]>=squareLength
    return hasTopBoarder and hasLeftBoarder and hasBottomBorder and hasRightBorder
    
    

def preComputeNumOfZeroes(matrix):
    infoMatrix=[[x for x in row] for row in matrix]
    n=len(matrix)
    for row in range(n):
        for col in range(n):
            numZeroes=1 if matrix[row][col]==0 else 0
            infoMatrix[row][col]={
                "numZeroesBelow":numZeroes,
                "numZeroesRight":numZeroes,
                }
    lastIdx=len(matrix)-1
    for row in reversed(range(n)):
        for col in reversed(range(n)):
            if matrix[row][col]==1:
                continue
            if row<lastIdx:
                infoMatrix[row][col]["numZeroesBelow"]+=infoMatrix[row+1][col]["numZeroesBelow"]   
            if col<lastIdx:
                infoMatrix[row][col]["numZeroesRight"]+=infoMatrix[row][col+1]["numZeroesRight"]   
    return infoMatrix

squareOfZeroes(matrix)
        
# In[] 
# iterative solution without optimisation
# O(n^4) time | 0 (1) space

def squareOfZeroes(matrix):
    n=len(matrix)
    for topRow in range(n):
        for leftCol in range(n):
            squareLength=2
            while squareLength<=n-leftCol and squareLength<=n-topRow:
                 bottomRow=topRow+squareLength-1
                 rightCol=leftCol+squareLength-1
                 if isSquareOfZeroes(matrix,topRow,leftCol,bottomRow,rightCol):
                     return True
                 squareLength+=1
    return False
    
def isSquareOfZeroes(matrix,r1,c1,r2,c2):
    for row in range(r1,r2+1):
        if matrix[row][c1]!=0 or matrix[row][c2]!=0:  # check vertical 0s for each of the rows
            return False
        
    for col in range(c1,c2+1):
        if matrix[r1][col]!=0 or matrix[r2][col]!=0:
            return False
    return True
    
squareOfZeroes(matrix)    

# In[] 
# iterative solution with optimisation
# O(n^3) time | 0 (n^2) space

def squareOfZeroes(matrix):
    infoMatrix=preComputeNumOfZeroes(matrix)
    n=len(matrix)
    for topRow in range(n):
        for leftCol in range(n):
            squareLength=2
            while squareLength<=n-leftCol and squareLength<=n-topRow:
                 bottomRow=topRow+squareLength-1
                 rightCol=leftCol+squareLength-1
                 if isSquareOfZeroes(infoMatrix,topRow,leftCol,bottomRow,rightCol):
                     return True
                 squareLength+=1
    return False
    
def isSquareOfZeroes(infoMatrix,r1,c1,r2,c2):
    squareLength=c2-c1+1
    hasTopBoarder=infoMatrix[r1][c1]["numZeroesRight"]>=squareLength
    hasLeftBoarder=infoMatrix[r1][c1]["numZeroesBelow"]>=squareLength
    hasBottomBorder=infoMatrix[r2][c1]["numZeroesRight"]>=squareLength
    hasRightBorder=infoMatrix[r1][c2]["numZeroesBelow"]>=squareLength
    return hasTopBoarder and hasLeftBoarder and hasBottomBorder and hasRightBorder
    
    

def preComputeNumOfZeroes(matrix):
    infoMatrix=[[x for x in row] for row in matrix]
    n=len(matrix)
    for row in range(n):
        for col in range(n):
            numZeroes=1 if matrix[row][col]==0 else 0
            infoMatrix[row][col]={
                "numZeroesBelow":numZeroes,
                "numZeroesRight":numZeroes,
                }
    lastIdx=len(matrix)-1
    for row in reversed(range(n)):
        for col in reversed(range(n)):
            if matrix[row][col]==1:
                continue
            if row<lastIdx:
                infoMatrix[row][col]["numZeroesBelow"]+=infoMatrix[row+1][col]["numZeroesBelow"]   
            if col<lastIdx:
                infoMatrix[row][col]["numZeroesRight"]+=infoMatrix[row][col+1]["numZeroesRight"]   
    return infoMatrix

    
squareOfZeroes(matrix)    
    
    
    
    