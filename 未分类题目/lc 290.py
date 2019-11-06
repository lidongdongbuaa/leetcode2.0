# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 22:16
# @Author  : LI Dongdong
# @FileName: lc 290.py

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        new_str=str.split(' ')
        word_dic={}
        if len(pattern)!=len(new_str):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in word_dic:
                if new_str[i] in word_dic.values():
                    return False
                else:
                    word_dic[pattern[i]]=new_str[i]
            else:
                if word_dic[pattern[i]]==new_str[i]:
                    continue
                elif word_dic[pattern[i]]!=new_str[i]:
                    return False
        return True


x=Solution()
print(x.wordPattern("abba","dog cat cat dog"))