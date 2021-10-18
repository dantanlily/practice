#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 01:10:00 2021

@author: dantan
"""


#332. Reconstruct Itinerary

#Depth-First Search
#Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
#Output: ["JFK","MUC","LHR","SFO","SJC"]

from collections import defaultdict
class Solution(object):
    def findItinerary(self,tickets):
        
        path=defaultdict(list)
        for i in tickets:
            path[i[0]].append(i[1]) # key;value
        for i in path.keys():
            path[i].sort()
        ans=[]
        
        def dfs(node):
            while path[node]:
                dfs(path[node].pop(0))
            ans.append(node)
            
        dfs('JFK')
        
        return ans[::-1]


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
answer=Solution()
answer.findItinerary(tickets)


