class Merge:
    def mergeArr(self, arr):  # input: list[list], k, n, merge all sorted list
        if len(arr) == 0:  # edge case
            return
        if len(arr) == 1:
            return arr[0]

        length = len(arr)  # divide into groups
        mid = length // 2
        L = arr[:mid]
        R = arr[mid:]

        self.mergeArr(L)  # merge to left
        self.mergeArr(R)  # merge to right

        i = j = k = 0
        while i < len(L[0]) and j < len(R[0]):  # merge left and right
            if L[0][i] < R[0][j]:
                arr[k] = L[i]
                k += 1
                i += 1

            else:
                arr[k] = R[j]
                k += 1
                j += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1


        return arr

x = Merge()
print(x.mergeArr([[1, 5, 9], [2, 4, 7],[3, 8, 9]]))