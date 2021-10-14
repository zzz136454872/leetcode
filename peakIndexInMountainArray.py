from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] > arr[mid + 1]:
                right = mid
            elif arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                left += 1

        return left


arr = [-1, 1, 0]
arr = [1, 3, 5, 4, 2]
arr = [0, 10, 5, 2]
arr = [3, 4, 5, 1]
arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
print(Solution().peakIndexInMountainArray(arr))
