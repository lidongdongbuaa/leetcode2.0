n = 5

for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = l + i - 1
        print((i,j))