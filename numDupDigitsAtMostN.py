from math import perm


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        limit = list(map(int, str(n + 1)))
        s = set()
        k = len(limit)
        res = sum(9 * perm(9, i) for i in range(k - 1))

        for i in range(len(limit)):
            x = limit[i]

            if i == 0:
                for y in range(1, x):
                    res += perm(9, k - 1)
            else:
                for y in range(x):
                    if y not in s:
                        res += perm(9 - i, k - i - 1)

            if x in s:
                break
            s.add(x)

        return n - res


n = 100
n = 1000
n = 20
print(Solution().numDupDigitsAtMostN(n))
