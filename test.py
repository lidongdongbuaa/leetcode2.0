from collections import deque


class MySolution:
    def bfsGraph(self, num, slides):
        graph = [[] for _ in range(num)]  # 建立空邻接表
        visited = [0 for _ in range(num)]  # 建立空访问表

        for i, j in slides:  # 填充邻接表
            graph[i].append(j)
            graph[j].append(i)

        queue = deque()
        queue.append(0)

        while queue:
            node_ind = queue.popleft()  # 从某个顶点出发，访问其各个邻接点
            visited[node_ind] = 1
            print('visited node index:%s' % node_ind)
            print('visit: %s' % visited)
            for neigh_ind in graph[node_ind]:  # 从邻接点出发，访问邻接点的邻接点
                if visited[neigh_ind] == 0:
                    queue.append(neigh_ind)
        return


x = MySolution()
x.bfsGraph(5, [[0, 1], [0, 2], [0, 3], [1, 4]])