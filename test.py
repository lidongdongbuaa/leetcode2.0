class Solution:
    def sortArrayByParity(self, A):  # even first, odd later
        if len(A) == 0:  # edge case
            return A
        if len(A) == 1:  # edge case
            return A

        i = 0
        j= len(A) - 1
        pivot = A[i]
        while i < j:
            while i < j and A[j] % 2 != 0:  # A[j] is even
                j -= 1
            A[i] = A[j]
            while i < j and A[i] % 2 == 0:  # A[i] is odd
                i += 1
            A[j] = A[i]
        A[i] = pivot
        return A

x = Solution()
x.sortArrayByParity([3,1,2,4])