#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:15:34 2022

@author: dantan
"""
# 860
# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

# 注意，一开始你手头没有任何零钱。

# 给你一个整数数组 bills ，其中 bills[i] 是第 i 位顾客付的账。如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lemonade-change
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #[5,5,10,10,20]
        num5=num10=num20=0
        for i in range(len(bills)):
            if bills[i]==5:
                num5+=1
            if bills[i]==10:
                if num5>=1:
                    num5-=1
                    num10+=1
                else:
                    return False
                    #break
            if bills[i]==20:
                if num5 >=1 and num10>=1:
                    num5-=1
                    num10-=1
                    num20+=1
                elif num5>=3:
                    num5-=3
                    num20+=1
                else:
                    return False
                    #break
        return True