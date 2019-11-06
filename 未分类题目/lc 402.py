class Solution:
    def removeKdigits(self, num, k):
        if len(num) == 0:
            return num
        elif len(num) == 1:
            if k == 0:
                return num
            elif k == 1:
                return '0'
        elif len(num) >= 2:
            stack = []
            stack.append(num[0])
            n = 0
            for i in range(1, len(num)):
                while  int(stack[-1]) > int(num[i]) and n < k:
                    stack.pop()
                    n = n + 1
                stack.append(num[i])

            if n < k:
                x = k - n
                for i in range(x):
                    stack.pop()
            if len(stack) == 0:
                return '0'
            result = ''
            for elem in stack:
                result = result + elem
            intresult = int(result)
            return str(intresult)

x=Solution()
x.removeKdigits("1432219",3)