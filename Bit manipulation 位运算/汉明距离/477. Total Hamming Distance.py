#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 21:17
# @Author  : LI Dongdong
# @FileName: 477. Total Hamming Distance.py
''''''
'''
题目分析
1.要求：The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
    Now your job is to find the total Hamming distance between all pairs of the given numbers.
    Input: 4, 14, 2
    Output: 6
    Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
    showing the four bits relevant in this case). So the answer will be:
    HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
2.理解：求一组数中，两两个数中的汉明距离的和
3.类型：bit manipulation
4.边界条件：Elements of the given array are in the range of 0 to 10^9。Length of the array will not exceed 10^4.
list []? N only one? N repeat? N order? N
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A.
思路：bit compare two by two
方法：
    compare two by two number
        count dif numb
        accumulate dif numb
time complex: O(N**2)
space complex: O(1)
缺点：time complexity过高
易错点：第二个循环是从i开始，而不是1开始的
'''
class Solution:
    def totalHammingDistance(self, nums) -> int:
        res = 0
        for i in range(len(nums) - 1):  # find all two pairs
            for j in range(i, len(nums)):
                res += self.countDif(nums[i], nums[j])
        return res

    def countDif(self, numb1, numb2):  # count dif value, output: int
        z = numb1 ^ numb2
        dif = 0
        while z != 0:
            z = z & z - 1
            dif += 1
        return dif

x = Solution()
print(x.totalHammingDistance([4,14,4,14]))

'''
B.
思路：record 1 and 0 for every bit of all elem at the same time
方法：
    scan every bit
        scan every number, calculate distance for this numb
        accumulate all distance
time complex: O(32 * N) = O(N)
space complex: O(1)
易错点：每一位的汉明距离为 0 出现的次数乘以 1 出现的次数
'''
class Solution:
    def totalHammingDistance(self, nums) -> int:
        if nums == []:
            return 0

        res = 0
        for i in range(32):
            t1 = 0
            t2 = 0
            for elem in nums:
                if elem >> i & 1 == 1:
                    t1 += 1
                else:
                    t2 += 1
            res += t1 * t2
        return res

x = Solution()
print(x.totalHammingDistance([4,14,4,14]))