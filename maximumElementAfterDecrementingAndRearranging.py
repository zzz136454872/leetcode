from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self,
                                                      arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1

        return arr[-1]


sl = Solution()
arr = [2, 2, 1, 2, 1]
arr = [100, 1, 1000]
arr = [1, 2, 3, 4, 5]
print(sl.maximumElementAfterDecrementingAndRearranging(arr))
