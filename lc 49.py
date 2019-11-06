# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 20:34
# @Author  : LI Dongdong
# @FileName: lc 49.py

class Solution:
    def groupAnagrams(self, strs):
        str_dic={}
        for i in strs:
            s = ''.join(sorted(i))
            if s not in str_dic:
                str_dic[s]=[]
                str_dic[s].append(i)
            else:
                str_dic[s].append(i)

        result=[]
        for j in str_dic.values():
            result.append(j)
        return result

x=Solution()
x.groupAnagrams(["eat","tea","tan","ate","nat","bat"])


