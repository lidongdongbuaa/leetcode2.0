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
2.理解：带权无向图的遍历 weighted undirected graph/ 并查集
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
A. create the graph by dict and use dfs to search this graph to get result
    Method:
        1. create the graph: {a:{b:20}, b:{a:1/2, c:3.0}..} by the equation and values in dict # time O(len(equations)), space O(2 * e)
        2. traversal every pairs in queries  # t O(e * queries) space O(q + e)
            a set named visited to present if the node is visited
            use dfs(x, y of pair) to scan the elements in each pair -> get result: 1.5
                End: x ==y, return 1
                Process: 
                    tag x is visited by add it to set
                    visited x's neighbors j
                        if j not visited:
                            d = dfs(j, y)
                            return d * graph[x][y]
            save the result in a ans list 
        3. return the ans list
    time complexity: O(e + e * q) 
    space complexity: O(e + q)
易错点：
    注意dfs也是有返回值的
    格式上依照无向图的dfs写
    时间空间复杂度也是要根据变量名来写
'''


class Graph:
    def division(self, equations, values, queries):  # return division result
        from collections import defaultdict
        g = defaultdict(dict)  # 带权图的表示方法

        for (x, y), val in zip(equations, values):  # 同时遍历两个数
            g[x][y] = val
            g[y][x] = 1.0 / val  # float格式的话，直接与float格式数字计算即可

        def dfs(x, y, visited):
            if x == y:
                return 1.0

            visited.add(x)  # x就相当于普通dfs里的i， y其实是目标值
            for j in g[x]:  # 对x的邻居进行遍历
                if j not in visited:
                    d = dfs(j, y, visited)
                    if d > 0:
                        return d * g[x][j]
            return -1.0

        ans = []
        for x, y in queries:
            if x in g and y in g:
                visited = set()
                ans.append(dfs(x, y, visited))
            else:
                ans.append(-1)
        return ans


x = Graph()
x.division(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
           queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])

'''
B Union-find method
    不理解，有点难
    方法
        1. 构造groupTag，并计算每种连接方式的值
            
        2. 遍历queries，求每一对的值，加入ans
'''


class Solution:
    def calcEquation(self, equations, values, queries):
        U = {}

        def find(x):
            if x != U[x][0]:
                px, pv = find(U[x][0])
                U[x] = (px, U[x][1] * pv)
            return U[x]

        for (x, y), v in zip(equations, values):
            if x not in U and y not in U:
                U[x] = (y, v)  # 把y设为共同的被除数
                U[y] = (y, 1.0)
            elif x not in U:
                U[x] = (y, v)

            elif y not in U:
                U[y] = (x, 1.0 / v)
            else:  # 如果x，y都存在
                rx, vx = find(x)
                ry, vy = find(y)
                U[rx] = (ry, v / vx * vy)

        def divide(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry:
                return -1
            else:
                return vx / vy

        ans = []
        for x, y in queries:
            if x in U and y in U:
                ans.append(divide(x, y))
            else:
                ans.append(-1)

        return ans

x = Solution()
x.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
           queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])

''''
C.bfs
苏丹的方法，需要学习
'''
class Solution:
    def calcEquation(self, equations, values, queries):
        def buildMap(equations, values, d):
            for (a, b), c in zip(equations, values):
                d[a][b] = c
                d[b][a] = 1.0 / c

        from collections import defaultdict, deque
        d = defaultdict(dict)
        buildMap(equations, values, d)
        res = []

        def helper(d, query):
            a, b = query
            if a not in d or b not in d:
                return -1.0
            if a == b:
                return 1.0

            q = deque()
            q.append((a, 1.0))
            visited = set()
            visited.add(a)
            while q:
                node, value = q.popleft()
                if node == b:
                    return value
                for v in d[node]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, value * d[node][v]))
            return -1.0

        for query in queries:
            res.append(helper(d, query))
        return res
