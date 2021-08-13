class Solution:
    def countDigitOne(self, n: int) -> int:
        base = 1
        out = 0

        while n >= base:
            out += n // (base * 10) * base + min(
                max(n % (base * 10) - base + 1, 0), base)
            base *= 10

        return out


sl = Solution()
n = 10
n = 13
n = 1
print(sl.countDigitOne(n))
