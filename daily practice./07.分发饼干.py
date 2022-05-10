#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 20:35:03 2022

@author: dantan
"""

a=[2,3,1]
a.sort() # a =1,2,3

# 455
# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

# 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。


# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/greedy/rvrk1c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        g.sort()
        s.sort()
        i=0
        j=0 # i=j=count=0
        while i <len(g) and j < len(s):
            while j<len(s) and g[i]>s[j]:
                j+=1
            if j<len(s):
                count+=1
            i+=1
            j+=1
        return count
    
Solution().findContentChildren([1,2,3],[1,1])

# 「贪心算法」总是做出在当前看来最好的选择就可以完成任务；
