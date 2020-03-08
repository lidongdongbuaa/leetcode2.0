#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 19:30
# @Author  : LI Dongdong
# @FileName: 444. Sequence Reconstruction.py
''''''
'''
题目分析
1.要求：Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

    Example 1:
    
    Input:
    org: [1,2,3], seqs: [[1,2],[1,3]]
    
    Output:
    false
    
    Explanation:
    [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
    Example 2:
    
    Input:
    org: [1,2,3], seqs: [[1,2]]
    
    Output:
    false
    
    Explanation:
    The reconstructed sequence can only be [1,2].
    Example 3:
    
    Input:
    org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
    
    Output:
    true
    
    Explanation:
    The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
    Example 4:
    
    Input:
    org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
    
    Output:
    true
    UPDATE (2017/1/8):
    The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings). Please reload the code definition to get the latest changes.
2.理解：
3.类型：
4.确认输入输出及边界条件：

5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''

易错点：
'''
''''
太复杂了，没做出来
input: org list[int], seqs list[list]. have order? seq has the same order with Org element.  repeated word in Org? N, in seq list list? No
output: True or False
corner case: 
Org is None, is [] -> False
seq is None is [] -> False
Org and seq is None or [] -> True
if org elem != seq elem , False
Org has only one, seq has only one, and same -> True, else False

A.topological sort 
Method:
create the indegree [] and outdegree[[]] by org and seqs
use stack to save and  traversal nodes with 0 indegree
use DFS to visit node, save the path node in tmp
when reach to terminal, save tmp in res
compare res element with Org, if Org in res, Return True, Else return False

time complexity O(V + E), space complexity O(V)

'''

class Solution:
    def sequenceReconstruction(self, org, seqs) -> bool:
        if not org and not seqs:  # corner case
            return True
        if not org:
            return False
        if not seqs:
            return False
        if org == seqs[0]:
            return True

        tmp = set()
        for elem in seqs:
            for val in elem:
                tmp.add(val)
        if set(org) != tmp:
            return False

        indegree = [0] * len(org)
        outdegree = [[] for _ in range(len(org))]

        for elem in seqs:
            length = len(elem)
            for i in range(0, length - 1):
                indegree[elem[i + 1]] += 1
                outdegree[elem[i]] = elem[i + 1]

        if indegree.count(0) > 1:
            return False

        stack = indegree.index(0)

        tmp = []
        res = []
        for index in stack:
            self.dfs(index, tmp, res, outdegree, seqs)

        if org in res:
            return True
        else:
            return False

    def dfs(self, index, tmp, res, outdegree, seqs):  # save path in res
        if outdegree[index] == []:
            res.append(tmp[:])
            return

        tmp.append(seqs[index])
        for elem in outdegree[index]:
            self.dfs(elem, tmp, res, outdegree, seqs)
        tmp.pop()
        return

x = Solution()
x.sequenceReconstruction([1,2,3], [[1,2],[1,3]])

'''
input: org list[int], seqs list[list]. have order? seq has the same order with Org element.  repeated word in Org? N, in seq list list? No
output: True or False
corner case: 
Org is None, is [] -> False
seq is None is [] -> False
Org and seq is None or [] -> True
if org elem != seq elem , False
Org has only one, seq has only one, and same -> True, else False


核心：queue加入[index, [list of path]]
B. BFS find the path sum
    Method:
        corner case
        create indegree dict, outdegreee dict
        find indegree = 0, push [key,[key]]  of it into queue
            if more than 1, return False
        traversal the queue
            ind, tmp = queue popleft
            if not outdegree[ind]:
                res.append(tmp[:])
            for elem in outdegree[ind]
                indegree[elem] -= 1
                if == 0, queue.append([elem, [key + elem]]). (first copy, then append)
易错点：存在循环，[1, 2], [2, 1],故不能if org == seqs[0]
    indegree初始化，val必须全部赋值0
'''
from collections import defaultdict, deque


class Solution:
    def sequenceReconstruction(self, org, seqs) -> bool:
        if not org and not seqs:  # corner case
            return True
        if not org or not seqs:
            return False
        seq_set = set()
        for elem in seqs:
            for i in elem:
                seq_set.add(i)
        if set(org) != seq_set:
            return False
        # if org == seqs[0]:
        #     return True

        indegree = defaultdict(int)
        for elem in seq_set:
            indegree[elem] = 0
        outdegree = defaultdict(list)

        for elem in seqs:
            for i in range(0, len(elem) - 1):
                indegree[elem[i + 1]] += 1
                outdegree[elem[i]].append(elem[i + 1])

        queue = deque()
        for k, v in indegree.items():
            if v == 0:
                queue.append([k, [k]])
        if len(queue) > 1:  # two 0 indegree node
            return False

        res = []
        while queue:
            ind, tmp = queue.popleft()
            if outdegree[ind] == []:
                res.append(tmp[:])
            for elem in outdegree[ind]:
                indegree[elem] -= 1
                if indegree[elem] == 0:
                    new = tmp[:]
                    new.append(elem)
                    queue.append([elem, new])

        if org in res:
            return True
        else:
            return False




