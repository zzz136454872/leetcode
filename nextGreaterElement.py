from heapq import heappop, heappush
from typing import List


class Solution:
    # 第一种解法
    def nextGreaterElement(self, nums1: List[int],
                           nums2: List[int]) -> List[int]:
        stack = []
        log = {}

        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                log[stack.pop()] = num
            stack.append(num)

        for num in stack:
            log[num] = -1
        out = []

        for num in nums1:
            out.append(log[num])

        return out

    # 第二种解法
    def nextGreaterElement1(self, nums1: List[int],
                            nums2: List[int]) -> List[int]:
        heap = []
        log = {}

        for num in nums2:
            while len(heap) > 0 and heap[0] < num:
                log[heap[0]] = num
                heappop(heap)
            heappush(heap, num)

        for num in heap:
            log[num] = -1
        out = []

        for num in nums1:
            out.append(log[num])

        return out


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
# nums1 = [2, 4]
# nums2 = [1, 2, 3, 4]
print(Solution().nextGreaterElement(nums1, nums2))
