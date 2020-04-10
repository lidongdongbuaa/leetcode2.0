#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 10:16
# @Author  : LI Dongdong
# @FileName: 374. Guess Number Higher or Lower.py
''''''
'''
题目分析
1.要求：We are playing the Guess Game. The game is as follows:

        I pick a number from 1 to n. You have to guess which number I picked.
        
        Every time you guess wrong, I'll tell you whether the number is higher or lower.
        
        You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
        
        -1 : My number is lower
         1 : My number is higher
         0 : Congrats! You got it!
        Example :
        
        Input: n = 10, pick = 6
        Output: 6
2.理解：a array from 1 to n, change the range by binary search to find the pick
    找到对应数值的序号，并返回
3.类型：binary search
4.确认输入输出及边界条件：
    input: n: int; API guess: -1,1,0
    output:the pic number: int
    corner case:
        n is None?  N 
        n is 1? Y -> 1
5.方法及方法分析：Brute force, binary search
time complexity order: binary search O(logN) < brute force O(N)
space complexity order: O(1)
6.如何考
'''
'''
A. Brute force
    Method
     1. traversal all numbers from 0 to n, until it say 0

    time complexity: O(N)
    space: O(1)
'''
class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:   # corner case
            return 1

        for i in range(1, n + 1):
            if guess(i) == 0:
                return i

'''
B. binary search for target
    Method:
        1. corner case - n is 1
        2. determine the left bounder,l, as 0, right bounder, r, as n
        3. mid = (0 + n)//2
        4. do while l <= r
            a. if guess(mid) == 0, return mid
            b. if guess(mid) == 1, l = mid + 1
            c. if guess(mid) == -1, r = mid - 1
    time complexity： O(N)
    space: O(1)
易错点：guess的结果是计算机的数比我的大还是小
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:   # corner case
            return 1

        l = 0
        r = n

        while l <= r:
            mid = (l + r) // 2
            toggle = guess(mid)
            if toggle == 0:
                return mid
            elif toggle == 1:
                l = mid + 1
            elif toggle == -1:
                r = mid - 1

'''
test code
n = 10, pick = 6
l = 0
r = 10
loop 1:
    mid = 5
    guess(mid) = -1
    l = 6
loop 2:
    mid = 6 + 10)// 2 = 8 
    guess(mid) = 1
    r = mid - 1 = 7
loop 3
    mid = 6 + 7)// 2 = 6
    guess(6) = 0
    return 6
    
'''
x = Solution()
x.guessNumber(10)