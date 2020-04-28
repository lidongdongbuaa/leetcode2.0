class Graph:
    def clone(self, nums):
        self.dic = {}

        def helper(nums):
            self.dic[nums[1]] = 2

        helper(nums)
        print(self.dic[nums[1]])

x = Graph()
x.clone([1,2,3])