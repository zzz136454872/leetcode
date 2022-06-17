from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        j = 0
        i = 0
        n = len(arr)

        while i < n:
            if arr[i] == 0:
                j += 1
            i += 1
            j += 1

            if j >= n:
                break
        i -= 1
        j -= 1

        if j == n:
            i -= 1
            j -= 2
            arr[-1] = 0

        while i >= 0:
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
            arr[j] = arr[i]
            i -= 1
            j -= 1


arr = [1, 0]
arr = [1, 2, 3]
print(Solution().duplicateZeros(arr))
print(arr)
