class Solution:
    def letterCombinations(self, digits: str):
        tag = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i']}

        strList = [tag[elem] for elem in digits]

        m = len(digits)

        def backtrack(start, path):  # save all combinations in res
            # if start == m:
            #     res.append(path[:])
            #     return 
            if start > m - 1:
                return

            for i in range(len(strList[start])):
                path.append(strList[start][i])
                if len(path) == m:
                    res.append(path[:])

                backtrack(start + 1, path)
                path.pop()

        res = []
        backtrack(0, [])
        res = [''.join(elem) for elem in res]
        return res

x = Solution()
print(x.letterCombinations("23"))