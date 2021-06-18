import math


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        def sub(k, t):
            return (k**t - 1) // (k - 1)

        n = int(n)
        nMax = math.ceil(math.log2(n))
        nMin = 3

        for i in range(nMax, nMin - 1, -1):
            k = math.floor(n**(1 / (i - 1)))

            if k >= 2:
                if sub(k, i) == n:
                    return str(k)

        return str(n - 1)


sl = Solution()
n = '7'
print(sl.smallestGoodBase(n))
