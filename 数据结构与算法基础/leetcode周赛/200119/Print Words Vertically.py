# -*- coding: utf-8 -*-
# @Time    : 2020/1/19 11:52
# @Author  : LI Dongdong
# @FileName: Print Words Vertically.py
''''''
'''
题目分析
1.要求：Given a string s. Return all the words vertically in the same order in which they appear in s.
    Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
    Each word would be put on only one column and that in one column there will be only one word.
    Example 1:
    
    Input: s = "HOW ARE YOU"
    Output: ["HAY","ORO","WEU"]
    Explanation: Each word is printed vertically. 
     "HAY"
     "ORO"
     "WEU"
    1 <= s.length <= 200
    s contains only upper case English letters.
    It's guaranteed that there is only one space between 2 words.
    
    Example 3:
    Input: s = "CONTEST IS COMING"
    Output: ["CIC","OSO","N M","T I","E N","S G","T"]
2.理解：竖向输出每个字符
3.类型：string
4.确认输入输出及边界条件：
    input：string 1 <= s.length <= 200
    output: list[string, string]
    corner case: None? Y Only one? Y
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A.
思路：split and scan
方法： 
    1. splite s with blanket, get list containing elems tO(N) ? 
    2. scan elems at same time，get longest of length of elems tO(N) N is numb of alphabet sO(N)
            scam i in elem
                if i, add to tmp
                else, add ' ' to tmp
            add tmp to res
time complex:  O(N)
space complex: O(N)
易错点：
'''
class Solution:
    def printVertically(self, s: str):
        if s == ' ':  # corner case
            return [' ']
        if len(s) == 1 and s.isalpha():
            return [s]

        sList = s.split(' ')  # transfer to list

        maxLen = 0  # get longest length of words
        for elem in sList:
            if len(elem) > maxLen:
                maxLen = len(elem)

        tmp = ''
        res = []
        for i in range(maxLen):  # scan sList and transfer
            for elem in sList:
                if i < len(elem):
                    tmp += elem[i]
                else:
                    tmp += ' '
            tmp = tmp.rstrip()  # delete Trailing spaces
            res.append(tmp)
            tmp = ''

        return res

x = Solution()
print(x.printVertically("HOW ARE YOU"))