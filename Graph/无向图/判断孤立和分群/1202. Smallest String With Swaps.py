#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 17:04
# @Author  : LI Dongdong
# @FileName: 1202. Smallest String With Swaps.py
''''''
'''
题目分析
1.要求：You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

        You can swap the characters at any pair of indices in the given pairs any number of times.
        
        Return the lexicographically smallest string that s can be changed to after using the swaps.
        
         
        
        Example 1:
        
        Input: s = "dcab", pairs = [[0,3],[1,2]]
        Output: "bacd"
        Explaination: 
        Swap s[0] and s[3], s = "bcad"
        Swap s[1] and s[2], s = "bacd"
        Example 2:
        
        Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
        Output: "abcd"
        Explaination: 
        Swap s[0] and s[3], s = "bcad"
        Swap s[0] and s[2], s = "acbd"
        Swap s[1] and s[2], s = "abcd"
        Example 3:
        
        Input: s = "cba", pairs = [[0,1],[1,2]]
        Output: "abc"
        Explaination: 
        Swap s[0] and s[1], s = "bca"
        Swap s[1] and s[2], s = "bac"
        Swap s[0] and s[1], s = "abc"
         
        
        Constraints:
        
        1 <= s.length <= 10^5
        0 <= pairs.length <= 10^5
        0 <= pairs[i][0], pairs[i][1] < s.length
        s only contains lower case English letters.
2.理解：if all letters can be connected by pairs,  smallest string can be achieve, else, we just change the connected pair letter's order
3.类型：
4.确认输入输出及边界条件：
    input: string, pairs: [[0,1]..]. pair elem would be repeated? N; pair elem ordered? N; string length range? [1, 1000]; letter is low letter? Y
    output: best string.
    corner case: 
        string is None? N 
        string only one letter? Y
        pair is None? Y -> original string
        pair only one elem? Y
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. union-find set to divide groups, list save every group's letter, then order them, then place them back, and return
    Method:
        1. corner case
        2. set initial union groupTag from 0 - n
        3. use Union-find to divide the letter into dif groups as show in groupTag  # time O(N - len(string)) spaceO(N)
            a. find the root1 and root2 of letter in pairs by find() dfs
            b if root1 == root2, pass; else, make groupTag[root2] = root1
        4. sort every letters in every group  # tO(NlogN)
        5. push the sorted letter to their group place in string  # tO(N)
        6. return the string
    Time complexity:  O(NlogN)
    Space complexity: O(N)
易错点：本题发现了Union-find缺陷问题
'''
class String:
    def changeOrder(self, s, pairs):  # return order string
        if not pairs:  # corner case
            return s
        if len(s) == 1:
            return s

        groupTag = [i for i in range(len(s))]  # groupTag = list(range(n))

        def find(x):
            if x == groupTag[x]:
                return x
            return find(groupTag[x])


        def merge(i, j):
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                groupTag[root2] = root1


        for i, j in pairs:
            merge(i, j)

        for i in range(len(groupTag)):
            groupTag[i] = find(i)

        from collections import defaultdict
        type = defaultdict(list)
        for i, j in enumerate(groupTag):
            key = find(j)
            type[key].append(i)   # save group type 1: index1, index2...

        list_s = list(s)
        for key, val in type.items():
            tmp = ''
            for i in val:
                tmp += s[i]
            tmp = sorted(tmp)
            j = 0
            for i in val:
                list_s[i] = tmp[j]
                j += 1

        return ''.join(list_s)

x = String()
print(x.changeOrder(s = "dcab", pairs = [[0,3],[0,2],[1,2]]))






