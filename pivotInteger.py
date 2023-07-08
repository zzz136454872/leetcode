class Solution:
    def pivotInteger(self, n: int) -> int:
        l = n * (n + 1) // 2
        r = n
        t = n

        while l >= r:
            if l == r:
                return t
            l -= t
            t -= 1
            r += t

        return -1


n = 8
n = 1
n = 4
print(Solution().pivotInteger(n))
