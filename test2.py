'''
易错点：
    1. arr[i + 1:r + 1]：右端点到r+1，而不是r，也不是到j
    2. pivot 与 arr[i/j]的判断，用的是while，因为需要扫描搜索一段
    3.while i <j and pivot < arr[j], i < j 时刻不要忘记，pivot < arr[j]是符合大小排序的比较关系，若不成立，则跳出，变换值
'''
class Solution:
    def quickSort(self, arr):
        if len(arr) == 0 or len(arr) == 1:  # corner case
            return arr

        i = l = 0
        j = r = len(arr) - 1
        pivot = arr[i]

        while i < j:
            while i < j and pivot < arr[j]:  # 扫描一段去寻找合适的值, 循环条件是正常的顺序（pivot < arr[j]），若发现异常，则跳出更换i和j
                j -= 1
            arr[i] = arr[j]  # 搜寻一段之后，找到值，再替换
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]
        arr[i] = pivot  # i in center, give it pivot
        arr[0:i] = self.quickSort(arr[0:i])  # L part = arr[0:i] < pivot
        arr[i + 1:r + 1] = self.quickSort(arr[i + 1:r + 1])  # R part = arr[i + 1, j] > pivot
        return arr


X = Solution()

print(X.quickSort([9, 8, 7, 6, 5, 4, 4, 3, 2, 1]))
