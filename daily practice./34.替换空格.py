#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:43:35 2022

@author: dantan
"""

# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

# 示例 1：

# 输入：s = "We are happy."
# 输出："We%20are%20happy."
#  

# 限制：

# 0 <= s 的长度 <= 10000

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#Python 
def replaceSpace(self, s: str) -> str:
    s=s.replace(" ","%20")
    return s


# C++ more quick 0 ms
# 先填充多余空格 再从后往前填充替换数字
class Solution {
   public:
    string replaceSpace(string s) {
        int length = s.size();
        for (int i = 0; i < length; i++) {
            if (s[i] == ' ') {
                s += "  ";
            }
        }
        int j = s.size() - 1;
        for (int i = length - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                s[j--] = '0';
                s[j--] = '2';
                s[j--] = '%';
            } else {
                s[j--] = s[i];
            }
        }
        return s;
    }
};
