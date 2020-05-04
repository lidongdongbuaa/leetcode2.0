class Graph:
    def checkCycle(self, nums, pairs):  # if having cycle, return True
        if not nums:  # corner case
            return False
        if not pairs or pairs == [[]]:
            return False

        groupTag = [i for i in range(nums)]
        rank = [1] * nums

        def find(i):  # find the root index of i
            if i != groupTag[i]:
                return find(groupTag[i])
            else:
                return i

        def union(i, j):  # union i, j in groupTag
            root1 = find(i)
            root2 = find(j)

            nonlocal time
            if root1 != root2:
                time += 1
                if rank[root1] >= rank[root2]:
                    rank[root1] += rank[root2]
                    groupTag[root2] = groupTag[root1]
                else:
                    rank[root2] += rank[root1]
                    groupTag[root1] = groupTag[root2]

        time = 0
        for i, j in pairs:
            union(i, j)

        return nums - time


X = Graph()
print(X.checkCycle(6, [[0, 1], [1, 2], [3, 4], [5, 3], [0, 2]]))