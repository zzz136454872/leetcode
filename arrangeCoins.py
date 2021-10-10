class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = 1234567

        while l <= r:
            mid = (l + r) // 2

            if n >= mid * (mid + 1) // 2:
                l = mid + 1
            else:
                r = mid - 1
            # print(l,r,mid)

        return l - 1


n = 3
print(Solution().arrangeCoins(n))
