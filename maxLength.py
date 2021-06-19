from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def l2n(a):
            return ord(a) - ord('a')

        def search(mem, loc):
            if loc == len(arr):
                return sum(mem)
            new_mem = mem.copy()

            m = search(mem, loc + 1)

            for letter in arr[loc]:
                if new_mem[l2n(letter)] != 0:
                    return m
                new_mem[l2n(letter)] += 1

            return max(m, search(new_mem, loc + 1))

        return search([0] * 26, 0)


sl = Solution()
arr = ["un", "iq", "ue"]
arr = ["cha", "r", "act", "ers"]
arr = ["abcdefghijklmnopqrstuvwxyz"]
print(sl.maxLength(arr))
