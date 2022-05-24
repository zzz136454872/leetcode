from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        res1 = 0
        n = len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                res1 += 1

        def mergeSort(start, end):
            if start >= end - 1:
                return 0
            mid = (start + end) // 2
            res = mergeSort(start, mid)
            res += mergeSort(mid, end)
            i = start
            j = mid
            tmp = []

            while i < mid and j < end:
                if nums[i] < nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
                    res += mid - i

            if i < mid:
                tmp += nums[i:mid]

            if j < end:
                tmp += nums[j:end]

            for k in range(end - start):
                nums[k + start] = tmp[k]

            return res

        tmp = mergeSort(0, len(nums))

        return tmp == res1


nums = [1, 0, 2]
nums = [1, 2, 0]
print(Solution().isIdealPermutation(nums))
