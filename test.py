class Graph:
    def minTimes(self, n, pairs):
        groupTag = [i for i in range(n)]

        def find(index):  # return root index of i
            if groupTag[index] == index:
                return index
            else:
                return find(groupTag[index])

        rank = [1] * n
        for i, j in pairs:
            root1 = find(i)
            root2 = find(j)
            if root1 == root2:
                continue
            else:  # 把附着点少的点附着到附着点多的点上
                if rank[root1] >= rank[root2]:  # rank[i] = n 意思是n个点附着在点i上；root1上的附着点多于root2上的附着点
                    rank[root1] += rank[root2]  # 把root2附着到root1上
                    groupTag[root2] = root1  # 附着之后，把root2的标号改为root1，说明root2以root1为group leader
                else:
                    rank[root2] += rank[root1]
                    groupTag[root1] = root2

        print(groupTag)


x = Graph()
print(x.minTimes(3, [[0, 1],[2, 1]]))