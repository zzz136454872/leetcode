from typing import List


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        mk = max(vat)

        if mk == 0:
            return 0
        res = 12345678

        for k in range(1, mk + 1):
            t = 0

            for i in range(len(bucket)):
                t += max(0, (vat[i] + k - 1) // k - bucket[i])
            res = min(res, t + k)

        return res


bucket = [9, 0, 1]
vat = [0, 2, 2]
bucket = [1, 3]
vat = [6, 8]
print(Solution().storeWater(bucket, vat))
