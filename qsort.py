from typing import List


def qsort(mem, l, r):
    # print('start',mem,l,r)

    if l >= r:
        return
    loc = max((l + r) // 2 - 3, l)
    mem[loc], mem[l] = mem[l], mem[loc]
    p = l
    q = r

    while p < q:
        while p < q and mem[q] >= mem[p]:
            q -= 1

        if p < q:
            mem[p], mem[q] = mem[q], mem[p]
            p += 1

        while p < q and mem[p] < mem[q]:
            p += 1

        if p < q:
            mem[p], mem[q] = mem[q], mem[p]
            q -= 1
    # print('end',mem,p,q)
    qsort(mem, l, p - 1)
    qsort(mem, q + 1, r)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        qsort(nums, 0, len(nums) - 1)

        return nums


nums = [5, 2, 3, 1]
nums = [5, 1, 1, 2, 0, 0]
print(Solution().sortArray(nums))
