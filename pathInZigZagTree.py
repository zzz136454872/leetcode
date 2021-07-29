from math import floor, log2
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        depth = floor(log2(label)) + 1
        rowSum = (1 << depth) + (1 << (depth - 1)) - 1
        ret = [0] * depth

        while label > 0:
            depth -= 1
            ret[depth] = label
            label = (rowSum - label) >> 1
            rowSum >>= 1

        return ret


sl = Solution()
label = 7
print(sl.pathInZigZagTree(label))
