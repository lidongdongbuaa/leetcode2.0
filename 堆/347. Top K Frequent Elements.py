#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 15:17
# @Author  : LI Dongdong
# @FileName: 347. Top K Frequent Elements.py
''''''
'''
题目概述：返回list里，出现频率最高的k个数
题目考点：heap； dic
解决方案：heap用来对出现次数排序；dic用来记录次数
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: 
    nums, list; length range is from 0 to inf; value range is no limit; have repeated value; no order
    k, value range is from 1 to number of unique elements
output:
    list, k most frequent element
corner case
    nums is None, return []

A. dict and sort
    Method
        1. scan every element, save {element:times}
        2. sort dic by times, get list of elements
        3. return last k element
    Time complexity： O(nlogn), n is number of unique elements (<= nums size)
    Space: O(n)

B. dic and heap
    Method
        1. scan elements, save {elem:times} # tO(N)
        2. push(-times, elem) into the heap # tO(log1 + log2 +...logN) = O(logN!) < O(NlogN) 
        3. pop first k top elem in heap # tO(klogN)
    Time complexity: O(logN!) in worst case
    Space: O(N)
'''
from heapq import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(int)
        for elem in nums:
            dic[elem] += 1

        heap = []
        res = []

        for key, value in dic.items():
            heappush(heap, (-value, key))
        while k:
            res.append(heappop(heap)[1])
            k -= 1
        return res


'''
B. counter, and nlargest
Time: O(nlogk)
Space: O(n)
'''
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(int)
        for elem in nums:
            dic[elem] += 1

        return nlargest(k, dic, key=lambda x: dic[x])

