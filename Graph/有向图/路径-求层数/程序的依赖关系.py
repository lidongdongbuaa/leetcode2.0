#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 20:54
# @Author  : LI Dongdong
# @FileName: 程序的依赖关系.py
''''''
'''
题目分析
1.要求：求indegree 0 开始，所有的路径和
2.理解：find the level of the graph
3.类型：
4.确认输入输出及边界条件：

5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
升级版 topological sort
    Method:
        1. Create indegree by dic and outdegree by dic
        2. level = 0
        3. push indegree == 0 node into queue
            traversal the queue
                level + 1
                scan all element of queue
                    queue popleft the node
                    scan the node neighbor in outdegree
                        the neighbor indegree - 1
                        if indegree == 0
                            push this neighbor into queue
        time complexity O(V + E). space complexity O(V)
易错点：
'''
class Solution:
    def findlevel(self, n, pair):  # return level
        if n == 0:
            return 0
        if not pair:
            return 1

        from collections import defaultdict
        outdegree = defaultdict(list)

        indegree = { i : 0 for i in range(1, n + 1)}

        for i, j in pair:
            indegree[j] += 1
            outdegree[i].append(j)

        from collections import deque
        queue = deque([key for key, val in indegree.items() if val == 0])

        level = 0
        while queue:
            length = len(queue)
            level += 1
            for _ in range(length):
                ind = queue.popleft()
                for elem in outdegree[ind]:
                    indegree[elem] -= 1
                    if indegree[elem] == 0:
                        queue.append(elem)
        return level



'''
B.queue里添加[elem, level]
易错点：
    1. 不能写成 queue.append([[x, 1] for key, val in indegree.items() if val == 0])，因为queue里是[[[1],[2]]],列表生成式整个放了进去
    2. 不能在for循环中level += 1，因为是对每层+1，故应该放在while的popleft后，或者queue.append([elem, level + 1])
'''
from collections import defaultdict, deque
def findlevel(n, pair):  # return level
    if n == 0:  # corner case
        return 0
    if not pair:
        return 1

    indegree = { x : 0 for x in range(1, n + 1)}
    outdegree = defaultdict(list)

    for x, y in pair:  # fulfill the table
        indegree[y] += 1
        outdegree[x].append(y)

    queue = deque()
    for k, v in indegree.items():
        if v == 0:
            queue.append([k, 1])
    # 不能写成这样queue.append([[x, 1] for key, val in indegree.items() if val == 0])，

    while queue:
        ind, level = queue.popleft()
        for elem in outdegree[ind]:
            indegree[elem] -= 1
            if indegree[elem] == 0:
                queue.append([elem, level + 1])
    return level


x = Solution()
print(x.findlevel(5, [[1,3], [3, 4], [2, 3], [3, 5], [1, 4]]))