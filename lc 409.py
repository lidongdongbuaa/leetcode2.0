# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 20:57
# @Author  : LI Dongdong
# @FileName: lc 409.py

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dic={}
        for i in s:
            if i in s_dic:
                s_dic[i]=s_dic[i]+1
            else:
                s_dic[i]=1
        count=0
        odd=0
        for value in s_dic.values():
            if value%2==0:
                count=count+value
            else:
                odd=1

        return count+odd










x=Solution()
print(x.longestPalindrome("abccccdd"))