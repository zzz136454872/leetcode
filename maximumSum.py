from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        d0 = arr[0]
        d1 = arr[0]
        res = arr[0]

        for num in arr[1:]:
            d1 = max(d1 + num, d0)
            d0 = max(d0 + num, num)
            res = max(d0, d1, res)
            # print(num,d0,d1,res)

        return res


arr = [1, -2, 0, 3]
arr = [1, -2, -2, 3]
arr = [-1, -1, -1, -1]
print(Solution().maximumSum(arr))
