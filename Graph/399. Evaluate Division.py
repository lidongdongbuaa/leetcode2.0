#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 21:47
# @Author  : LI Dongdong
# @FileName: 399. Evaluate Division.py
''''''
'''
题目分析
1.要求：Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
        Given some queries, return the answers. If the answer does not exist, return -1.0.

        Example:
        Given a / b = 2.0, b / c = 3.0.
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
        return [6.0, 0.5, -1.0, 1.0, -1.0 ].
        
        The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
        
        According to the example above:
        
        equations = [ ["a", "b"], ["b", "c"] ],
        values = [2.0, 3.0],
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
         
        
        The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
2.理解：带权无向图的遍历/ 并查集
3.类型：
4.确认输入输出及边界条件：
    input： equations,[[str, str]]. str is number? letters? All in possible; values, list[float, float,...].
    output: list[float]
    corner case: 
        equation is None? N 
        equation is only one elem? Y -> normally 
        len(equation) == len(values)? Y
        value is None? N
        value is only one? Y
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. Union find set to represent the relationship between the letters
    Method:
易错点：
'''
class Graph:
    def division(self, equations, values, queries):  # return division result
        from collections import defaultdict
        group = defaultdict(dict)  # 带权图的表示方法

        for (x, y), v in zip(equations, values):  # 同时遍历两个数
            group[x][y] = v
            group[y][x] = 1.0 / v  # float格式的话，直接与float格式数字计算即可


        def divide(x, y, visited):  # return x/y result
            if x == y:
                return 1.0
            visited.add(x)
            for value in group[x]:
                if value not in visited:
                    visited.add(value)
                    d = divide(value, y, visited)
                    if d > 0:
                        return d * group[x][value]  # 这里是value，不是y
            return -1.0

        ans = []
        for x, y in queries:
            if x in group and y in group:
                visited = set()
                ans.append(divide(x, y, visited))
            else:
                ans.append(-1)
        print(ans)

x = Graph()
x.division(equations = [ ["a", "b"], ["b", "c"] ],values = [2.0, 3.0], queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ] )