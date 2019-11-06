# -*- coding: utf-8 -*-
# @Time    : 2019/8/6 21:38
# @Author  : LI Dongdong
# @FileName: lc 76.py
class Solution:
    def isWindowOk(self, map_s, map_t, vec_t):
        for k in range(len(vec_t)):
            if vec_t[k] not in map_s:
                return False
            elif map_s[vec_t[k]]<map_t[vec_t[k]]:
                return False
        return True

    def minWindow(self, s: str, t: str):
        map_s={}
        map_t={}
        window_begin=0
        result=""
        vec_t = []
        for i in range(len(t)):
            if t[i] in map_t:
                map_t[t[i]]+=1
            else:
                map_t[t[i]]=1
                vec_t.append(t[i])
        j=0
        i=0
        for i in range(len(s)):
            if s[i] in map_s:
                map_s[s[i]]+=1
            else:
                map_s[s[i]]=1
            while window_begin<i:
                begin_cn=s[window_begin]
                if begin_cn not in map_t:
                    window_begin+=1
                    map_s[begin_cn] -= 1
                elif map_s[begin_cn]>map_t[begin_cn]:
                    map_s[begin_cn]=map_s[begin_cn]-1
                    window_begin=window_begin+1
                else:
                    break
            if self.isWindowOk(map_s,map_t,vec_t):
                new_window_len=i-window_begin+1
                if result==''or len(result)>new_window_len:
                    result=s[window_begin:i+1]
        print(result)



x=Solution()
x.minWindow("ADOBECODEBANC","ABC")