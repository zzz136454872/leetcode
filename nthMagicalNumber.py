class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        l = min(a, b)
        r = n * max(a, b)

        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a % b)

        ab = a * b // gcd(a, b)

        while l <= r:
            mid = (l + r) // 2
            c = mid // a + mid // b - mid // (ab)

            if c >= n:
                r = mid - 1
            else:
                l = mid + 1

        return l % (10**9 + 7)


n = 1
a = 2
b = 3
n = 4
a = 2
b = 4
print(Solution().nthMagicalNumber(n, a, b))
