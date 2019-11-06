# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 20:43
# @Author  : LI Dongdong
# @FileName: lc 187.py
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        seq_map={}
        result=[]
        seq=[]
        for i in range(0,len(s)-9):
            seq=s[i:i+10]
            if seq in seq_map:
                seq_map[seq]+=1
            else:
                seq_map[seq]=1
        for elem in seq_map:
            if seq_map[elem]>1:
                result.append(elem)
        print(result)



x=Solution()
x.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
