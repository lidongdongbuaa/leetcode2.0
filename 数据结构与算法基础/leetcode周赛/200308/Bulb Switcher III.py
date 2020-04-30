#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:09
# @Author  : LI Dongdong
# @FileName: Bulb Switcher III.py
''''''
'''
题目分析
1.要求：There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

    At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.
    
    Return the number of moments in which all turned on bulbs are blue.
    
     
    
    Example 1:
    
    
    
    Input: light = [2,1,3,5,4]
    Output: 3
    Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.
    Example 2:
    
    Input: light = [3,2,4,1,5]
    Output: 2
    Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).
    Example 3:
    
    Input: light = [4,1,2,3]
    Output: 1
    Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
    Bulb 4th changes to blue at the moment 3.
    Example 4:
    
    Input: light = [2,1,4,3,6,5]
    Output: 3
    Example 5:
    
    Input: light = [1,2,3,4,5,6]
    Output: 6
     
    
    Constraints:
    
    n == light.length
    1 <= n <= 5 * 10^4
    light is a permutation of  [1, 2, ..., n]
2.理解：find how many time the left part is full when adding numbers
3.类型：prefix
4.确认输入输出及边界条件：
    input: list[int], no repeated, order is turning on the light; len(list) range，[1, 5*10^4 ]
    output: int
    corner case:
        only one in list
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''

A. find the pattern
    Method:
        1. calculate the sum of left n numbs, save it in light_sum
        2. traversal the light list
            tmp accumulate the light numb, i index
                if tmp == light_sum[i], means the left fulled
                    record the times
        3. return the times
    time O(N) space O(N)
易错点：
'''
class Solution:
    def numTimesAllBlue(self, light) -> int:
        if len(light) == 1:  # corner case
            return 1

        tmp = 0
        light_sum = []
        for elem in range(1, len(light) + 1):
            tmp += elem
            light_sum.append(tmp)

        times = 0
        tmp = 0
        for i in range(len(light)):
            tmp += light[i]
            if tmp == light_sum[i]:
                times += 1
        return times

x = Solution()
print(x.numTimesAllBlue([1,2,3,4,5,6]))
