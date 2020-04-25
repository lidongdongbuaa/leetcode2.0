from collections import Counter
from heapq import nlargest
class Solution:
    def topKFrequent(self, nums, k: int):
        from collections import defaultdict
        dic = defaultdict(int)
        for elem in nums:
            dic[elem] += 1

        print(dic.values())

        return nlargest(k,dic,key = lambda x:dic[x])

X = Solution()
print(X.topKFrequent(nums = [1,1,1,2,2,3], k = 2))