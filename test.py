from heapq import *


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        if not matrix or matrix == [[]]:  # corner case
            return None

        heap = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if len(heap) < k:
                    heappush(heap, -matrix[i][j])
                else:
                    heappushpop(heap, -matrix[i][j])
        return -heappop(heap)

X = Solution()
X.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
