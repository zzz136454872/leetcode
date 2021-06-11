from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        mem = [[-1] * (amount + 1) for i in range(len(coins))]

        def count(loc, amount_now):
            if loc == len(coins):
                if amount_now == 0:
                    return 1

                return 0

            if mem[loc][amount_now] != -1:
                return mem[loc][amount_now]
            out = 0
            a = amount_now

            while a >= 0:
                out += count(loc + 1, a)
                a -= coins[loc]

            mem[loc][amount_now] = out

            return out

        return count(0, amount)


sl = Solution()
amount = 5
coins = [1, 2, 5]
# amount = 3
# coins = [2]
# amount = 10
# coins = [10]
print(sl.change(amount, coins))
