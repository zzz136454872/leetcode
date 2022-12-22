from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True


arr = [3, 5, 1]
arr = [1, 2, 4]
print(Solution().canMakeArithmeticProgression(arr))
