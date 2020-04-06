#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 13:04
# @Author  : LI Dongdong
# @FileName: 946. Validate Stack Sequences.py
''''''
'''
题目概述：假设一个stack，进行push和pop一列的数，但是先后次序不确定，判断push和pop完成之后，stack是否为空
题目考点：模拟stack的流程
解决方案：模拟stack的流程，先加进去，后对能否进行pop进行判断
方法及方法分析：stack模拟法
time complexity order: O(N)
space complexity order: O(N)
如何考
'''
'''
case
pushed = [1,2,3,4,5], popped = [4,3,5,1,2] -> 

input: 
    pushed; list; length range from 0 to pop; value range from 0 to 1000
    popped; list; length = push; value range as pushed
    pushed is a permutation of popped
output:
    True if stack is empty, else False
corner case: 
    pushed length = popped length = 0, return True
    pushed == popped, return True

A. stack simulation
    Method:
        1. corner case
        2. stack to save pushed elem i one by one, until pushed i elem == popped j elem, pushed elem and popped elem move forward one step
        stack [1,2,3] -> pushed[3] = popped[0], so i = 4, j = 1
        3. then check popped elem with stack top elem, if same, stack pop top elem, and pop move a step,until not same
        stack[-1] == pop[1] = 3, stack.pop, stack=[1,2]
        4. then push move forword as step2, if i exceed range of pushed, and stack is not [], return False

易错点：
'''


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed == []:
            return True
        if pushed == popped:
            return True

        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return len(stack) == 0


'''
test case
 pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
 i = j = 0, stack = []

pushed = [1,2,3,4,5]
                    i
popped = [4,5,3,2,1]
                    j        

pushed[i] = 1, 2, 3
popped[j] = 4
stack = []
'''
