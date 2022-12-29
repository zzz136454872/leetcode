from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int],
                      nums3: List[int]) -> List[int]:
        c1 = set(nums1)
        c2 = set(nums2)
        c3 = set(nums3)

        return list(c1 & c2 | c1 & c3 | c2 & c3)


nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]
nums1 = [3, 1]
nums2 = [2, 3]
nums3 = [1, 2]
print(Solution().twoOutOfThree(nums1, nums2, nums3))
