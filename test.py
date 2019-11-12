import itertools
class Solution:
    def totalFruit(self, tree):
        blocks = [(k, len(list(v))) for k, v in itertools.groupby(tree)]

        if len(blocks) == 1:
            return blocks[0][1]

        ans = i = 0
        typ_dic = {}
        while i < len(blocks):
            sum_weight = blocks[i][1] + blocks[i+1][1]
            ans = max(ans, sum_weight)

        return ans


x = Solution()
print(x.totalFruit([0,1,2,3,4,4,6,6,6,6,5,5,5,5,6,6,6,6,6,6]))