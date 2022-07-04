from heapq import heappop, heappush
from typing import List


# 不知道是哪个
class Solution1:
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


# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# # nums1 = [2, 4]
# # nums2 = [1, 2, 3, 4]
# print(Solution().nextGreaterElement(nums1, nums2))


# 556. 下一个更大元素 III
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))[::-1]
        i = 0
        thres = 2**31 - 1

        while i < len(s) - 1:
            if s[i] > s[i + 1]:
                j = 0

                while s[j] <= s[i + 1]:
                    j += 1
                s[j], s[i + 1] = s[i + 1], s[j]
                j = 0

                while j < i:
                    s[i], s[j] = s[j], s[i]
                    i -= 1
                    j += 1
                res = int(''.join(s[::-1]))

                if res <= thres:
                    return res
                else:
                    return -1
            i += 1

        return -1


n = 12
# n=21
print(Solution().nextGreaterElement(n))
