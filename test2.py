
def peopleIndexes(favoriteCompanies):
    c = favoriteCompanies
    if len(c) == 1:
        return [0]

    dic = {tuple(val): index for index, val in enumerate(c)}
    res = [0] * len(c)
    c.sort(key=lambda x: len(x))
    sortC = c
    n = len(sortC)

    def check(l, r):
        for elem in l:
            if elem not in r:
                return False
        return True

    for i in range(n - 1):
        lenL = len(sortC[i])
        l  = sortC[i]
        for j in range(i + 1, n):
            r = sortC[j]
            if lenL < len(r) and check(l, r):
                res[dic[tuple(l)]] = 1

    return [i for i, val in enumerate(res) if val == 0]

print(peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))