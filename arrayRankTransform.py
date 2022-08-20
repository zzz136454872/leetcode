from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        arr = [[i, arr[i], 0] for i in range(len(arr))]
        arr.sort(key=lambda x: x[1])
        arr[0][2] = 1

        for i in range(1, len(arr)):
            if arr[i][1] > arr[i - 1][1]:
                arr[i][2] = arr[i - 1][2] + 1
            else:
                arr[i][2] = arr[i - 1][2]
        arr.sort()

        return [x[2] for x in arr]


arr = [40, 10, 20, 30]
arr = [100, 100, 100]
print(Solution().arrayRankTransform(arr))
