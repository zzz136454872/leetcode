from heapq import heappop, heappush
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int],
                       k: int) -> List[List[int]]:
        heap = []

        class Element:
            def __init__(self, idx1, idx2):
                self.idx1 = idx1
                self.idx2 = idx2

            def __lt__(self, other):
                return nums1[self.idx1] + nums2[self.idx2] < nums1[
                    other.idx1] + nums2[other.idx2]

        for i in range(min(len(nums1), k)):
            heappush(heap, Element(i, 0))
        out = []

        for i in range(k):
            if len(heap) == 0:
                break
            now = heappop(heap)
            out.append([nums1[now.idx1], nums2[now.idx2]])

            if now.idx2 < len(nums2) - 1:
                heappush(heap, Element(now.idx1, now.idx2 + 1))

        return out


nums1 = [1, 7, 11]
nums2 = [2, 4, 6]
k = 3
nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 2

nums1 = [1, 2]
nums2 = [3]
k = 3
print(Solution().kSmallestPairs(nums1, nums2, k))
