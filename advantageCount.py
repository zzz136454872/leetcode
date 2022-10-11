from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = [(nums2[i], i) for i in range(len(nums2))]
        nums2.sort()
        nums1.sort()
        l1 = []
        l2 = []
        j = 0

        for i in range(len(nums1)):
            if nums1[i] > nums2[j][0]:
                l1.append(nums1[i])
                j += 1
            else:
                l2.append(nums1[i])
        nums1 = l1 + l2
        nums1 = [(nums2[i][1], nums1[i]) for i in range(len(nums1))]
        nums1.sort()

        return [x[1] for x in nums1]


nums1 = [2, 7, 11, 15]
nums2 = [1, 10, 4, 11]
nums1 = [12, 24, 8, 32]
nums2 = [13, 25, 32, 11]
nums1 = [2, 0, 4, 1, 2]
nums2 = [1, 3, 0, 0, 2]
print(Solution().advantageCount(nums1, nums2))
