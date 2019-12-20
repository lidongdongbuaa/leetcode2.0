# merge sort 是先分割，再排序
# quick sort 是先排序，再分割

'''
讨论if i < j 和 i += 1 的作用:
仅不满足x < arr[j]时：
    if一定成立 - 有无都正常
    要寻找比x大的数，而i += 1存在时，直接跳过arr[i],这个等于arr[j]，且明显小于x的数
    而i += 1不存在时，重复 i += 1,再进行之后流程
    故有无 i+= 1都正常
仅不满足i<j时，即i=j了，ij重合:
    if 存在， i += 1存在
        arr[i] = arr[j] 和 i+=1 都不运行，整个程序运行结束，x赋给arr[i]
    if 存在， i += 1不存在
        arr[i] = arr[j] 不运行，整个程序运行结束，x赋给arr[i]
    if 不存在，i += 1存在
        arr[j]赋给arr[i],i = j，即arr[i]不变，i + 1，
        而下面的又进行了arr[j]赋给arr[i]，整个程序结束，x赋给arr[i+1]
        出错
    if 不存在，i += 1不存在
         arr[j]赋给arr[i],i = j，即arr[i]不变， 整个程序结束，x赋给arr[i]


故正确的是：
if 存在，i += 1存在
if 存在，i += 1不存在
if 不存在，i += 1不存在


'''

def AdjustArr(arr, l, r):  # return pivot position
    i = l
    j = r
    x = arr[i]  # 第一个坑
    while i < j:
        while i < j and x < arr[j]:  # find smaller val than x
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] < x:
            i += 1
        arr[j] = arr[i]
    arr[i] = x
    return i

def quicksort( arr, l, r):
    if l < r:
        i = AdjustArr(arr, l, r)
        quicksort(arr, l, i)
        quicksort(arr, i + 1,r)
    return arr

class Sort:
    def quicksort(self, arr, l, r):
        if len(arr) == 0 or len(arr) == 1:
            return arr

        if l < r:
            i = l
            j = r
            pivot = arr[i]
            while i < j:
                while i < j and pivot <= arr[j]:
                    j -= 1
                arr[i] = arr[j]
                while i < j and arr[i] <= pivot:
                    i += 1
                arr[j] = arr[i]
            arr[i] = pivot
            self.quicksort(arr, l, i)
            self.quicksort(arr, i + 1, r)
        return arr

# print(quicksort([9,8,7,6,5,4,3,2,1,0], 0, 9))


class Solution:
    def quicksort(self, arr, l, r):
        if len(arr) == 0 or len(arr) == 1:
            return arr

        if l < r:
            i = l
            j = r
            pivot = arr[i]
            while i < j:
                while i < j and pivot <= arr[j]:
                    j -= 1
                arr[i] = arr[j]
                while i < j and arr[i] <= pivot:
                    i += 1
                arr[j] = arr[i]
            arr[i] = pivot
            self.quicksort(arr, l, i)
            self.quicksort(arr, i + 1, r)
        return arr

    def sortArray(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return nums

        l = 0
        r = len(nums) - 1
        return self.quicksort(nums, l, r)

x = Solution()
print(x.sortArray([5,1,1,2,0,0]))
