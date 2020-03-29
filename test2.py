from copy import deepcopy


class Solution:
    def numTeams(self, rating) -> int:
        if len(rating) < 3:  # corner case
            return 0

        def backtrack(i, item, res):  # return all combination of 3 elem
            if len(rating) - 1 < i:
                return

            item.append(rating[i])
            if len(item) == 3:
                if item[0] < item[1] < item[2] or item[0] > item[1] > item[2]:
                    res.append(1)
            backtrack(i + 1, item, res)
            item.pop()
            backtrack(i + 1, item, res)

        res = []
        backtrack(0, [], res)

        ans = sum(res)
        return ans

x = Solution()
print(x.numTeams([1,2,3,4]))