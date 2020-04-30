#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 11:43
# @Author  : LI Dongdong
# @FileName: 5303. Decrypt String from Alphabet to Integer Mapping.py
''''''

'''
split 分拆法
'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {}
        for i in range(1, 27):
            dic[i] = chr(i + 96)
        #print(dic)

        new_s = s.split('#')
        res = ''
        for i in range(len(new_s)):
            if len(new_s[i]) ==1:
                numb = int(new_s[i])
                res += dic[numb]
            elif len(new_s[i]) == 2:
                if i == len(new_s) - 1:
                    for elem in new_s[i]:
                        numb = int(elem)
                        res += dic[numb]
                else:
                    numb = int(new_s[i])
                    res += dic[numb]
            elif 2 < len(new_s[i]):
                for elem in new_s[i][:-2]:
                    numb = int(elem)
                    res += dic[numb]
                numb = int(new_s[i][-2:])
                res += dic[numb]
        return res



x = Solution()
print(x.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))


'''
从后往前计数法
'''