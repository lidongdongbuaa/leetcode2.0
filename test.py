class Solution(object):
    def isIdealPermutation(self, A):
        if len(A) <= 2:  # edge case
            return True

        floor = len(A)
        for i in range(len(A) - 1, 1 , -1):  # judge A[i] with min(A[i+2:])
            floor = min(floor, A[i])
            if A[i - 2] > floor:
                return False
        return True


x = Solution()
x.isIdealPermutation([1,2,0])