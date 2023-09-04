class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost2, cost1 = cost1, cost2
        res = total // cost1 + 1

        while total >= 0:
            res += total // cost2
            total -= cost1

        return res


total = 20
cost1 = 10
cost2 = 5
print(Solution().waysToBuyPensPencils(total, cost1, cost2))
