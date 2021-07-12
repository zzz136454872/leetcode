from typing import List


# H指数
class Solution1:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i

        return len(citations)


# H指数II
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        n = len(citations)
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if n - mid > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return n - left


sl = Solution()
citations = [100, 100, 5]
citations = [0, 1, 3, 5, 6]
print(sl.hIndex(citations))
