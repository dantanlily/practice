#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:04:59 2021

@author: dantan
"""
class Solution:
    
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        
        for move in moves:
            if (move == 'U'):
                y+=1
            
            elif (move == 'D'):
                y-=1
            elif (move == 'R'):
                x+=1
            elif (move == 'L'):
                x-=1
            
        return x,y # return position is important

s=Solution()
answer=s.judgeCircle("URRDLL")
print(answer)

