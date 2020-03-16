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
5.方法及方法分析：DFS, BFS
time complexity order: O(E) + O(E) * Q = (EQ + E)
space complexity order: O(E)
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
    space complexity: O(e)
易错点：
    注意dfs也是有返回值的
    格式上依照无向图的dfs写
    时间空间复杂度也是要根据变量名来写
    注意：d = dfs(elem,j),只有在d != -1时，才返回d * graph[elem][j]，否则进行i的其他neighbors
'''

from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        def buildMap():
            graph = defaultdict(dict)
            for (i, j), val in zip(equations, values):
                graph[i][j] = val
                graph[j][i] = 1.0 / val
            return graph

        graph = buildMap()
        res = []

        def dfs(i, j):  # return pair's multiply result
            if i == j:
                return 1.0

            visited.add(i)
            for elem in graph[i]:
                if elem not in visited:
                    d = dfs(elem, j)
                    if d != -1.0:
                        return d * graph[i][elem]
            return -1.0


        for i, j in queries:
            if i not in graph or j not in graph:
                res.append(-1.0)
            else:
                visited = set()
                res.append(dfs(i, j))
        return res

x = Solution()
print(x.calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x2","x4"]]))
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

'''
C.BFS
    Method:
        1. build graph
            a -> b = 2, b ->a = 1.0/2
        2. do a bfs for each query
            first check if in the map and conrer case a == b
            start to find a shortest path to b and collect the weight and multiply them
            save in res
        3. return res
    
    E = len(equation), Q = len(queries)
    Time complexity: O(E) + O(E) * Q = (EQ + E)
    Space: 
        O(E) = O(Vertex)
易错点：改为buildMap
'''

from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations, values, queries):
        def buildMap():  # build the graph, and return
            graph = defaultdict(dict)
            for (i, j), val in zip(equations, values):
                graph[i][j] = val
                graph[j][i] = 1.0 / val
            return graph

        graph = buildMap()

        def find(i, j):  # use bfs to find i, j division result
            if i not in graph or j not in graph:
                return -1.0
            if i == j:
                return 1.0

            q = deque([(i, 1)])
            visited = set()
            visited.add(i)
            while q:
                node, val = q.popleft()
                if node == j:
                    return val
                for elem, elemVal in graph[node].items():
                    if elem not in visited:
                        visited.add(elem)
                        q.append([elem, elemVal * val ])
            return -1.0

        res = []
        for i, j in queries:
            res.append(find(i, j))
        return res

x = Solution()
print(x.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))