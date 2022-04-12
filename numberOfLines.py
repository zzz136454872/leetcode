from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        mem = [0]

        def l2n(a):
            return ord(a) - ord('a')

        for letter in s:
            tmp = widths[l2n(letter)]

            if mem[-1] + tmp <= 100:
                mem[-1] += tmp
            else:
                mem.append(tmp)

        return [len(mem), mem[-1]]


widths = [
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 10, 10, 10
]
s = "abcdefghijklmnopqrstuvwxyz"
widths = [
    4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 10, 10, 10
]
s = "bbbcccdddaaa"
print(Solution().numberOfLines(widths, s))
