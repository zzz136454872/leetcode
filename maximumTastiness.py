from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l = 0
        r = price[-1]
        big = 1234567890

        while l <= r:
            mid = (l + r) // 2
            prev = -big
            get = 0

            for p in price:
                if p - prev >= mid:
                    get += 1
                    prev = p

                    if get >= k:
                        break

            if get >= k:
                l = mid + 1
            else:
                r = mid - 1

        return r


price = [13, 5, 1, 8, 21, 2]
k = 3
price = [1, 3, 1]
k = 2
price = [7, 7, 7, 7]
k = 2
print(Solution().maximumTastiness(price, k))
