from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = set()
        dishes = set()
        mem = {}

        for order in orders:
            tables.add(order[1])
            dishes.add(order[2])

            if order[1] not in mem:
                mem[order[1]] = {}

            if order[2] not in mem[order[1]]:
                mem[order[1]][order[2]] = 1
            else:
                mem[order[1]][order[2]] += 1
        tables = sorted(tables, key=lambda x: int(x))
        dishes = sorted(dishes)
        out = []
        tmp = ['Table']

        for dish in dishes:
            tmp.append(dish)
        out.append(tmp)

        for table in tables:
            tmp = [table]

            for dish in dishes:
                tmp.append(str(mem[table].get(dish, 0)))
            out.append(tmp)

        return out


sl = Solution()
orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"],
          ["David", "3", "Fried Chicken"], ["Carla", "5", "Water"],
          ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]
print(sl.displayTable(orders))
