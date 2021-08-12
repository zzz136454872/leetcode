from typing import List


# 等差数列划分
class Solution1:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        out = 0
        val = -1
        count = 0

        for v in diff:
            if v == val:
                count += 1
                out += count - 1
            else:
                count = 1
                val = v

        return out


def comb(a, b):
    out = 1

    for i in range(b):
        out = out * (a - i) // (i + 1)

    return out


# sl = Solution()
# nums = [1, 2, 3, 4]
# nums = [1]
# print(sl.numberOfArithmeticSlices(nums))


#  等差数列划分 II - 子序列
# fail one: wa
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        mem = {}

        for num in nums:
            mem[num] = mem.get(num, 0) + 1
        out = 0

        for num in mem:
            if mem[num] >= 3:
                tmp = mem[num]
                out += 2**tmp - comb(tmp, 1) - comb(tmp, 2) - 1
        mem1 = set(mem.keys())
        mem = sorted(list(mem.items()))

        # print(mem)

        for i in range(len(mem) - 1):
            for j in range(i + 1, len(mem)):
                diff = mem[j][0] - mem[i][0]
                tmp = mem[j][1] * mem[i][1]
                want = mem[j][0] + diff

                # print(i,j,mem[i][0],mem[j][0],diff,want)

                while True:
                    if want not in mem1:
                        break
                    left = j
                    right = len(mem)

                    while left <= right:
                        mid = (left + right) // 2

                        if mem[mid][0] < want:
                            left = mid + 1
                        elif mem[mid][0] > want:
                            right = mid - 1
                        else:
                            left = mid
                            right = mid - 1

                    if mem[left][0] != want:
                        print('error')

                    tmp *= mem[left][1]
                    out += tmp
                    want += diff

        return out


nums = [2, 4, 6, 8, 10]
nums = [7, 7, 7, 7, 7]
nums = [
    79, 20, 64, 28, 67, 81, 60, 58, 97, 85, 92, 96, 82, 89, 46, 50, 15, 2, 36,
    44, 54, 2, 90, 37, 7, 79, 26, 40, 34, 67, 64, 28, 60, 89, 46, 31, 9, 95,
    43, 19, 47, 64, 48, 95, 80, 31, 47, 19, 72, 99, 28, 46, 13, 9, 64, 4, 68,
    74, 50, 28, 69, 94, 93, 3, 80, 78, 23, 80, 43, 49, 77, 18, 68, 28, 13, 61,
    34, 44, 80, 70, 55, 85, 0, 37, 93, 40, 47, 47, 45, 23, 26, 74, 45, 67, 34,
    20, 33, 71, 48, 96
]
sl = Solution()
print(sl.numberOfArithmeticSlices(nums))
