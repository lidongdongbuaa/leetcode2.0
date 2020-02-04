# 按照出现次数的多少进行排序
# value, times as key and val of dic
# make list of [value, times]
# sort list with list[1]
from jedi.evaluate.context import iterable

a = [1, 1, 2, 4, 5, 3, 5, 6, 7, 2, 1, 2, 3, 4, 5]


dic = {'a':15, 'e':13, 'd':45, 'b':10}
dic1 = sorted(dic.items(), key = lambda item: item[1])
print(dic1)