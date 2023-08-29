from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        res = [1] * n
        mod = 10**9 + 7

        for i in range(1, n):
            k = i - 1

            for j in range(i):
                while k > 0 and arr[j] * arr[k] > arr[i]:
                    k -= 1

                if j > k:
                    break

                if arr[j] * arr[k] == arr[i]:
                    if j != k:
                        res[i] = (res[i] + 2 * res[j] * res[k]) % mod
                    else:
                        res[i] = (res[i] + res[j] * res[k]) % mod

        return sum(res) % mod


arr = [2, 4]
arr = [2, 4, 5, 10]
print(Solution().numFactoredBinaryTrees(arr))
