from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        heap = []
        mem = Counter(barcodes)

        for k, v in mem.items():
            heappush(heap, [-v, k])

        res = []

        while len(heap) > 0:
            now1 = heappop(heap)

            if len(res) > 0 and res[-1] == now1[1]:
                now2 = heappop(heap)
                heappush(heap, now1)
                now1 = now2
            res.append(now1[1])
            now1[0] += 1

            if now1[0] < 0:
                heappush(heap, now1)

        return res


barcodes = [1, 1, 1, 2, 2, 2]
barcodes = [1, 1, 1, 1, 2, 2, 3, 3]
print(Solution().rearrangeBarcodes(barcodes))
