from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = min(brackets[0][0], income) * brackets[0][1]

        for i in range(1, len(brackets)):
            if brackets[i - 1][0] >= income:
                break
            res += (min(brackets[i][0], income) -
                    brackets[i - 1][0]) * brackets[i][1]

        res += (income - min(brackets[-1][0], income)) * brackets[-1][1]

        return res / 100


brackets = [[3, 50], [7, 10], [12, 25]]
income = 10
brackets = [[1, 0], [4, 25], [5, 50]]
income = 2
brackets = [[2, 50]]
income = 0
print(Solution().calculateTax(brackets, income))
