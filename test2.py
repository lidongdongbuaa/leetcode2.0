a = [1, 2, 3, 4, 5]
b = sorted(a, key=lambda x: x ** 2)
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key= lambda x:x[0], reverse=True)
print(b)
print(random)
