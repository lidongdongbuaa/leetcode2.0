#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 22:21
# @Author  : LI Dongdong
# @FileName: Mock523. Continuous Subarray Sum.py
''''''
'''
mock总结
    问题：
        1.考官提问题时，大脑空白 --> 预备：预想可能的问题；空白的时候：坚决明确问题，输入输出，自己理清楚
        2.优化时，逻辑跳跃, 从O(n3) 直接到了 O(n)--> 优化顺序：O(n3) 两个for-> O(n2) 先算前序和/sum -> O(n) -> O(1)
        3.自己的思路没有说清楚 --> 觉得讲不清楚的时候，用小例子表达
        4.被要求往下写时，还是多次重复话语 --> 集中注意力去想题目

知识点：        
    1. any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。 元素除了是 0、空、FALSE 外都算 TRUE。
        any([nums[i] == 0 and nums[i+1] ==0 for i in range(len(nums) -1)])
    2. [x for x in Y] 返回 [x1, x2, x3, x4, ...]
    3. 先解决特殊情况，即先解决k = 0 的情况
    3. dic一般用来记录值和其序号
    
'''
'''
题目分析
1.要求：Given a list of non-negative numbers and a target integer k, 
write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.
2.理解：
3.类型：array 题
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

'''
brute force法
思路：
方法：
边界条件：
time complex: O(n3)
space complex: O(n)
'''
class Solution:
    def checkSubarraySum(self, nums, k):
        stack = []
        for i in range(len(nums) -1):#O(n)
            stack.append(nums[i])
            for j in range(i+1, len(nums)):#O(n)
                stack.append(nums[j])
                if k == 0 and sum(stack) == 0: #sum -> O(n)
                    return True
                elif k != 0 and sum(stack) % k == 0:
                    return True
            stack = []
        return False


'''
brute force法2
思路：用sum代替stack去保存每次的数组,
方法：
边界条件：k=0
time complex: O(n2)
space complex: O(1)
编程技巧：sum_nums 若会被定义覆盖 (sum_nums =0/nums[i]),则可以删除归0的操作
'''
class Solution:
    def checkSubarraySum(self, nums, k):
        sum_nums = 0 #可以删除
        for i in range(len(nums) - 1):#O(n)
            sum_nums = nums[i]
            for j in range(i+1, len(nums)):#O(n)
                sum_nums += nums[j]
                if k == 0 and sum_nums == 0:
                    return True
                elif k != 0 and  sum_nums % k == 0:
                    return True
            sum_nums = 0 #可以删除
        return False

'''
brute force法3
思路：前序和
方法：求前序和prefix, 则i到j的和为prefix[j]-prefix[i]+nums[i]
边界条件：k=0
time complex: O(n2)
space complex: O(n) sum array of size nn is used.

'''
class Solution:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any([nums[i] == 0 and nums[i+1] ==0 for i in range(len(nums) -1)]) #O(n)

        prefix = []
        sum_prefix = 0

        for i in range(len(nums)):
            sum_prefix += nums[i]
            prefix.append(sum_prefix)

        for start in range(len(nums)-1): #O(n)
            for end in range(start+1, len(nums)):#O(n)
                summ = prefix[end] - prefix[start] + nums[start]
                if summ % k == 0:
                    return True
        return False


'''
hash法
思路：满足条件的subarray的头点和尾后一点的余数是相同的，即x + n*K = y，故看有没有相同余数的这个subarray
方法：求前序和，求前序和除以k的余数，若两个余数序号间隔大于2，即j-i>=2，且余数相同，则满足条件，返回为True
边界条件：k = 0
time complex: O(n)
space complex: O(min(k, n)) if k != 0, else O(n). 
            在n<k情况下，遍历完n，就是O(n);在n>k情况下，不重复的余数的可能性就是0,1,2,...k-1，再迭代就是重复的，故次数为k次，故为O(min(k, n))
易错点：prefix_sum_mod[0] = -1 --》针对[0,0],k=3等仅有两个数，且这两个数的和为k的倍数的情况
'''
class Solution:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any([nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums) -1)])

        prefix_sum_mod = {}
        prefix_sum_mod[0] = -1 #易错点
        sum_prefix = 0
        for i in range(len(nums)):#O(n)
            sum_prefix += nums[i]
            if sum_prefix % k not in prefix_sum_mod:
                prefix_sum_mod[sum_prefix % k] = i
            else:
                if i > prefix_sum_mod[sum_prefix % k] + 1:
                    return True
        else:
            False

#升级版-enumerate
class Solution:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any([nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums) -1)])

        prefix_sum_mod = {}
        prefix_sum_mod[0] = -1 #易错点
        sum_prefix = 0
        for i, n in enumerate(nums):#O(n)
            sum_prefix += n
            if sum_prefix % k not in prefix_sum_mod:
                prefix_sum_mod[sum_prefix % k] = i
            else:
                if i > prefix_sum_mod[sum_prefix % k] + 1:
                    return True
        else:
            False

'''
题目变形：求不连续的和是k的n倍
hash法
思路：
方法：
边界条件：
time complex: O(n)
space complex: 
'''
class Solution:
    def checkSubarraySum(self, nums, k):
        if k == 0:
            stack = []
            length = len(nums)
            result = []
            self.recursive_zero(0, length, stack, nums, k, result)
            if result == []:
                return False
            else:
                return True
        else:
            stack = []
            length = len(nums)
            result = []
            self.recursive(0, length, stack, nums, k, result)
            if result == []:
                return False
            else:
                return True


    def recursive(self, i, length, stack, nums, k, result):
        if i == length:
            return
        stack.append(nums[i])
        if len(stack) > 1 and sum(stack) %k == 0:
            result.append(1)
        self.recursive(i + 1, length, stack, nums, k, result)
        stack.pop()
        self.recursive(i + 1, length, stack, nums, k, result)

    def recursive_zero(self, i, length, stack, nums, k, result):
        if i == length:
            return
        stack.append(nums[i])
        if len(stack) > 1 and sum(stack) == 0:
            result.append(1)
        self.recursive_zero(i + 1, length, stack, nums, k, result)
        stack.pop()
        self.recursive_zero(i + 1, length, stack, nums, k, result)



x = Solution()
x.checkSubarraySum([0,0], 0)
