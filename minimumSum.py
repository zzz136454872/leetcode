class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        t = k // 2

        if t >= n:
            return (1 + n) * n // 2
        else:
            return (t + 1) * t // 2 + (n - t) * (2 * k + n - t - 1) // 2


n = 5
k = 4
n = 2
k = 6
print(Solution().minimumSum(n, k))
