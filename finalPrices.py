from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = prices.copy()
        stack = []

        for i in range(len(prices) - 1, -1, -1):

            while len(stack) > 0 and stack[-1] > prices[i]:
                stack.pop()

            if len(stack) > 0:
                res[i] -= stack[-1]
            stack.append(prices[i])

        return res
