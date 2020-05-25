def check(subPath):  # check elem is pseudoPalindromic
    from collections import defaultdict
    dic = defaultdict(int)
    for elem in subPath:
        dic[elem] += 1
    oddNumb = 0
    for value in dic.values():
        if value % 2 == 1:
            oddNumb += 1
    if oddNumb <= 1:
        return True
    else:
        return False

print(check([2, 3, 1]))