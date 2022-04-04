#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 00:21:40 2022

@author: dantan
"""
#452

# 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中points[i] = [xstart, xend] 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。

# 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。

# 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。

#  
# 示例 1：

# 输入：points = [[10,16],[2,8],[1,6],[7,12]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# -在x = 6处射出箭，击破气球[2,8]和[1,6]。
# -在x = 11处发射箭，击破气球[10,16]和[7,12]。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
#method 1
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        end=points[0][1]
        num=1
        for i in range(1,len(points)):
            if end<points[i][0]:
                end=points[i][1]
                num+=1
            else: 
                end=min(end,points[i][1])
                #num+=1
        return num
    
#method 2
# 无重叠区间 返回 需要移除区间的最小数量，使剩余区间互不重叠 。
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #[[1,2],[2,3],[3,4],[1,3]]
        intervals.sort(key=lambda x:x[1]) #按照右侧最后一个排序
        end=intervals[0][1]
        res=0
        for i in range(1,len(intervals)):
            if end<=intervals[i][0]:
                end=intervals[i][1]
            else:
                end=min(end,intervals[i][1])
                res+=1
        return len(intervals)-res



