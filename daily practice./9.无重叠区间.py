#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:46:56 2022

@author: dantan
"""
intervals=[[1,2],[2,3],[3,4],[1,3]]

intervals[0][1]

#图解 先排序 最好情况 是上一个末尾 <=下一个开头；上一个末尾如果和下一个开头有冲突的时候，比较上一个末尾和下一个末尾 选择末尾小的（右侧区间小）

#将所有区间按照右端点从小到大进行排序，那么排完序之后的首个区间，就是我们选择的首个区间。
intervals.sort(key=lambda x: x[1])

student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。



# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/non-overlapping-intervals
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。


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
        return res
