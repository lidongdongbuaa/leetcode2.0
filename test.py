class Solution:
    def reverseBits(self, n: int) -> int:
        if n == None:
            return None

        string = bin(n)[2:].zfill(32)
        reverse_string = string[::-1]
        return int(reverse_string, 2)

x = Solution()
print(x.reverseBits(5))