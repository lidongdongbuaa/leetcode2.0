# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 11:37
# @Author  : LI Dongdong
# @FileName: Maximum 69 Number.py
''''''
'''
题目分析
1.要求：Given a positive integer num consisting only of digits 6 and 9. Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
2.理解：Input: num = 9669 Output: 9969
    Explanation: 
    Changing the first digit results in 6669.
    Changing the second digit results in 9969.
    Changing the third digit results in 9699.
    Changing the fourth digit results in 9666. 
    The maximum number is 9969.
3.类型：change number in int
4.确认输入输出及边界条件：
    input: int consisting 6 or 9, > 0
    output: int
    corner case: None? N 0? N 1? Y
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A. 
思路：brute force - change first 6
方法：
    1. scan num in string from left to right
        if find first 6,change to 9, add to new string 
        if find 9 or other 6, add to new string
    2. return int from string
time complex: O(len(str(num)))
space complex: O(1)
易错点：string不支持切片替换操作
'''
class Solution:
    def maximum69Number (self, num: int) -> int:
        if num == 6:
            return 9
        if num == 9:
            return 9

        newS= ''
        count = 0
        for elem in str(num):
            if elem == '9':
                newS += elem
            elif count == 0 and elem == '6':
                newS += '9'
                count += 1
            else:
                newS += elem
        return int(newS)

x = Solution()
print(x.maximum69Number(9669))

'''
B. 
思路：bit manipulation 6 is 0, 9 is 1
方法：
time complex: 
space complex: 
易错点：
'''