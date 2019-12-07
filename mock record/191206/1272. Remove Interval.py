#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 19:40
# @Author  : LI Dongdong
# @FileName: 1272. Remove Interval.py
''''''
'''

1.要求：Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.
    We remove the intersections between any interval in intervals and the interval toBeRemoved.
    Return a sorted list of intervals after all such removals.
    Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6] Output: [[0,1],[6,7]]
    Input: intervals = [[0,5]], toBeRemoved = [2,3] Output: [[0,2],[3,5]]
2.理解：intervals里面去掉与toBeRemoved不相交的区间
3.类型：射击区间题
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input:[]? Y/ length = 1? Y /repeat? N/ sort？ Y/ 取值范围 无
    output: []/ orig output 
    focus on time or space? N
'''

'''
idea：greedy method
Method：
    traversal the elem of interval  # tO(N)
        case1 if elem disjoint toBeRemoved(tBR), output it
        case2 if elem joint tBR on left or right, but not in tBR, output the not disjoint. Two sub cases
        case3 if elem in tBR, output nothing
        case4 if elem cover tBR, output margin. Three sub cases.
    save output in Stack, then return #sO(N)
time complex: 
space complex: 
易错点：
    edge时有两个input，故两个都可能为[]:
    写边界关系的不等式时，基本情况是把四个边界都比较一遍（特殊的case1除外）。例如 case2.1，最后的<toBeRemoved[1]要加上
    这种边界题，一定要考虑所有的边界关系，因为会有重合的，比如 不加 < toBeRemoved[1]的case2.1 和case4 是相同的
'''

class Solution:
    def removeInterval(self, intervals, toBeRemoved):  # output the left part
        if len(intervals) == 0:  # edge case: intervals = []
            return []
        if len(toBeRemoved) == 0:  # edge case: toBeRemove = []
            return intervals

        stack = []
        for i in range(len(intervals)):
            if intervals[i][1] <= toBeRemoved[0] or toBeRemoved[1] <= intervals[i][0]:  # case 1
                stack.append(intervals[i])
            elif intervals[i][0] < toBeRemoved[0] < intervals[i][1] < toBeRemoved[1]:  # case 2.1
                stack.append([intervals[i][0], toBeRemoved[0]])
            elif toBeRemoved[0] < intervals[i][0] < toBeRemoved[1] < intervals[i][1]:  # case 2.2
                stack.append([toBeRemoved[1], intervals[i][1]])
            elif toBeRemoved[0] <= intervals[i][1] < intervals[i][0] <= toBeRemoved[1]:  # case 3
                pass
            elif intervals[i][0] < toBeRemoved[0] < toBeRemoved[1] < intervals[i][1]:  # case 4.1
                stack.append([intervals[i][0], toBeRemoved[0]])
                stack.append([toBeRemoved[1], intervals[i][1]])
            elif intervals[i][0] == toBeRemoved[0] and toBeRemoved[1] < intervals[i][1]:  # case 4.2
                stack.append([toBeRemoved[1], intervals[i][1]])
            elif intervals[i][0] < toBeRemoved[0] and toBeRemoved[1] == intervals[i][1]:  # case 4.3
                stack.append([intervals[i][0], toBeRemoved[0]])
        return stack


