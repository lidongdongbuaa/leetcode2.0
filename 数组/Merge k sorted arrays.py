#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/12 8:39
# @Author  : LI Dongdong
# @FileName: Merge k sorted arrays.py
''''''
'''
Merge k sorted arrays
1.要求：
    Given k sorted arrays of size n each, merge them and print the sorted output.
    Input: k = 3, n =  4 arr = [[1, 3, 5, 7],[2, 4, 6, 8]，[0, 9, 10, 11]] ;
    Output: 0 1 2 3 4 5 6 7 8 9 10 11 
2.理解：合并k个有序数组
3.类型：merge sort
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input:k= 0? Y N=[]？ k=1?Y repeated? Y order? Y
    output:[]/[]/list/list/list
    focus on time or space?
'''

'''
idea：brute force
Method：
    use a stack to append all all element  #sO(nk)
    use sort() to order stack element and return  #tO(nklog(nk))
time complex: O(nklog(nk))
space complex: O(nk)
易错点：arr元素扩展进stack里时，用extend，而不是append
'''
class Merge:
    def mergeArr(self, arr, k, n):  # input: list[list], k, n, merge all sorted list
        if k == 0:  # edge case
            return []
        if n == 0:  # edge case
            return []
        if k == 1:  # edge case
            return arr

        stack = []
        for elem in arr:  # add all elem to stack
            stack.extend(elem)

        stack.sort()  # sort stack

        return stack


x = Merge()
print(x.mergeArr([[1, 5, 9], [2, 4, 7]], 2, 3))

'''
idea：merge sort method
Method：
    divide elements in groups of at most two sublist
    compare, sort and merge every two groups
    process is repeated, until one group left. 
    return the stack
time complex: k/2 * n * logk = O(nklogk)
space complex: O(nk)
易错点：
    注释 merge to left / merge left and right
    想清楚递归是倒数第二步，输入的是大的，返回的是合并好的左右，之后完成最后一步，合并左右
    return arr[0]：  arr形式是[[]]的，故要用arr[0]表示里面括号里的数，才能去掉括号
'''
class Merge:
    def mergeArr(self, arr, k, n):  # input: list[list], k, n, merge all sorted list
        if k == 0:  # edge case
            return []
        if n == 0:  # edge case
            return []
        if k == 1:  # edge case
            return arr[0]

        length = len(arr)  # divide into groups
        mid = length // 2
        L = arr[:mid]
        R = arr[mid:]

        sub_l = self.mergeArr(L, len(L), len(L[0]))  # merge to left
        sub_r = self.mergeArr(R, len(R), len(R[0]))  # merge to right

        stack = []
        i = j = 0
        while i < len(sub_l) and j < len(sub_r):  # merge left and right
            if sub_l[i] < sub_r[j]:
                stack.append(sub_l[i])
                i += 1
            else:
                stack.append(sub_r[j])
                j += 1

        if i < len(sub_l):
            stack.extend(sub_l[i:])
        if j < len(sub_r):
            stack.extend(sub_r[j:])


        return stack

x = Merge()
print(x.mergeArr([[1, 5, 9], [2, 4, 7],[3, 8, 9]], 3, 3))