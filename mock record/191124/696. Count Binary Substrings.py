#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 19:18
# @Author  : LI Dongdong
# @FileName: 696. Count Binary Substrings.py
''''''
'''
题目分析
1.要求：Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
    and all the 0's and all the 1's in these substrings are grouped consecutively. 
    Substrings that occur multiple times are counted the number of times they occur.
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
    Notice that some of these substrings repeat and are counted the number of times they occur.
    Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
2.理解：求子序列的数量，子序列的要求是相同数量的0和1，并且0和0要挨在一起，1和1都要挨在一起
3.类型：array题
4.方法及方法分析：
time complexity order: 
space complexity order: 
5.egde case
    for this array
        None？ N
        has other numb？ N
        how long? 1 - 50000
    for result:
        repeated result is numbered twice? or None - Twice
        if no such subarray, return what? - 0
'''

'''
brute force method
idea：find all substring, and calculate numb of the required substring, 
method：
    traverse the string by two for loop to get all substring, and save them in a list: all_list #tO(N2), sO(N2)
    traverse the list elems, if length of the elem is even, half of elem is one numb, another of elem is another numb, the output + 1 #tO(N2), sO(1)
time complex: O(N2)
space complex: O(N2)
易错点：
'''


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        all_list = []
        for i in range(len(s)):  # traverse to get all substring
            for j in range(i + 1, len(s)):
                all_list.append(s[i:j + 1])

        output = 0
        for elem in all_list:  # traverse all substring
            if len(elem) % 2 == 0:  # substring is even
                length = len(elem)
                half = length // 2
                if elem[0:half] == "1" * half and elem[half:] == "0" * half:  # substring is 1*n + 0*n
                    output += 1
                elif elem[0:half] == "0" * half and elem[half:] == "1" * half:  # substring is 0*n + 1*n
                    output += 1

        return output


'''
accumulate repeated numb time method
idea： the accumulation of two adjacent occurring time of 0/1 is what we want
method：
    traversal string, transfer string into elems occurring times list  #tO(N), sO(N)
    traversal list, compare adjacent two elem, accumulate min of these two elem as result #tO(N), sO(1)
time complex: O(N)
space complex:  O(N)
易错点：遇到新的加旧的进入numb_list, 故在for结束后要numb_list.append(numb)
'''


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:  # only one elem string
            return 0

        numb_list = []
        temp = s[0]
        numb = 1
        for i in range(1, len(s)):  # accumulate elems repeat times
            if temp == s[i]:
                numb += 1
            else:
                numb_list.append(numb)
                numb = 1
                temp = s[i]
        numb_list.append(numb)

        ans = 0
        for i in range(len(numb_list) - 1):  # compare two adjacent numb, accumulate min of them
            ans = ans + min(numb_list[i], numb_list[i + 1])
        return ans

'''
test case
'''
x = Solution()
x.countBinarySubstrings("100101")