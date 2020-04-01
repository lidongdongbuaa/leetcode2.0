#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 15:12
# @Author  : LI Dongdong
# @FileName: 841. Keys and Rooms.py
''''''
'''
题目分析
1.要求：There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:  
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.
Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
2.理解：only one start, from it to detect other room, check if can detect all rooms;len(room list) is numb of room
3.类型：graph dfs
4.确认输入输出及边界条件：
    input:  room list[ key list[]], repeated value in key list? Y; order? N
    output:T/F
    corner case:
        room list is None? N
        room list only one element? Y
5.方法及方法分析：
time complexity order: 
space complexity order: 
6.如何考
'''
'''
A. dfs + visited grid
    Method:
        from the room to scan all its neighbors, and label as visited, until all its neighbors visited. if room is not visited, return False
        1. create the visited list [0] * n
        2. traversal all room 0 's neighbors by dfs()
            all visited node labeled 1
        3. check visited list == [1] * n, if true, return True else return Fasle
    time complexity: O(N + E) N is the number of rooms, and E is the total number of keys. 
    space O(N)
易错点：本题是有向图查孤立个数的题目，限定条件是有且仅有一个开头
'''
class Graph:
    def visitRooms(self, rooms):  # return T for can visit all rooms
        if not rooms:  # corner case
            return True
        if len(rooms) == 1:
            return True

        visited = [0] * len(rooms)

        def dfs(i):  # visit i neighbors and label 1
            if visited[i] == 1:
                return

            visited[i] = 1
            for j in rooms[i]:
                dfs(j)
            return

        visited[0] = 1
        for i in rooms[0]:
            if visited[i] == 0:
                dfs(i)
        return visited == [1] * len(rooms)

'''
test code
[[1],[2],[3],[]]
visited = [1,0,0,0]
rooms[0] : 1
    dfs(1)
    visited = [1,1,0,0]
    dfs(2)
    visited = [1,1,1,0]
    dfs(3)
    visited = [1,1,1,1]

[[1,3],[3,0,1],[2],[0]]
visited = [0,0,0,0]
room[0] : 1, 3
visited = [1,0,0,0]
    dfs(1)
    visited = [1,1,0,0]
    dfs(3)
    visited = [1,1,0,1]
    dfs(3)
visited = [1,1,0,1] != [0,0,0,0]
'''

x = Graph()
print(x.visitRooms([[1],[2],[3],[]]))

'''
iteration 实现dfs
易错点： 不要多打=
'''
class Graph:
    def visitRooms(self, rooms):  # return T for visit all rooms
        if not rooms:  # corner case
            return True
        if len(rooms) == 1:
            return True

        visited = [0] * len(rooms)
        visited[0] = 1
        stack = [0]

        while stack:
            index = stack.pop()
            for j in rooms[index]:
                if visited[j] == 0:
                    visited[j] = 1
                    stack.append(j)
        return visited == [1] * len(rooms)

x = Graph()
print(x.visitRooms([[1],[2],[3],[]]))