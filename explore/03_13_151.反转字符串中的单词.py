#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:12:12 2023

@author: dantan
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(sep=' ')
        # start, stop, step
        new_line='' # must initialize 
        for i in range(len(words)-1,-1,-1):
            if words[i]!='': 
                new_line=new_line+words[i]+' '
        return new_line[:-1]

# In[]
# s=" a very good   example  "
# words=s.split(sep=' ')
# print([s.strip(' ') for s in words]) # remove the 8 from the string borders
# print([s.replace(' ', '') for s in words]) # remove all the 8s 


# i=0
# j=len(line)-1
# while i<j:
#     temp=line[i]
#     line[i]=line[j]
#     line[j]=temp
#     i+=1 # inside condition for while condition to determine the end of loop
#     j-=1


      
        
        


