from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        mem = set(arr)

        res = 0

        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                a = arr[i]
                b = arr[j]
                cnt = 2

                while a + b in mem:
                    a, b = b, a + b
                    cnt += 1

                if cnt > 2:
                    res = max(res, cnt)

        return res


arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr = [1, 3, 7, 11, 12, 14, 18]
arr = [1, 3, 5]
print(Solution().lenLongestFibSubseq(arr))
