from typing import List


class Solution:
    def totalMoney(self, n: int) -> int:
        out = 0
        tmp = 1

        for i in range(n):
            out += tmp

            if i % 7 != 6:
                tmp += 1
            else:
                tmp -= 5

        return out


n = 4
n = 10
n = 20
print(Solution().totalMoney(n))
