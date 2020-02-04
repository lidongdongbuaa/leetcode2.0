#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 12:39
# @Author  : LI Dongdong
# @FileName: Reduce Array Size to The Half.py
''''''
'''
题目分析
1.要求：Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
    Return the minimum size of the set so that at least half of the integers of the array are removed.
    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2
    Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
    Possible sets of size 2 are {3,5},{3,2},{5,2}.
    Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
2.理解：删除一半以上的数，又因为由重复值，故求删除的数的种类的最小值
3.类型：array
4.确认输入输出及边界条件：
    input: list 1 <= arr.length <= 10^5,arr.length is even.
    output: int
    corner case: None? N, only one? Y
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：brute force
方法：
    1. get length tO(N) sO(1)
    2. use dic to record value and its times tO(N) sO(N)
    3. get key list with times order tO(NlogN) sO(N)
    3. calculate to reduce values whose total times can reach to half length tO(N) sO(1)
time complex: tO(NlogN) 
space complex: sO(N)
易错点：sort dic的方法
'''


class Solution:
    def minSetSize(self, arr) -> int:
        if len(arr) == 1:  # corner case
            return 1

        length = len(arr)  # get length

        dic = {}  # record value and its times
        for elem in arr:
            if elem not in dic:
                dic[elem] = 1
            else:
                dic[elem] += 1

        res = 0
        half = length // 2
        cur = 0

        new_list = sorted(dic, key=lambda x: dic[x], reverse=True)  # get key list by times

        for elem in new_list:  # get times
            res += 1
            cur += dic[elem]
            if cur >= half:
                return res


x = Solution()
print(x.minSetSize([1000, 1000, 3, 7]))

'''
思路：sort dic
方法：
    1. get length tO(N) sO(1)
    2. use dic to record value and its times tO(N) sO(N)
    3. sort dic by times tO(NlogN) sO(N)
    3. calculate to reduce values whose total times can reach to half length tO(N) sO(1)
time complex: tO(NlogN) 
space complex: sO(N)
易错点：sort dic的方法
'''

class Solution:
    def minSetSize(self, arr) -> int:
        if len(arr) == 1:  # corner case
            return 1

        length = len(arr)  # get length

        dic = {}  # record value and its times
        for elem in arr:
            if elem not in dic:
                dic[elem] = 1
            else:
                dic[elem] += 1

        newDic = sorted(dic.items(), key=lambda item: item[1], reverse=True)  # sort list by times

        res = 0
        half = length // 2
        cur = 0
        for key, value in newDic.items():
            res += 1
            cur += value
            if cur >= half:
                return res


x = Solution()
print(x.minSetSize([1000, 1000, 3, 7]))