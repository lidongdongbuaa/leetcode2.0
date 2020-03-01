#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 11:49
# @Author  : LI Dongdong
# @FileName: Rank Teams by Votes.py
''''''
'''
题目分析
1.要求：
2.理解：vote ranking of elem, by the times they apppear at the first position of votes
3.类型：dict
4.确认输入输出及边界条件：
    input: list[string] repeated? Y, elem word repeated? N order? N elem numb? [1, 1000];elem length? [1, 26]
    output: string by first to end
    corner case: None? N, Only one? Y
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
报错！本题意是根据从前到后的出现顺序进行判断，若前面已经出现次数够了，就不用统计后面的次数了
A. count score of team
    Method:
        cancel 1. build a score system where first team get len(team) val, and the last one get 1 value, by build a score-dic{index: value}  time complexity O(N), space O(N)
        2. scan votes elem's index and name tO(N), sO(N)
            use res-dict to record {name:sum score} by index 0 mean score is len(team)
        3. sort the dic by the sum score, return name together tO(NlogN) sO(N)
    time complexity O(NlogN) space O(N)
易错点：打分值，
'''
class Solution:
    def rankTeams(self, votes):  # return string of team name
        if len(votes) == 1:  # corner case
            return votes[0]

        res = {}
        for elem in votes:
            for i, val in enumerate(elem):  # count score
                if val not in res:
                    res[val] = i
                else:
                    res[val] += i

        sorted_res = sorted(res.items(), key = lambda item: (item[1], item[0]))
        res_str = ''
        for team_name, score in sorted_res:
            res_str += team_name
        return res_str

'''
test case
corner case: only one  -> return votes[0]
votes = ["WXYZ","XYZW"]
length = 4
res = {}
loop 1:
    WXYZ
    0 w
    res[w]=4
    1 x
    res[x] = 3
    2 y res[y] =2
    3 z res[z] = 1
loop 2
    XYZW
    0 X
        res[X] 3 + 4 = 7
    1 Y
        res[y] 2 + 3 = 5
    2 Z
        res[z] 1 + 2 = 3
    3 W
        res[w] 4 + 1 = 5
return xwyz
'''
'''
A. count alphabet in every position
    Method:
        1. count alphabet's apperance times. for a, [0:1, 1:2,..]. have len(votes[0]) alphabet, so have such many dict
        2. scan these dict at same time, from first to end, to find most frequent alphabet in every position, if have commom times, search for next positon of these alphebet, ...until find
            else use the alphebet order. save the res alphabet in res string
        3. return the string
易错点：排序a里的字母，可以通过b里的关于a字母的字典集进行排序
'''
from collections import defaultdict
class Solution:
    def rankTeams(self, votes):  # return string of team name
        if len(votes) == 1:  # corner case
            return votes[0]

        num = len(votes[0])  # kinds of alphabet

        lookup = defaultdict(list)
        used = set()  # 统计出现的字符

        for vote in votes:
            for i, v in enumerate(vote):
                used.add(v)
                if len(lookup[v]) == 0:
                    lookup[v] = [0] * 26  # 构造一个dict， key是字母，value是list,[times], 元素是各个位置出现的频率
                lookup[v][i] += 1

        tmp = sorted(list(used), key = lambda x : (lookup[x], -ord(x)))  # ord 技巧
        tmp.reverse()
        return ''.join(tmp)

x = Solution()
x.rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"])