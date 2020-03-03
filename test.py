class SortList:
    def mergeSort(self, arr):  # Merge sort by bottom-up merge sort
        if len(arr) == 0 or len(arr) == 1:  # edge case
            return arr

        length = len(arr)
        interval = 1
        while interval < length:
            for i in range(0, length, 2 * interval):  # bottom-up merge sort
                arr[i: i + 2 * interval] = self.subsort(arr[i: i + interval], arr[i + interval: i + interval * 2])
            interval = interval * 2
        return arr

    def subsort(self, list1, list2):  # sort two sorted list
        if not list1:
            return list2
        if not list2:
            return list1

        new_list = []
        left_len = len(list1)
        right_len = len(list2)
        i, j = 0, 0
        while i < left_len and j < right_len:
            if list1[i] < list2[j]:
                new_list.append(list1[i])
                i += 1
            else:
                new_list.append(list2[j])
                j += 1

        if i != left_len:
            new_list.extend(list1[i:])
        if j != right_len:
            new_list.extend(list2[j:])
        return new_list

x = SortList()
x.mergeSort([4,3,2,1,0])