#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 12:50
# @Author  : LI Dongdong
# @FileName: Closest Divisors.py
''''''
'''
题目分析
1.要求：Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.
    
    Return the two integers in any order.
    
     
    
    Example 1:
    
    Input: num = 8
    Output: [3,3]
    Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
    Example 2:
    
    Input: num = 123
    Output: [5,25]
    Example 3:
    
    Input: num = 999
    Output: [40,25]
    
    Constraints:

    1 <= num <= 10^9
2.理解：get num + 1 or num + 2, find two int have less abs of dif can produce them
3.类型： math
4.确认输入输出及边界条件：
    input: int, range：1 <= num <= 10^9
    output: [numb1, numb2]
    corner case: numb = 1
4.方法及方法分析：brute force
time complexity order: 
space complexity order: 
'''
'''
A.brute force
    Method:
        1. get numb1 = num + 1, numb2 = num + 2
        2. find all production combination of numb1 or numb2, save in list
        3. calculate abs, use dic save index and abs, find the min
        4. return min's combination
time complex: O(N)
space complex: O(N)
易错点：int(num**0.5) 取平方根来降低遍历的次数
'''
class Solution:
    def closestDivisors(self, num: int) :
        if num == 1:  # corner case
            return [1, 2]

        num1 = num + 1
        num2 = num + 2

        list1 = self.combination(num1)
        list2 = self.combination(num2)

        list1.extend(list2)

        gap = [abs(a - b) for a, b in list1]
        min_index = 0
        for index, value in enumerate(gap):
            if value < gap[min_index]:
                min_index = index

        return list1[min_index]

    def combination(self, num):  # find all combination
        if num == 1:  # corner case
            return [[1,1]]

        res = []
        for i in range(1,  int(num**0.5) + 1):
            if num % i == 0:
                res.append([i, num // i])
        return res


x = Solution()
print(x.closestDivisors(999))
