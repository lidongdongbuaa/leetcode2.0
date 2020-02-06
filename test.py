
# Function to do insertion sort
# def insertionSort(arr):
#     if len(arr) == 1:
#         return arr
#
#     for i in range(len(arr) - 1):
#         basic = arr[:i + 1]
#         compare = arr[i + 1]
#         for j in range(len(basic) - 1, -1, -1):
#             if j != 0 and basic[j - 1] <= compare < basic[j]:  # or arr[j]
#                 arr[j:i + 2] = [compare] + basic[j:]
#                 break
#             elif j == 0 and compare < basic[j]:
#                 arr[:i + 2] = [compare] + basic
#                 break
#     return arr

def insertionSort(arr):
    if len(arr) == 1:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :  # 此时key = arr[j + 1]
            arr[j], arr[j + 1]= key, arr[j]
            j -= 1
    return arr

a = [5,11,3,2,1]
print(insertionSort(a))