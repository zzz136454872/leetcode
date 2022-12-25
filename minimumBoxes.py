class Solution:
    def minimumBoxes(self, n: int) -> int:
        l = 1
        r = 10000

        while l <= r:
            mid = (l + r) // 2
            t = mid * (mid + 1) * (mid + 2) // 6

            if n <= t:
                r = mid - 1
            else:
                l = mid + 1
        l -= 1
        n -= l * (l + 1) * (l + 2) // 6
        j = 0

        while n > 0:
            j += 1
            n -= j

        return l * (l + 1) // 2 + j


n = 1
n = 3
n = 4
n = 10
n = 15
n = 51

print(Solution().minimumBoxes(n))
