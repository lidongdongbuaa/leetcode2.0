# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 22:31
# @Author  : LI Dongdong
# @FileName: lc 3.py

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin=0
        result=0
        word=''
        char_map=[]
        for i in range(len(s)):
            char_map.append(s[i])
            if char_map.count(s[i])==1:
                word=word+s[i]
                if result<len(word):
                    result=len(word)
            elif char_map.count(s[i])>1:
                while begin<i and char_map.count(s[i])>1:
                    char_map.pop(0)
                    begin=begin+1
                word=""
                for j in range(begin,i+1):
                    word=word+s[j]
        print(result)
x=Solution()
x.lengthOfLongestSubstring("tmmzuxt")