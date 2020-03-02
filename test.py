class Solution:
    def findOrder(self, nums, condition):  # return T/F
        if nums == 0:  # corner case
            return []
        if condition == []:
            return [i for i in range(nums)]
        if nums == 1:
            return [0]

        graph = [[] for _ in range(nums)]
        visit = [-1 for _ in range(nums)]  # 三种状态，-1未访问，0正在DFS中访问，1已经访问

        for i, j in condition:  # build adjacency table
            graph[j].append(i)

        stack = []
        for i in range(nums):
            if visit[i] == -1:  # 只访问未访问的，相当于剪枝
                if not self.dfs(graph, visit, i, stack):
                    return []
        return stack[::-1]


    def dfs(self, graph, visit, ind, stack):  # when repeat, return True or False
        if visit[ind] == 0:
            return False
        if visit[ind] == 1:
            return True

        visit[ind] = 0
        for elem in graph[ind]:
            if not self.dfs(graph, visit, elem, stack):
                return False
        visit[ind] = 1  # 底部的
        stack.append(ind)
        return True

x = Solution()
x.findOrder(5, [[3,2],[2,1],[1,0],[0,4]])