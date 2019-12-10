#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/10 8:05
# @Author  : LI Dongdong
# @FileName: 253. Meeting Rooms II.py
''''''
'''

1.要求：Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
    Input: [[0, 30],[5, 10],[15, 20]]  Output: 2
    Input: [[7,10],[2,4]] Output: 1
    Following up NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
2.理解：calculate number of rooms that is being used at the same time
3.类型：Greedy
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input: None? Y only one? Y repeat？ Y ordered? N value range？ >=0
    output: 0 / int
6. focus on time or space? Whatever
'''

'''
idea：Greedy algorithm
Method：
    sort the input base on list[i][0]
    traversal the elements, record the i-end time in stack
        traversal  the stack, compare i+1 start time with stack elements (end time)
            if start time < stack[i],remove the i elements of stack - 无法实现
        then add the i-end time, and save the length of stack, compare it with former length, record the max value
    return the max value as the min rooms we need
time complex: O(N2) K is number of stack
space complex: O(N)
易错点：
'''

"超时，tO(N2)"
class Solution:
    def minMeetingRooms(self, intervals) -> int:  # input[[]], find min rooms we need
        if intervals == []:  # edge case
            return 0
        if len(intervals) == 1:  # edge case
            return 1

        intervals.sort(key=lambda x: x[0])  # sort the intervals based on first value of elements

        stack = []
        stack.append(intervals[0][1])
        output = 0
        numb = 1
        for i in range(1, len(intervals)):  # find the min number of rooms
            for elem in stack:
                if intervals[i][0] < elem:
                    numb += 1
            stack.append(intervals[i][1])
            output = max(output, numb)
            numb = 1

        return output


x = Solution()
x.minMeetingRooms([[1, 5], [8, 9], [8, 9]])

"optimized code"
'''
改进之处：对stack进行筛选，依旧上课的时间放入tmp中，再加入新上课时间，最后赋给stack。减少了stack的元素数量，减少了遍历时间
易错点：tmp用完以后要清空，重置为[]
time complex: O(Nlogk)
'''
class Solution:
    def minMeetingRooms(self, intervals) -> int:  # input[[]], find min rooms we need
        if intervals == []:  # edge case
            return 0
        if len(intervals) == 1:  # edge case
            return 1

        intervals.sort(key=lambda x: x[0])  # sort the intervals based on first value of elements

        stack = []
        stack.append(intervals[0][1])
        tmp = []
        output = 0
        for i in range(1, len(intervals)):  # find the min number of rooms
            for j in range(len(stack)):
                if stack[j] > intervals[i][0]:
                    tmp.append(stack[j])
            tmp.append(intervals[i][1])
            stack = tmp
            output = max(output, len(stack))
            tmp = []
        return output

'''
idea：Greedy algorithm + heap
Method：
time complex: O(NlogN)
space complex: O(N)
易错点：
'''