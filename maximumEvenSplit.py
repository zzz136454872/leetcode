from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        finalSum //= 2
        k = int(finalSum**0.5)
        s = k * (k + 1) // 2
        finalSum -= s

        while finalSum > k:
            k += 1
            finalSum -= k

        # print(finalSum,k)
        res = [2 * (1 + i) for i in range(k)]
        res[-1] += 2 * finalSum

        return res


finalSum = 12
finalSum = 7
finalSum = 28
print(Solution().maximumEvenSplit(finalSum))
