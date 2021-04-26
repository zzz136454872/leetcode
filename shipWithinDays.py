from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def countDay(cap):
            day = 1
            nowWeight = 0

            for weight in weights:
                if weight + nowWeight <= cap:
                    nowWeight += weight
                else:
                    day += 1
                    nowWeight = weight

            return day

        minWeight = max(weights)
        maxWeight = 500 * 50000

        while minWeight <= maxWeight:
            mid = (minWeight + maxWeight) // 2
            days = countDay(mid)

            if days <= D:
                maxWeight = mid - 1
            else:
                minWeight = mid + 1

        return minWeight


sl = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D = 5
weights = [3, 2, 2, 4, 1, 4]
D = 3
weights = [1, 2, 3, 1, 1]
D = 4
print(sl.shipWithinDays(weights, D))
