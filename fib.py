from typing import *


# 斐波那契数列
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        log = [0 for i in range(n + 1)]
        log[0] = 0
        log[1] = 1

        for i in range(2, n + 1):
            log[i] = log[i - 1] + log[i - 2]

        return log[n]


# 斐波那契数列 with a mod
class Solution:
    def fib(self, n: int) -> int:
        mod = 10**9 + 7

        if n <= 1:
            return n
        now = 1
        pre = 0

        for i in range(n - 1):
            now, pre = (now + pre) % mod, now

        return now


n = 2
n = 5
print(Solution().fib(n))
