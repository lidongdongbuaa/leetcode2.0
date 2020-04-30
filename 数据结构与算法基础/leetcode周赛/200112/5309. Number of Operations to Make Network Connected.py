#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/12 12:12
# @Author  : LI Dongdong
# @FileName: 5309. Number of Operations to Make Network Connected.py
''''''
'''
题目分析
1.要求：There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.
    Given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of times you need to do this in order to make all the computers connected. If it's not possible, return -1
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1 Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1 Explanation: There are not enough cables.
2.理解：
3.类型：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：
方法：
边界条件：
time complex: 
space complex: 
易错点：
'''


class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n - 1:
            return -1

        dic = {}
        rep = 0
        for x, y in connections:
            if x not in dic and y not in dic:
                dic[x] = 1
                dic[y] = 1
            elif x not in dic and y in dic:
                dic[x] = 1
                dic[y] += 1
            elif x in dic and y not in dic:
                dic[x] += 1
                dic[y] = 1
            elif x in dic and y in dic:
                rep += 1


        length  = len(dic)
        return n - length

x = Solution()
print(x.makeConnected(100, [[17,51],[33,83],[53,62],[25,34],[35,90],[29,41],[14,53],[40,84],[41,64],[13,68],[44,85],[57,58],[50,74],[20,69],[15,62],[25,88],[4,56],[37,39],[30,62],[69,79],[33,85],[24,83],[35,77],[2,73],[6,28],[46,98],[11,82],[29,72],[67,71],[12,49],[42,56],[56,65],[40,70],[24,64],[29,51],[20,27],[45,88],[58,92],[60,99],[33,46],[19,69],[33,89],[54,82],[16,50],[35,73],[19,45],[19,72],[1,79],[27,80],[22,41],[52,61],[50,85],[27,45],[4,84],[11,96],[0,99],[29,94],[9,19],[66,99],[20,39],[16,85],[12,27],[16,67],[61,80],[67,83],[16,17],[24,27],[16,25],[41,79],[51,95],[46,47],[27,51],[31,44],[0,69],[61,63],[33,95],[17,88],[70,87],[40,42],[21,42],[67,77],[33,65],[3,25],[39,83],[34,40],[15,79],[30,90],[58,95],[45,56],[37,48],[24,91],[31,93],[83,90],[17,86],[61,65],[15,48],[34,56],[12,26],[39,98],[1,48],[21,76],[72,96],[30,69],[46,80],[6,29],[29,81],[22,77],[85,90],[79,83],[6,26],[33,57],[3,65],[63,84],[77,94],[26,90],[64,77],[0,3],[27,97],[66,89],[18,77],[27,43]]))