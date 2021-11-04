from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        tmp = 0

        for i in range(k):
            tmp += arr[i]
        out = 0

        if tmp >= target:
            out = 1

        for i in range(k, len(arr)):
            tmp = tmp + arr[i] - arr[i - k]

            if tmp >= target:
                out += 1

        return out


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(Solution().numOfSubarrays(arr, k, threshold))
