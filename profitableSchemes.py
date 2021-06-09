from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int],
                          profit: List[int]) -> int:
        log = [[0] * (n + 1) for j in range(minProfit + 1)]

        for k in range(n + 1):
            log[0][k] = 1
        log[0][0] = 1
        mod = 10**9 + 7

        for i in range(len(group)):
            log_old = log
            log = [[0] * (n + 1) for j in range(minProfit + 1)]

            for k in range(n + 1):
                if k >= group[i]:
                    log[0][k] = (log_old[0][k] +
                                 log_old[0][k - group[i]]) % mod
                else:
                    log[0][k] = log_old[0][k]

            for j in range(1, minProfit + 1):
                for k in range(1, n + 1):
                    if k >= group[i]:
                        log[j][k] = (
                            log_old[j][k] +
                            log_old[j - profit[i] if j >= profit[i] else 0][
                                k - group[i]]) % mod
                    else:
                        log[j][k] = log_old[j][k]
            # print(log)

        return log[-1][-1]


sl = Solution()
n = 5
minProfit = 3
group = [2, 2]
profit = [2, 3]
n = 10
minProfit = 5
group = [2, 3, 5]
profit = [6, 7, 8]
print(sl.profitableSchemes(n, minProfit, group, profit))
