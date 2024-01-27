from typing import List


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int,
                          composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:

        res = 0

        for c in composition:
            left = 0
            right = 10**10 + 1

            while left <= right:
                need = 0
                mid = (left + right) // 2

                for i in range(n):
                    want = mid * c[i] - stock[i]

                    if want > 0:
                        need += want * cost[i]

                if need > budget:
                    right = mid - 1
                else:
                    left = mid + 1
            res = max(res, right)

        return res


n = 3
k = 2
budget = 15
composition = [[1, 1, 1], [1, 1, 10]]
stock = [0, 0, 0]
cost = [1, 2, 3]

n = 3
k = 2
budget = 15
composition = [[1, 1, 1], [1, 1, 10]]
stock = [0, 0, 100]
cost = [1, 2, 3]
print(Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost))
