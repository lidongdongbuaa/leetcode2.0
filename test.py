class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        if n == 1:
            return [1]

        from collections import defaultdict

        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)

        res = [0] * n

        def dfs(i):  # scan every node
            times = dfsTimes(i, labels[i])
            res[i] = times

            for j in dic[i]:
                dfs(j)

        def dfsTimes(i, tag):  # scan i's child to find the times of i's label
            times = 0
            if labels[i] == tag:
                times += 1
            for j in dic[i]:
                times += dfsTimes(j, tag)
            return times

        dfs(0)

        return res

X = Solution()
X.countSubTrees(4,[[0,2],[0,3],[1,2]], "aeed")

