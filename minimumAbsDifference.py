from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = 1234567

        for i in range(len(arr) - 1):
            diff = min(arr[i + 1] - arr[i], diff)
        res = []

        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == diff:
                res.append([arr[i], arr[i + 1]])
        res.sort()

        return res


arr = [4, 2, 1, 3]
arr = [1, 3, 6, 10, 15]
arr = [3, 8, -10, 23, 19, -4, -14, 27]
print(Solution().minimumAbsDifference(arr))
