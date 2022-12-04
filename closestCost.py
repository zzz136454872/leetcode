from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int],
                    target: int) -> int:
        mem = set(baseCosts)

        for t in toppingCosts:
            new = []

            for c in mem:
                if c >= target:
                    continue

                if c + t not in mem:
                    new.append(c + t)

                    if c + t >= target:
                        continue

                if c + 2 * t not in mem:
                    new.append(c + 2 * t)

            for v in new:
                mem.add(v)

        mem = sorted(list(mem))
        res = 0
        diff = 12345678

        for v in mem:
            if abs(target - v) < diff:
                res = v
                diff = target - v

        return res


baseCosts = [1, 7]
toppingCosts = [3, 4]
target = 10

baseCosts = [2, 3]
toppingCosts = [4, 5, 100]
target = 18

baseCosts = [10]
toppingCosts = [1]
target = 1
print(Solution().closestCost(baseCosts, toppingCosts, target))
