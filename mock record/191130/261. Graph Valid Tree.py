#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 19:11
# @Author  : LI Dongdong
# @FileName: 261. Graph Valid Tree.py
''''''
'''
261. Graph Valid Tree
1.要求：Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), 
    write a function to check whether these edges make up a valid tree.
    Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]] Output: true
    Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]] Output: false
    Note: you can assume that no duplicate edges will appear in edges. 
    Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
2.理解：图题，检测每个节点是否都被连接，且没有成环
3.类型：Union-find 
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.edge case: 
    input: 
        n <= 0? N 
        n = 1? Y 
        range of length of edges? 0 - unlimited 
        edge has repeated? [1, 0] and [0, 1]? N
        range of value of pair of edge? 0 < value < n
        edge is ordered?
        if n <= length of edges -2, no tree
        if n >= length of edges, have circle
        if n = length of edges, tree of have circle
    output: if None, output? False
    class name: Solution
    focus on time or space? time 
'''

'''
idea：Union-Find method - array
Method：
    build node_set to present the set every node belongs to. index present node, value present set, node 1 belongs to set 1
    traversal edges, for pairs of edges, [A,B], change B's set value to A
    statistic the kinds of value in node_set, 
        case 1 it is 1, no single node/node pair, it is tree
        case 2 it is more than 1, it is not a tree
time complex: 
space complex: 
易错点：
'''