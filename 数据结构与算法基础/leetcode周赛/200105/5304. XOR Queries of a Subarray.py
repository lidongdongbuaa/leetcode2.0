#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 12:27
# @Author  : LI Dongdong
# @FileName: 5304. XOR Queries of a Subarray.py
''''''

'''
1310. XOR Queries of a Subarray
计算复杂度过高，超时
'''
class Solution:
    def xorQueries(self, arr, queries) :
        res = []
        for elem in queries:
            if elem[0] == elem[1]:
                res.append(arr[elem[0]])
            else:
                tmp = arr[elem[0]]
                for i in range(elem[0] + 1, elem[1] + 1):
                    tmp = tmp^arr[i]
                res.append(tmp)
        return res

x = Solution()
print(x.xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))
print(x.mergeXor([1,3,4, 8]))

'''
Prefix sum method
'''


class Solution:
    def xorQueries(self, arr, queries):
        prefix = []
        for elem in arr:
            if not prefix:
                prefix.append(elem)
            else:
                prefix.append(prefix[-1] ^ elem)

        res = []
        for query in queries:
            l, r = query
            if l == 0:
                res.append(prefix[r])
            elif l == r:
                res.append(arr[l])
            else:
                res.append(prefix[r] ^ prefix[l - 1])
        return res

x = Solution()
print(x.xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))
print(x.mergeXor([1,3,4, 8]))