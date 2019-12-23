class sortArr:
    def sortPN(self, arr):  # put the negative front fo positive value
        if len(arr) == 0 or len(arr) == 1:  # edge case
            return arr

        i = 0
        j = len(arr) - 1
        pivot = arr[i]
        while i < j:
            while i < j and arr[j] >= 0:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] < 0:
                i += 1
            arr[j] = arr[i]
        arr[i] = pivot
        return arr


x = sortArr()
print(x.sortPN([9, 8, 7, 4, 5, -1, -2, -3]))