


edges = [[0,1],[0,4],[1,4],[2,3]]
graph = [[] for _ in range(5)]
for i, j in edges:
    graph[i].append(j)
    graph[j].append(i)
print(graph)




