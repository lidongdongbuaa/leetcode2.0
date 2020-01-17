# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 19:30
# @Author  : LI Dongdong
# @FileName: 29. Divide Two Integers.py
''''''
'''
题目分析
1.要求：Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
    Return the quotient after dividing dividend by divisor.
    The integer division should truncate toward zero.
    
    Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    
    Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    
    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
    For the purpose of this problem, assume that your function returns 2**31 − 1 when the division result overflows.
2.理解：不用乘除mod计算商
3.类型：bit 除法
4.确认输入输出及边界条件：
    输入： dividend: int, divisor: int，not 0
    输出：int。quotient, if <0, truncate toward zero.
    corner case: 
        input: dividend is 0
        over [−2**31,  2**31 − 1].division result overflow: 2**31 − 1
    解释：题目中要求我们不能用乘法和除法，但是我们可以用减法，我们可以通过被除数最多可以减多少个除数还能保证是非负来得到商。
    dividend=quotient∗divisor+remainder
    不过这样在某些情况会超时（比如 2**30/1），为了解决效率问题，可以减去除数的倍数，利用位运算，每次除数左移一位（2 倍），次数相应加对应的倍数。然后再判断当前的和是否大于被除数，如果大于的话，再把除数回置（右移）
4.方法及方法分析：
time complexity order: 
space complexity order: 
'''
'''
A.
思路：use reduce, find the number of reduction of divisor
方法：
    1. find plus and minus of result, abs of dividend, divisor  tO(1) sO(1)
    2. continue to reduce the divisor, count quotient tO(k/m) sO(1)
        try multiply divisor to reduce time
time complex: tO(1)
space complex: sO(1)
易错点：
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:  # corner case
            return 0

        negative_sign = (dividend > 0) ^ (divisor >0)  # res sign
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        count = 0
        left = 0
        while left >= 0:  # calculate range of quotient
            # 除数加倍直到超过剩余的被除数
            quotient += (1 << count)
            left = dividend - (divisor << count)
            count += 1
        count -= 1

        # while dividend - (divisor << count) >= 0:
        #     quotient += (1 << count)
        #     dividend -= (divisor << count)
        #     count += 1

        while count > 0:  # 除数减半直到count=0
            if dividend - (divisor << count) >= 0:
                quotient += (1 << count)
                dividend -= (divisor << count)
            count -= 1

        # while count > 0:  # 除数减半直到count=0
        #     count -= 1
        #     if dividend - (divisor << count) >= 0:
        #         quotient += (1 << count)
        #         dividend -= (divisor << count)

        if negative_sign:
            quotient = - quotient

        if quotient > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if quotient < - 2 ** 31:
            return 2 ** 31 - 1

        return quotient

x = Solution()
print(x.divide(7, -3))


