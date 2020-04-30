#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 12:37
# @Author  : LI Dongdong
# @FileName: Filter Restaurants by Vegan-Friendly, Price and Distance.py
''''''
'''
题目分析
1.要求：Given the array restaurants where  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.
    The veganFriendly filter will be either true (meaning you should only include restaurants with veganFriendlyi set to true) or false (meaning you can include any restaurant). In addition, you have the filters maxPrice and maxDistance which are the maximum value for price and distance of restaurants you should consider respectively.
    Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. For restaurants with the same rating, order them by id from highest to lowest. For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.
    Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
    Output: [3,1,5] 
    Explanation: 
    The restaurants are:
    Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
    Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
    Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
    Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
    Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1] 
    After filter restaurants with veganFriendly = 1, maxPrice = 50 and maxDistance = 10 we have restaurant 3, restaurant 1 and restaurant 5 (ordered by rating from highest to lowest). 

    Example 2:
    Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
    Output: [4,3,2,1,5]
    Explanation: The restaurants are the same as in example 1, but in this case the filter veganFriendly

    Example 3:
    
    Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3
    Output: [4,5]
2.理解：按照规定条件筛选和排序
3.类型：list 排序？
4.确认输入输出及边界条件：
    input：restaurants, requirement
    output: index
    corner case: None? N only one? Y
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
思路：brute force
方法：
    scan list three time for three command,left suitable ones tO(N) sO(N)
    order suitble ones by rating and index tO(NlogN) sO(N)
time complex: tO(NlogN)
space complex: sO(N)
易错点：
'''
class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance) :
        veg = []
        if veganFriendly == 1:
            for elem in restaurants:  # scan veganFriendly
                if elem[2] == veganFriendly:
                    veg.append(elem)
        else:
            veg = restaurants

        maxP = []
        for elem in veg:  # scan price
            if elem[3] <= maxPrice:
                maxP.append(elem)

        maxD = []
        for elem in maxP:
            if elem[4] <= maxDistance:
                maxD.append(elem)

        if maxD == []:
            return []

        maxD.sort(key = lambda x: (x[1], x[0]), reverse= True)
        # maxD.sort(key = lambda x: x[0], reverse= True)
        return [elem[0] for elem in maxD]

x = Solution()
print(x.filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 0, 50, 10))