class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:  # only one elem string
            return 0

        numb_list = []
        temp = s[0]
        numb = 1
        for i in range(1, len(s)):  # accumulate elems repeat times
            if temp is s[i]:
                numb += 1
            else:
                numb_list.append(numb)
                numb = 1
                temp = s[i]
        numb_list.append(numb)

        ans = 0
        for i in range(len(numb_list) - 1):
            ans = ans + min(numb_list[i], numb_list[i+1])

        return ans

'''
test case
'''
x = Solution()
x.countBinarySubstrings("100101")