from collections import defaultdict


class Solution:
    def displayTable(self, orders):
        food = []
        table = []
        for elem in orders:
            if elem[2] not in food:
                food.append(elem[2])
            if elem[1] not in table:
                table.append(elem[1])

        food.sort()
        table.sort(key = lambda x : int(x))

        res = []
        res.append(['Table'] + food)

        for elem in table:
            row = []
            row.append(elem)
            row.extend(['0' for _ in range(len(food))])
            for menu in orders:
                if elem == menu[1]:
                    ind = food.index(menu[2])
                    row[ind + 1] = str(int(row[ind + 1]) + 1)
            res.append(row)
        return res


x = Solution()
print(x.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))