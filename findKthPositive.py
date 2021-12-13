from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        idx = 0

        for i in range(1, 2001):
            if idx < len(arr) and i == arr[idx]:
                idx += 1
            else:
                k -= 1

                if k == 0:
                    return i

        return -1


arr = [2, 3, 4, 7, 11]
k = 5
arr = [1, 2, 3, 4]
k = 2
print(Solution().findKthPositive(arr, k))
