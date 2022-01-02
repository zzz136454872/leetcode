from typing import *


def ysf(n, m):
    if n == 1:
        return 0
    else:
        return (ysf(n - 1, m) + m) % n


class Solution1:
    def lastRemaining(self, n: int, m: int) -> int:
        return ysf(n, m)


# 消除游戏
class Solution:
    def lastRemaining(self, n: int) -> int:
        r = 0
        count = n
        a0 = 1
        step = 1

        while count > 1:
            print(r, count, step, a0)

            if r % 2 == 0:
                a0 += step
            else:
                if count % 2 != 0:
                    a0 += step
            step *= 2
            count = count // 2
            r += 1

        return a0


n = 9
n = 1
print(Solution().lastRemaining(n))
