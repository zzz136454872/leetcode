class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        k -= n
        t = k // 25
        r = k - 25 * t

        if r == 0:
            return 'a' * (n - t) + 'z' * t

        return 'a' * (n - 1 - t) + chr(ord('a') + r) + 'z' * t


n = 3
k = 27
n = 5
k = 73
n = 24
k = 552
n = 5
k = 130

print(Solution().getSmallestString(n, k))
