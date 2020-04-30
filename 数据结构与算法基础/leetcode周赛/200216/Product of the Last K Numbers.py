#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 11:58
# @Author  : LI Dongdong
# @FileName: Product of the Last K Numbers.py
''''''
'''
题目分析
1.要求：
    Implement the class ProductOfNumbers that supports two methods:
    
    1. add(int num)
    
    Adds the number num to the back of the current list of numbers.
    2. getProduct(int k)
    
    Returns the product of the last k numbers in the current list.
    You can assume that always the current list has at least k numbers.
    At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

    Example:
    
    Input
    ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
    [[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]
    
    Output
    [null,null,null,null,null,null,20,40,0,null,32]
    
    Explanation
    ProductOfNumbers productOfNumbers = new ProductOfNumbers();
    productOfNumbers.add(3);        // [3]
    productOfNumbers.add(0);        // [3,0]
    productOfNumbers.add(2);        // [3,0,2]
    productOfNumbers.add(5);        // [3,0,2,5]
    productOfNumbers.add(4);        // [3,0,2,5,4]
    productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
    productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
    productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
    productOfNumbers.add(8);        // [3,0,2,5,4,8]
    productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 

2.理解：desing a add number and calculate last k production program
3.类型： system design
4.确认输入输出及边界条件：
    input: numbers, repeated? Y order? N value range? 0 <= num <= 100, operation times? <= 4000
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
超时
思路：system - stack
方法：
    initial - build a stack
    add - use stack to add numbers
    getProduct - get last[k], multiply them
time complex: add - O(1) getP O(K)
space complex: add - O(1) getP (1)
易错点：
    起始的res是1，不是0！
    本方法超时
'''


class ProductOfNumbers:

    def __init__(self):
        self.stack = []  # use stack to store value

    def add(self, num: int) -> None:
        self.stack.append(num)


    def getProduct(self, k: int) -> int:
        res = 1
        for elem in self.stack[-k:]:
            res = elem * res
        return res

# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(5)
param_2 = obj.getProduct(2)

'''

思路：system - stack + prefix product
方法：
    initial - build a stack
    add -  a = 1,1,0,2,2 -> A: 1,2,4
    getProduct - 0 in stack[-k:] judgement 
time complex: add - O(1) getP O(newK - oldK)
space complex: add - O(1) getP (1)
易错点：
'''


class ProductOfNumbers:

    def __init__(self):
        self.A = [1]

    def add(self, a): # save product of a, e.g. after first a, A=[1, a]
        if a == 0:  # meet 0， A = [1], restart t0 deal with 0
            self.A = [1]
        else:
            self.A.append(self.A[-1] * a)

    def getProduct(self, k):
        if k >= len(self.A):  # k reach to the 0 area
            return 0
        else:   # normal case
            return self.A[-1] / self.A[-k - 1]

obj = ProductOfNumbers()
obj.add(3)
obj.add(5)
param_2 = obj.getProduct(2)