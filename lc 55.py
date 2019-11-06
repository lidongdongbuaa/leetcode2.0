class Solution:
    def canJump(self, nums):
        find_index=[]
        for i in range(len(nums)):
            find_index.append(i+nums[i])
        jump=0
        max_index=0
        while jump<len(find_index)-1:
            for j in range(jump,find_index[jump]+1):
                if j<len(find_index)-1 and max_index<find_index[j]:
                    max_index=find_index[j]
                elif j < len(find_index)-1 and max_index>=find_index[j]:
                    continue
                elif j>=len(find_index)-1:
                    return True
            if find_index[j]==j:
                return False
            else:
                jump=j
        else:
            return True

x=Solution()
print (x.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))