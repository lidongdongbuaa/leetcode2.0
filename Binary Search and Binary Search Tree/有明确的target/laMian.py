#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 8:33
# @Author  : LI Dongdong
# @FileName: laMian.py
''''''
'''
题目目的概述：只能选一种拉面，0，1，2个配菜，配菜不能重复，只能选一次，问组合中最接近target价格的价格是多少。相同的价格的话，选花钱少的
方法及方法分析：
time complexity order: 
space complexity order: 
如何考
'''
'''
input: [target, [ramem1, ramen2,...], [option1, option2,...]]; target: [1,10000]; ramem numb :[1,10]; option numb :[0,10]
output: price int
corner case:
    1. target is None? N
    2. ramem is None? N; only one? Y
    3. option is None? Y, only one? Y

A.brute force
    Method:
        1. find all combination
            calculate the options' combinaton, use optCom list to save, based on numb of options
                for 0 option
                for 1 option
                for 2 option
            calculate the all combinations, comb list to save
                for ramen types
                    for options' combinations
        2. use binary search to check the target in combinations, if has, return target; else, return closet and min one
            type 1, has clear target
            l, r = 0, len(comb) - 1
            do while loop, l < r
                mid = l + (r - l) // 2
                if target == com[mid]
                    return target
                if <
                    r = mid - 1
                if > 
                    l = mid + 1
            if abs(com[l]) = abs(com[r])
                retrun com[r]
            if  >
                return com[r]
            if <
                return com[l] 
易错点：
    1. set()带0初始化时，要set([0])
    2. set是无法索引的，故需要转化成list
    3. 采用模板1时，l可能会越界，所以
'''


def combine(ramen, options):  # return all combination of ramen and options
    if len(options) == 0:  # get options combinations
        opt = set([0])
    elif len(options) == 1:
        opt = set([0, options[0]])
    else:
        opt = set([0])  # 不要option
        for elem in options:  # 只要一个option
            opt.add(elem)
        for i in range(len(options) - 1):
            for j in range(i + 1, len(options)):  # 注意从i+1开始
                opt.add(options[i] + options[j])

    comb = set()  # get all combinations
    for i in ramen:
        for j in opt:
            comb.add(i + j)
    return list(comb)


def binarySearch(target, comb):  # find the closet one

    comb.sort()  # 不要忘记sort

    if target in comb:
        return target
    if target < comb[0]:
        return comb[0]
    if target > comb[-1]:
        return comb[-1]

    l, r = 0, len(comb) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if target == comb[mid]:
            return target
        if target < comb[mid]:
            r = mid - 1
        else:
            l = mid + 1
    if abs(target - comb[r]) == abs(target - comb[l]):
        return comb[r]
    elif abs(target - comb[r]) < abs(target - comb[l]):
        return comb[r]
    else:
        return comb[l]


def closetPrice(input: [int, list, list]):
    target, ramen, options = input

    comb = combine(ramen, options)
    res = binarySearch(target, comb)
    return res


print(closetPrice([1000, [700, 750], [100, 350, 650]]))