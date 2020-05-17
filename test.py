class Solution:
    def arrangeWords(self, text: str) -> str:
        if len(text) == 1:
            return text

        sList = text.split(' ')
        sList.sort(key=lambda x: len(x))
        res = ' '.join(sList)
        res = res.capitalize()
        return res
X = Solution()
print(X.arrangeWords("Keep calm and code on"))