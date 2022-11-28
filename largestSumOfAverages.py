from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        mem = {}
        presum = [0]
        tmp = 0

        for num in nums:
            tmp += num
            presum.append(tmp)

        def find(start, end, kk):
            if kk > end - start + 1:
                return -12345678

            if kk == 1:
                return (presum[end + 1] - presum[start]) / (end - start + 1)
            key = (start, end, kk)

            if key in mem:
                return mem[key]
            out = 0

            for i in range(start, end):
                out = max(out, find(start, i, 1) + find(i + 1, end, kk - 1))
            mem[key] = out

            return out

        return find(0, len(nums) - 1, k)


nums = [9, 1, 2, 3, 9]
k = 3
nums = [1, 2, 3, 4, 5, 6, 7]
k = 4
nums = [
    357, 2991, 2815, 2842, 1001, 2933, 2240, 4531, 5155, 1031, 2178, 9865, 583,
    5117, 5777, 9314, 5076, 1533, 8718, 7694, 9367, 1271, 9416, 468, 4987,
    8627, 6031, 5897, 2478, 1926, 7922, 8041, 1309, 5443, 2157, 705, 8399,
    8924, 5110, 5039, 9350, 9581, 3555, 6663, 8944, 6744, 2115, 632, 9109, 3181
]
k = 35
print(Solution().largestSumOfAverages(nums, k))
