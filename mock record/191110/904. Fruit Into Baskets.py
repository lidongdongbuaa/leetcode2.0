#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 21:10
# @Author  : LI Dongdong
# @FileName: 904. Fruit Into Baskets.py
''''''
'''
题目分析
1.要求：In a row of trees, the i-th tree produces fruit with type tree[i].
        You start at any tree of your choice, then repeatedly perform the following steps:
        Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
        Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
        Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
        You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
        What is the total amount of fruit you can collect with this procedure?
        Input: [0,1,2,2]
        Output: 3
        Explanation: We can collect [1,2,2].
        If we started at the first tree, we would only collect [0, 1].
2.理解：寻找包含两种元素的最长子序列
3.类型：
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''

'''
dic保存迭代法 - brute force
思路：begin at a position, then traverse the tree, record the type and number, until find two type fruit, then record the sum of fruit.
    do this step from the first tree to the last 2nd tree. finally return the biggest sum
方法：使用for，对point进行遍历，从第一个到倒数第二个：使用while寻找到两种水果，用dic的key记录种类，用value记录该种的个数，直到到达第三种key；
    sum = key1.val + key2.val, 用list记录所有的sum，然后对list进行sort，找到最大的sum，然后输出
    ->优化：用判断语句替代list，定义sum=0，若发现新的sum比原来的大，就替换掉原来的sum
边界条件：list = []
time complex: O(N2)
space complex: O(N)
易错点：dic只保存了两个数，故是sO(2)，不是sO(N)
'''

class Solution:
    def totalFruit(self, tree):
        if tree == []:
            return 0
        if len(tree) == 1:
            return 1

        sum_list = []
        for i in range(len(tree) - 1): #tO(N)*O(N) = O(N2)
            fruit_dic = {}
            type_fruit = 0
            for j in range(i, len(tree)): #tO(N)
                if tree[j] not in fruit_dic:
                    if type_fruit == 2:
                        break
                    fruit_dic[tree[j]] = 1
                    type_fruit += 1
                else:
                    fruit_dic[tree[j]] += 1
            sum_fruit = 0
            for value in fruit_dic.values(): #sO(2) = sO(1)
                sum_fruit += value
            sum_list.append(sum_fruit) #sO(N)

        sum_list.sort() #tO(NlogN)
        return sum_list[-1]

x = Solution()
x.totalFruit([0])


'''
升级版-用j-i+1/j-i表示区间长度；用max(x1,x2)找到最大值，替换掉list及list.sort
time complex: O(N2)
space complex: O(1)
'''
class Solution:
    def totalFruit(self, tree):
        if tree == []:
            return 0
        if len(tree) == 1:
            return 1

        res_fruit = 0
        for i in range(len(tree)): #tO(N)*O(N) = O(N2)
            fruit_dic = {} #sO(2)= O(1)
            for j in range(i, len(tree)):
                if tree[j] not in fruit_dic and len(fruit_dic) == 2:
                    new_sum_fruit = j - i
                    break
                elif tree[j] not in fruit_dic and len(fruit_dic) < 2:
                    fruit_dic[tree[j]] = 1
                    new_sum_fruit = j - i + 1
                elif tree[j] in fruit_dic:
                    fruit_dic[tree[j]] += 1
                    new_sum_fruit = j - i + 1
            res_fruit = max(res_fruit, new_sum_fruit) #tO(2) = tO(1)

        return res_fruit


'''
按块扫描法
思路:
方法：
边界条件：
time complex: 
space complex: 
易错点：
'''





'''
test case
'''
x = Solution()
x.totalFruit([0])