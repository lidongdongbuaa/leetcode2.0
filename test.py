# a >> i & 1 谁的优先级高
res = 0
mask = 1
for _ in range(n):
    res = res | mask
    mask = mask << 1