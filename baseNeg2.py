class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = []

        while n != 1:
            r = n & 1
            res.append(r)
            n -= r
            n //= -2
        res.append(1)

        return ''.join([str(a) for a in res[::-1]])


n = 2
n = 3
n = 4
print(Solution().baseNeg2(n))
