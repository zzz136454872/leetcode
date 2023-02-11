from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()

        if amount[0] + amount[1] <= amount[2]:
            return amount[2]

        return (sum(amount) + 1) // 2


amount = [1, 4, 2]
amount = [5, 4, 4]
amount = [5, 0, 0]
print(Solution().fillCups(amount))
