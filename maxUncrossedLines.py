from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        table = [[0] * (len(nums2) + 1) for i in range(len(nums1) + 1)]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    table[i + 1][j + 1] = max(table[i][j] + 1, table[i + 1][j],
                                              table[i][j + 1])
                else:
                    table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
        # print(table)

        return table[len(nums1)][len(nums2)]


sl = Solution()
nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
nums1 = [2, 5, 1, 2, 5]
nums2 = [10, 5, 2, 1, 5, 2]
nums1 = [1, 3, 7, 1, 7, 5]
nums2 = [1, 9, 2, 5, 1]
print(sl.maxUncrossedLines(nums1, nums2))
