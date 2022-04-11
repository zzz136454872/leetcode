class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def csub(n):
            if n == 0:
                return 1
            elif n == 1:
                return 9
            out = 9

            for i in range(n - 1):
                out *= (9 - i)

            return out

        out = 0

        for i in range(n + 1):
            out += csub(i)

        return out

n = 1
n = 0
n = 2
print(Solution().countNumbersWithUniqueDigits(n))
