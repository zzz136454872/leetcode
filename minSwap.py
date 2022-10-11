from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        m0 = 0
        m1 = 1

        for i in range(1, len(nums1)):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                nm0 = m0
                nm1 = m1 + 1

                if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                    nm0 = min(nm0, m1)
                    nm1 = min(nm1, m0 + 1)
            else:
                nm0 = m1
                nm1 = m0 + 1
            m0 = nm0
            m1 = nm1

        return min(m0, m1)


# nums1 = [1, 3, 5, 4]
# nums2 = [1, 2, 3, 7]
# nums1 = [0, 3, 5, 8, 9]
# nums2 = [2, 1, 4, 6, 9]
# nums1=[3,3,8,9,10]
# nums2=[1,7,4,6,8]
nums1 = [0, 4, 4, 5, 9]
nums2 = [0, 1, 6, 8, 10]
print(Solution().minSwap(nums1, nums2))
