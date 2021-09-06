from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def t1(arr):
            n1 = arr.copy()
            out = 0

            for i in range(1, len(n1), 2):
                if i > 0 and n1[i] >= n1[i - 1]:
                    out += n1[i] - n1[i - 1] + 1
                    n1[i] = n1[i - 1] - 1

                if i < len(n1) - 1 and n1[i] >= n1[i + 1]:
                    out += n1[i] - n1[i + 1] + 1

            return out

        def t2(arr):
            n2 = arr.copy()
            out = 0

            for i in range(0, len(n2), 2):
                if i > 0 and n2[i] >= n2[i - 1]:
                    out += n2[i] - n2[i - 1] + 1
                    n2[i] = n2[i - 1] - 1

                if i < len(n2) - 1 and n2[i] >= n2[i + 1]:
                    out += n2[i] - n2[i + 1] + 1
                # print(i,out)

            return out

        return min(t1(nums), t2(nums))


nums = [1, 2, 3]
nums = [9, 6, 1, 6, 2]
nums = [2, 7, 10, 9, 8, 9]
print(Solution().movesToMakeZigzag(nums))
