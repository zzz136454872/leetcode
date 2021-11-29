from heapq import heappop, heappush
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)

        for i in range(n - 1):
            for j in range(i + 1, n):
                tmp = -arr[i] / arr[j]

                if len(heap) == k:
                    if tmp > heap[0][0]:
                        heappop(heap)
                        heappush(heap, (tmp, arr[i], arr[j]))
                else:
                    heappush(heap, (tmp, arr[i], arr[j]))
                # print(i,j,heap)

        return [heap[0][1], heap[0][2]]


arr = [1, 2, 3, 5]
k = 3
print(Solution().kthSmallestPrimeFraction(arr, k))
