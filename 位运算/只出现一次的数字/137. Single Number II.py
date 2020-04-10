#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 7:56
# @Author  : LI Dongdong
# @FileName: 137. Single Number II.py
''''''
'''
题目分析
1.要求：Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
    Input: [2,2,3,2]
    Output: 3
2.理解：非空list，一个值出现了一次，其余的都出现三次，求出现一次的值。tO(N), sO(1)
3.类型：bit manipulation
4.确认输入输出及边界条件：
    input: list, repeat？ Y order? N
    output: value int
    corner case:
        input： None？ N Only one? No
4.方法及方法分析：dic store, XOR 
time complexity order: dic store O(N) = XOR O(N)
space complexity order: XOR(1) < dic storeO(N)
'''
'''
A.
思路：brute force - dic store
方法：
    1. scan list, store value and time in dic's key and value
    2. output 1 value's key
time complex: O(N)
space complex: O(N)
易错点：for k, v in dic.items(): 从value查key
'''
class Solution:
    def singleNumber(self, nums) -> int:
        dic = {}
        for elem in nums:   # store value, times in dic
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1

        for k, v in dic.items():  # output 1 times key
            if v == 1:
                return k
        return 0

'''
B.
优点：技巧性太强
思路：bit manipulation
方法：
    设计如下的状态机去处理三次数值
	            a	b	
    初始状态：	0	0	
    第一次碰见某个数 x：	0	x	把 x 记录在 b 中
    第二次碰见某个数 x：	x	0	把 x 记录在 a 中
    第三次碰见某个数 x：	0	0	把 a 和 b 都清空，可以处理其他数
    我们按照上述变换规则设计 a 和 b：
    b=0 时碰到 x，就变成 x；b=x 时再碰到 x，就变成 0，这个就是异或，我们也许可以设计 b=b xor x。当 b 再次碰到 x，这时候 b 还是要为 0，但这时候不同的是 a=x，而前两种情况都是 a=0。所以我们可以设计成 b=(b xor x)&~a
    同样道理，我们可以设计出：a=(a xor x)&~b
    按照这个设计，最后那个只出现一次的元素必定存储在 b 中。
time complex: O(N)
space complex: O(1)
易错点：0 和一个数异或后得到那个数，两个相同的数异或后则为 0。
'''
class Solution:
    def singleNumber(self, nums) -> int:
        a = 0
        b = 0
        for elem in nums:
            b = (b ^ elem) & ~a
            a = (a ^ elem) & ~b
        return b