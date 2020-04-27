class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:  # corner case
            return ''

        res = s + '0'
        n = len(s)
        l = r = 0

        dicT = {}
        for elem in t:
            if elem in dicT:
                dicT[elem] += 1
            else:
                dicT[elem] = 1

        def judge(subS):  # judege T in subS
            dicS = {}
            for elem in subS:
                if elem in dicS:
                    dicS[elem] += 1
                else:
                    dicS[elem] = 1
            for key, val in dicT.items():
                if key not in dicS:
                    return False
                else:
                    if dicS[key] < val:
                        return False
            return True

        for r in range(n):
            subS = s[l:r + 1]
            while judge(subS):
                if len(subS) < len(res):
                    res = subS
                l += 1
                subS = s[l:r + 1]
        return res if res != (s + '0') else ''

X = Solution()
print(X.minWindow("ADOBECODEBANC", "ABC"))