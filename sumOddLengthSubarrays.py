from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        preSum = [0]
        s = 0

        for num in arr:
            s += num
            preSum.append(s)
        out = 0
        n = len(arr)

        for i in range(n):
            print(i, i // 2, (n - i + 1) // 2)
            out += (i + 2) // 2 * preSum[i + 1] - (n + 1 - i) // 2 * preSum[i]

        return out


sl = Solution()
arr = [1, 4, 2, 5, 3]
print(sl.sumOddLengthSubarrays(arr))
