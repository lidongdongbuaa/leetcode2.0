class ProductOfNumbers:

    def __init__(self):
        self.A = [1]

    def add(self, a):
        if a == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * a)

    def getProduct(self, k):
        if k >= len(self.A): return 0
        return self.A[-1] / self.A[-k - 1]

obj = ProductOfNumbers()
obj.add(3)
obj.add(5)
obj.add(0)
param_2 = obj.getProduct(2)