#  Union by rank 方法, 求 component number
class Graph:
    def unionFind(self, n, pairs):  # 
        if not pairs or pairs == [[]]:
            return -1

        groupTag = [i for i in range(n)]
        rank = [1] * n

        def find(index):  # return tag the i node belongs to
            if groupTag[index] == index:
                return index
            else:
                return find(groupTag[index])

        for i, j in pairs:
            root1 = find(i)
            root2 = find(j)
            if root1 == root2:
                continue
            else:
                if rank[root1] >= rank[root2]:
                    rank[root1] += rank[root2]
                    groupTag[root2] = root1
                else:
                    rank[root2] += rank[root1]
                    groupTag[root1] = root2

        print(groupTag)
        nums = len(set([find(i) for i in groupTag]))
        return nums


x = Graph()
print(x.unionFind(9, [[0, 1], [1, 2],[2, 8], [3, 4], [3, 5],[5,6], [6, 7],[1, 3]]))