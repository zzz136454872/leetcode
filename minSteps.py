class Solution:
    def minSteps(self, n: int) -> int:
        out = 0
        i = 2

        while n != 1:
            if n % i == 0:
                n = n // i
                out += i
            else:
                i += 1

        return out


sl = Solution()
print(sl.minSteps(3))
