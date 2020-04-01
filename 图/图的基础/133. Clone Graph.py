#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 11:13
# @Author  : LI Dongdong
# @FileName: 133. Clone 图.py
''''''
'''
题目分析
1.要求：Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.
    
    Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
    
    class Node {
        public int val;
        public List<Node> neighbors;
    }
     
    
    Test case format:
    
    For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.
    
    Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
    
    The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
    
     
    
    Example 1:
    
    
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    Example 2:
    
    
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
    Example 3:
    
    Input: adjList = []
    Output: []
    Explanation: This an empty graph, it does not have any nodes.
    Example 4:
    
    
    Input: adjList = [[2],[1]]
    Output: [[2],[1]]
     
    
    Constraints:
    
    1 <= Node.val <= 100
    Node.val is unique for each node.
    Number of Nodes will not exceed 100.
    There is no repeated edges and no self-loops in the graph.
    The 图 is connected and all nodes can be visited starting from the given node.
2.理解：复制一个graph
3.类型：图基础，构建图
4.确认输入输出及边界条件：
    input: first node of graph
    output: first node of copied graph
    corner case:
        None -> None
        only node without neighbor -> return node copy

5.方法及方法分析：BFS + dict, DFS + dict
time complexity order: O(N)
space complexity order: O(N)
6.如何考
'''
'''
我这个是深度copy，就是相同的值进行了复制，不是题目要求的copy
A. bfs the node and copy it like a tree copy
    Method:
        1. res = new = Node(node.val)
        2. use queue to save [node, new]
            root, new = queue popleft
            traversal root neighbor - elem
                tmp = Node（elem）
                new.neighbor.append(tmp)
                queue.append([elem, tmp])
        3. return res
    time complexity O(N)  space O(N)         
易错点：
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""



from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:  # corner case
            return None
        if not node.neighbors:
            return node.copy()

        res = new = Node(node.val)
        visit = []

        queue =deque([(node, new)])
        while queue:
            node, new = queue.popleft()
            visit.append(node)
            for elem in node.neighbors:
                if elem not in visit:
                    tmp = Node(elem.val)
                    new.neighbors.append(tmp)
                    queue.append([elem, tmp])
        return res

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.neighbors = [b, d]
b.neighbors = [a, c]
c.neighbors = [b, d]
d.neighbors = [a, c]

x = Solution()
print(x.cloneGraph(a).neighbors[1].val)

'''
正确的解法
BFS
    use dict to show corresponding
    先创立点，再建立dic映射，再在新的graph上连接点
易错点：neigbor遇到重复点时，不要重复新建节点
    time complexity O(N)  space O(N) 
'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:  # corner case
            return None
        if not node.neighbors:
            res = Node(node.val)
            return res

        visited = {}

        queue =deque([node])
        visited[node] = Node(node.val)

        while queue:
            n = queue.popleft()
            for elem in n.neighbors:
                if elem not in visited:
                    visited[elem] = Node(elem.val)
                    queue.append(elem)
                visited[n].neighbors.append(visited[elem])
        return visited[node]

'''
B. DFS
    Method:
        1. build visited dict {node:new_node}
        2. dfs() recursion : return dic[Node]
            end： node in dict
            process： dict[node] = newNode
            trigger: for elem in neighbors, do dfs(elem)
        3. return dict[node]
    time complexity O(N)  space O(N) 
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:  # corner case
            return None
        if not node.neighbors:
            res = Node(node.val)
            return res

        dic = {}
        self.dfs(node, dic)
        return dic[node]

    def dfs(self, node, dic):  # result save in dic
        if node in dic:
            return

        dic[node] = Node(node.val)

        for elem in node.neighbors:
            self.dfs(elem, dic)
            dic[node].neighbors.append(dic[elem])
        return